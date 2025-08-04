resource "azurerm_databricks_workspace" "dbw" {
  name                        = "${var.prefix}-${var.random_id}-dbw"
  resource_group_name         = var.resource_group_name
  location                    = var.location
  sku                         = "standard"
  managed_resource_group_name = "${var.prefix}-${var.random_id}-dbw-mrg"
}

resource "databricks_job" "data_process" {
  provider = databricks.this

  name = "transform-clean-data-process"

  job_cluster {
    job_cluster_key = "data_process_cluster"

    new_cluster {
      num_workers   = 0
      spark_version = "15.4.x-scala2.12"
      node_type_id  = "Standard_F4"

      spark_conf = {
        "spark.databricks.cluster.profile" = "singleNode"
        "spark.master"                     = "local[*]"
      }

      custom_tags = {
        "ResourceClass" = "SingleNode"
      }
    }
  }

  git_source {
    url      = var.git_repo_url
    provider = "gitHub"
    branch   = var.git_repo_branch
  }

  task {
    task_key        = "bronze_layer"
    description     = "Bronze data transformation"
    job_cluster_key = "data_process_cluster"

    spark_python_task {
      source      = "GIT"
      python_file = "data-processing/bronze/src/main.py"
    }
  }

  task {
    task_key        = "silver_layer"
    description     = "Silver data transformation"
    job_cluster_key = "data_process_cluster"

    depends_on {
      task_key = "bronze_layer"
    }

    spark_python_task {
      source      = "GIT"
      python_file = "data-processing/silver/src/main.py"
    }
  }

  task {
    task_key        = "gold_layer"
    description     = "Gold data transformation"
    job_cluster_key = "data_process_cluster"

    depends_on {
      task_key = "silver_layer"
    }

    spark_python_task {
      source      = "GIT"
      python_file = "data-processing/gold/src/main.py"
    }
  }
}
