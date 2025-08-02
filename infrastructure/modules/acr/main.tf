resource "azurerm_container_registry" "acr" {
  name                = "${var.prefix}${var.random_id}acr"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "Basic"
  admin_enabled       = false
}
