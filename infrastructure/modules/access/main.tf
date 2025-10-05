resource "azuread_group" "data_engineers" {
  display_name = var.data_engineers_group
}

resource "azuread_group" "data_analysts" {
  display_name = var.data_analysts_group
}

resource "azuread_group" "data_scientists" {
  display_name = var.data_scientists_group
}

locals {
  containers = ["raw", "bronze", "silver", "gold"]
}

resource "azurerm_storage_data_lake_gen2_path" "permissions" {
  for_each = {
    "raw"    = azuread_group.data_engineers.id
    "bronze" = azuread_group.data_engineers.id
    "silver" = azuread_group.data_engineers.id
    "gold"   = azuread_group.data_analysts.id
  }

  filesystem_name    = each.key
  path               = "/"
  storage_account_id = var.storage_account_id
  role               = "Storage Blob Data Contributor"
  principal_id       = each.value
}
