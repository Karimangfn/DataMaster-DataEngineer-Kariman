terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.30.0"
    }
  }
}

provider "databricks" {
  alias                       = "this"
  azure_client_id             = var.client_id
  azure_client_secret         = var.client_secret
  azure_tenant_id             = var.tenant_id
  azure_workspace_resource_id = azurerm_databricks_workspace.dbw.id
  host                        = azurerm_databricks_workspace.dbw.workspace_url
}
