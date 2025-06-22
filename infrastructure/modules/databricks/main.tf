resource "databricks_job" "transform_clean_data_process" {
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

  task {
    task_key        = "bronze_layer"
    description     = "Bronze data transformation"
    job_cluster_key = "data_process_cluster"

    notebook_task {
      source        = "GIT"
      notebook_path = "data-processing/bronze/main.ipynb"

      git_source {
        git_url    = var.git_repo_url
        git_branch = var.git_repo_branch
      }
    }
  }

  task {
    task_key        = "silver_layer"
    description     = "Silver data transformation"
    job_cluster_key = "data_process_cluster"

    depends_on {
      task_key = "bronze_layer"
    }

    notebook_task {
      source        = "GIT"
      notebook_path = "data-processing/silver/main.ipynb"

      git_source {
        git_url    = var.git_repo_url
        git_branch = var.git_repo_branch
      }
    }
  }

  task {
    task_key        = "gold_layer"
    description     = "Gold data transformation"
    job_cluster_key = "data_process_cluster"

    depends_on {
      task_key = "silver_layer"
    }

    notebook_task {
      source        = "GIT"
      notebook_path = "data-processing/gold/main.ipynb"

      git_source {
        git_url    = var.git_repo_url
        git_branch = var.git_repo_branch
      }
    }
  }
}
