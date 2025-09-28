output "resource_group_name" {
  description = "Name of the created Resource Group"
  value       = module.resource_group.resource_group_name
}

output "storage_account_name" {
  description = "Name of the created Storage Account"
  value       = module.storage.storage_account_name
}

output "container_registry_name" {
  description = "Name of the Azure Container Registry"
  value       = module.acr.container_registry_name
}

output "kubernetes_cluster_name" {
  description = "Name of the AKS cluster"
  value       = module.aks.kubernetes_cluster_name
}

output "kube_config" {
  description = "Raw Kubernetes configuration for the AKS cluster"
  value       = module.aks.kube_config
  sensitive   = true
}

output "databricks_workspace_url" {
  description = "URL of the Databricks workspace"
  value       = module.databricks.databricks_workspace_url
}
