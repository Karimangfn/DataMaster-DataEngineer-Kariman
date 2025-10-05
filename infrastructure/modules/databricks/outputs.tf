output "databricks_workspace_url" {
  description = "URL of the Databricks workspace"
  value       = azurerm_databricks_workspace.dbw.workspace_url
}

output "databricks_workspace_name" {
  description = "Databricks workspace name"
  value       = azurerm_databricks_workspace.dbw.name
}

output "workspace_resource_id" {
  value = azurerm_databricks_workspace.dbw.id
}
