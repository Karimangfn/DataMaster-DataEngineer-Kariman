terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.20.0"
    }
  }
}

provider "databricks" {
  alias = "this"

  azure_client_id       = var.client_id
  azure_client_secret   = var.client_secret
  azure_tenant_id       = var.tenant_id
  azure_workspace_resource_id = var.workspace_resource_id
}
