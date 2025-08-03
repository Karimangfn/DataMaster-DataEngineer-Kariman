resource "random_id" "unique" {
  byte_length = 2
}

resource "azurerm_resource_group" "rg" {
  name     = "mwnsqws-rg"
  location = var.location
}
