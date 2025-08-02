data "azurerm_client_config" "current" {}

module "resource_group" {
  source  = "./modules/resource_group"
  prefix  = var.prefix
  location = var.location
}

module "acr" {
  source              = "./modules/acr"
  prefix              = var.prefix
  random_id           = module.resource_group.random_id
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location
}

module "key_vault" {
  source              = "./modules/key_vault"
  prefix              = var.prefix
  random_id           = module.resource_group.random_id
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location
  tenant_id           = data.azurerm_client_config.current.tenant_id
}

module "aks" {
  source                = "./modules/aks"
  prefix                = var.prefix
  random_id             = module.resource_group.random_id
  resource_group_name   = module.resource_group.resource_group_name
  location              = module.resource_group.resource_group_location
  container_registry_id = module.acr.container_registry_id
}

resource "azurerm_databricks_workspace" "dbw" {
  name                        = "${var.prefix}-${module.resource_group.random_id}-dbw"
  resource_group_name         = module.resource_group.resource_group_name
  location                    = module.resource_group.resource_group_location
  sku                         = "standard"
  managed_resource_group_name = "${var.prefix}-${module.resource_group.random_id}-dbw-mrg"
}

module "databricks" {
  source = "./modules/databricks"

  client_id     = var.client_id
  client_secret = var.client_secret
  tenant_id     = var.tenant_id

  git_repo_url     = var.git_repo_url
  git_repo_branch  = var.git_repo_branch
  workspace_resource_id = azurerm_databricks_workspace.dbw.id

  enable = var.enable_databricks
}

module "storage" {
  source              = "./modules/storage"
  prefix              = var.prefix
  random_id           = module.resource_group.random_id
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location
}
