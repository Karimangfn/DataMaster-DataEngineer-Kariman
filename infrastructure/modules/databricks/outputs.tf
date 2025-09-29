output "databricks_workspace_url" {
  description = "URL of the Databricks workspace"
  value       = azurerm_databricks_workspace.dbw.workspace_url
}

output "workspace_resource_id" {
  value = azurerm_databricks_workspace.dbw.id
}

output "databricks_catalog_name" {
  description = "Name of the Databricks Unity Catalog for this workspace"
  value       = local.databricks_catalog_name
}
