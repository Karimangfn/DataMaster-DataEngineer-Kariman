output "storage_account_name" {
  description = "Name of the created Storage Account"
  value       = azurerm_storage_account.lake.name
}

output "storage_account_id" {
  description = "ID of the created Storage Account"
  value = azurerm_storage_account.lake.id
}

output "raw_container_id" {
  description = "ID of the 'raw' storage container"
  value       = azurerm_storage_container.raw.id
}

output "bronze_container_id" {
  description = "ID of the 'bronze' storage container"
  value       = azurerm_storage_container.bronze.id
}

output "silver_container_id" {
  description = "ID of the 'silver' storage container"
  value       = azurerm_storage_container.silver.id
}

output "gold_container_id" {
  description = "ID of the 'gold' storage container"
  value       = azurerm_storage_container.gold.id
}
