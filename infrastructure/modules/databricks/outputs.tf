output "databricks_workspace_url" {
  description = "URL of the Databricks workspace"
  value       = azurerm_databricks_workspace.dbw.workspace_url
}

output "workspace_resource_id" {
  value = azurerm_databricks_workspace.dbw.id
}
