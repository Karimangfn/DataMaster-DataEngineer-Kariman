output "databricks_workspace_url" {
  description = "URL of the Databricks workspace"
  value       = azurerm_databricks_workspace.dbw.workspace_url
}

output "workspace_resource_id" {
  value = azurerm_databricks_workspace.dbw.id
}

output "databricks_access_connector_id" {
  description = "Resource ID of the Databricks Access Connector"
  value       = azurerm_databricks_access_connector.connect-unity.id
}

output "databricks_access_connector_principal_id" {
  description = "Principal ID (objectId) of the Access Connector managed identity"
  value       = azurerm_databricks_access_connector.connect-unity.identity[0].principal_id
}
