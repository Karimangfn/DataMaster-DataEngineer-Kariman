data "azuread_service_principal" "github_actions_spn" {
  client_id = var.client_id
}

resource "azurerm_storage_account" "lake" {
  name                     = "${var.prefix}${var.random_id}lake"
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
}

resource "azurerm_role_assignment" "spn_storage_blob_contributor" {
  scope                = azurerm_storage_account.lake.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = data.azuread_service_principal.github_actions_spn.object_id
}

resource "azurerm_storage_container" "raw" {
  name                  = "raw"
  storage_account_id    = azurerm_storage_account.lake.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "bronze" {
  name                  = "bronze"
  storage_account_id    = azurerm_storage_account.lake.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "silver" {
  name                  = "silver"
  storage_account_id    = azurerm_storage_account.lake.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "gold" {
  name                  = "gold"
  storage_account_id    = azurerm_storage_account.lake.id
  container_access_type = "private"
}
