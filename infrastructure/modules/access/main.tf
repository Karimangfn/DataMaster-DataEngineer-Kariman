data "azuread_service_principal" "github_actions_spn" {
  client_id = var.client_id
}

data "azuread_group" "data_engineers" {
  display_name = var.data_engineers_group
}

data "azuread_group" "data_analysts" {
  display_name = var.data_analysts_group
}

resource "azurerm_role_assignment" "raw_access" {
  scope                = var.raw_container_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = data.azuread_group.data_engineers.object_id
}

resource "azurerm_role_assignment" "bronze_access" {
  scope                = var.bronze_container_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = data.azuread_group.data_engineers.object_id
}

resource "azurerm_role_assignment" "silver_access" {
  scope                = var.silver_container_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = data.azuread_group.data_analysts.object_id
}

resource "azurerm_role_assignment" "gold_access" {
  scope                = var.gold_container_id
  role_definition_name = "Storage Blob Data Reader"
  principal_id         = data.azuread_group.data_analysts.object_id
}
