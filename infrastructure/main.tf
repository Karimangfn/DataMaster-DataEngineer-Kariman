resource "random_id" "unique" {
  byte_length = 2
}

resource "azurerm_resource_group" "rg" {
  name     = "${var.prefix}-${random_id.unique.hex}-rg"
  location = var.location

  tags = {
    environment = "dev"
    updated_by  = "ci-cd"
  }
}

resource "azurerm_container_registry" "acr" {
  name                = "${var.prefix}${random_id.unique.hex}acr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = false
}

resource "azurerm_key_vault" "kv" {
  name                        = "${var.prefix}${random_id.unique.hex}akv"
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
  purge_protection_enabled    = false
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "${var.prefix}${random_id.unique.hex}aks"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "${var.prefix}-${random_id.unique.hex}aks"

  default_node_pool {
    name                 = "default"
    auto_scaling_enabled = true
    min_count            = 1
    max_count            = 2
    vm_size              = "Standard_D2als_v6"
    os_disk_size_gb      = 30
    max_pods             = 30
    zones                = []
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin = "azure"
  }

  sku_tier = "Free"
  role_based_access_control_enabled = true
  local_account_disabled            = false
}

resource "azurerm_network_watcher" "default" {
  name                = "NetworkWatcher_eastus"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_role_assignment" "aks_acr_pull" {
  scope                = azurerm_container_registry.acr.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id
  skip_service_principal_aad_check = true
}

resource "azurerm_databricks_workspace" "dbw" {
  name                = "${var.prefix}-${random_id.unique.hex}-dbw"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "standard"

    tags = {
    environment = "dev"
    updated_by  = "ci-cd"
  }

managed_resource_group_name = "${var.prefix}-${random_id.unique.hex}-dbw-mrg"
}

resource "azurerm_storage_account" "lake" {
  name                     = "${var.prefix}${random_id.unique.hex}lake"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
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
