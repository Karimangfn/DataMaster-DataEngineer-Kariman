terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 4.9.0"
    }
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.20.0"
    }
  }

  required_version = ">= 1.5.7"
}

provider "azurerm" {
  subscription_id = var.subscription_id

  features {
    key_vault {
      purge_soft_delete_on_destroy = false
    }
  }
}

provider "databricks" {
  azure_client_id   = var.client_id
  azure_client_secret = var.client_secret
  azure_tenant_id   = var.tenant_id
  azure_workspace_resource_id = azurerm_databricks_workspace.dbw.id
}
