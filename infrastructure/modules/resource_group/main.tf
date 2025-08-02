resource "random_id" "unique" {
  byte_length = 2
}

resource "azurerm_resource_group" "rg" {
  name     = "${var.prefix}-${random_id.unique.hex}-rg"
  location = var.location
}
