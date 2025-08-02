output "container_registry_name" {
  description = "Name of the Azure Container Registry"
  value       = azurerm_container_registry.acr.name
}

output "container_registry_id" {
  description = "ID of the Azure Container Registry"
  value       = azurerm_container_registry.acr.id
}
