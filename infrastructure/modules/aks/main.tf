resource "azurerm_kubernetes_cluster" "aks" {
  name                = "${var.prefix}${var.random_id}aks"
  location            = var.location
  resource_group_name = var.resource_group_name
  dns_prefix          = "${var.prefix}-${var.random_id}aks"

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
  location            = var.location
  resource_group_name = var.resource_group_name
}

resource "azurerm_role_assignment" "aks_acr_pull" {
  scope                = var.container_registry_id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id
  skip_service_principal_aad_check = true
}
