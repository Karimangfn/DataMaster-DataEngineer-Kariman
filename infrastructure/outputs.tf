output "resource_group_name" {
  description = "Name of the created Resource Group"
  value       = azurerm_resource_group.rg.name
}

output "storage_account_name" {
  description = "Name of the created Storage Account"
  value       = azurerm_storage_account.lake.name
}

output "container_registry_name" {
  description = "Name of the Azure Container Registry"
  value       = azurerm_container_registry.acr.name
}

output "key_vault_name" {
  description = "Name of the Key Vault"
  value       = azurerm_key_vault.kv.name
}

output "kubernetes_cluster_name" {
  description = "Name of the AKS cluster"
  value       = azurerm_kubernetes_cluster.aks.name
}

output "kube_config" {
  description = "Raw Kubernetes configuration for the AKS cluster"
  value       = azurerm_kubernetes_cluster.aks.kube_config_raw
  sensitive   = true
}

output "databricks_workspace_url" {
  description = "URL of the Databricks workspace"
  value       = azurerm_databricks_workspace.dbw.workspace_url
}