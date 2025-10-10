resource "azurerm_databricks_workspace" "dbw" {
  name                        = "${var.prefix}-${var.random_id}-dbw"
  resource_group_name         = var.resource_group_name
  location                    = var.location
  sku                         = "premium"
  managed_resource_group_name = "${var.prefix}-${var.random_id}-dbw-mrg"
}

locals {
  databricks_catalog_name = replace(azurerm_databricks_workspace.dbw.name, "-", "_")
}

resource "databricks_schema" "data_processing_db" {
  provider      = databricks.accounts
  name          = "data_processing_db"
  catalog_name  = local.databricks_catalog_name
}

locals {
  storage_account = var.storage_account_name

  base_spark_conf = {
    "spark.databricks.cluster.profile"             = "singleNode"
    "spark.master"                                 = "local[*]"
    "spark.databricks.delta.optimizeWrite.enabled" = "true"
    "spark.databricks.delta.autoCompact.enabled"   = "true"
  }

  dynamic_spark_conf = {
  for key, value in {
    "auth.type"              = "OAuth"
    "oauth.provider.type"    = "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
    "oauth2.client.id"       = var.client_id
    "oauth2.client.secret"   = var.client_secret
    "oauth2.client.endpoint" = "https://login.microsoftonline.com/${var.tenant_id}/oauth2/v2.0/token"
     } : "spark.hadoop.fs.azure.account.${key}.${local.storage_account}.dfs.core.windows.net" => value
  }
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

      spark_conf = merge(
        local.base_spark_conf,
        local.dynamic_spark_conf
      )

      custom_tags = {
        "ResourceClass" = "SingleNode"
      }

      data_security_mode = "SINGLE_USER"
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
      parameters  = [
          "--storage-account", var.storage_account_name,
          "--catalog", local.databricks_catalog_name,
          "--database", databricks_schema.data_processing_db.name
      ]
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
      parameters  = [
          "--storage-account", var.storage_account_name,
          "--catalog", local.databricks_catalog_name,
          "--database", databricks_schema.data_processing_db.name
      ]
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
      parameters  = [
          "--storage-account", var.storage_account_name,
          "--catalog", local.databricks_catalog_name,
          "--database", databricks_schema.data_processing_db.name
      ]
    }
  }
}

resource "azurerm_role_assignment" "databricks_blob_contributor" {
  scope                = var.storage_account_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = var.db_access_connector_principal_id
}

resource "databricks_external_location" "bronze" {
  provider        = databricks.accounts
  name            = "bronze_external"
  url             = "abfss://bronze@${var.storage_account_name}.dfs.core.windows.net"
  credential_name = local.databricks_catalog_name
  fallback        = true
  skip_validation = true
  force_update    = true
  comment         = "Bronze external location"
}

resource "databricks_external_location" "silver" {
  provider        = databricks.accounts
  name            = "silver_external"
  url             = "abfss://silver@${var.storage_account_name}.dfs.core.windows.net"
  credential_name = local.databricks_catalog_name
  fallback        = true
  skip_validation = true
  force_update    = true
  comment         = "Silver external location"
}

resource "databricks_external_location" "gold" {
  provider        = databricks.accounts
  name            = "gold_external"
  url             = "abfss://gold@${var.storage_account_name}.dfs.core.windows.net"
  credential_name = local.databricks_catalog_name
  fallback        = true
  skip_validation = true
  force_update    = true
  comment         = "Gold external location"
}
