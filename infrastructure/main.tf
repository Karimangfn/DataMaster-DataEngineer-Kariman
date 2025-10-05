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

module "aks" {
  source                = "./modules/aks"
  prefix                = var.prefix
  random_id             = module.resource_group.random_id
  resource_group_name   = module.resource_group.resource_group_name
  location              = module.resource_group.resource_group_location
  container_registry_id = module.acr.container_registry_id
}

module "storage" {
  source              = "./modules/storage"
  prefix              = var.prefix
  random_id           = module.resource_group.random_id
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location
  client_id           = var.client_id
}

module "databricks" {
  source                = "./modules/databricks"
  prefix                = var.prefix
  random_id             = module.resource_group.random_id
  location              = module.resource_group.resource_group_location
  resource_group_name   = module.resource_group.resource_group_name
  storage_account_name  = module.storage.storage_account_name
  client_id             = var.client_id
  client_secret         = var.client_secret
  tenant_id             = var.tenant_id
  git_repo_url          = var.git_repo_url
  git_repo_branch       = var.git_repo_branch
  enable                = var.enable_databricks
}

module "access" {
  source                = "./modules/access"
  prefix                = var.prefix
  raw_container_id      = module.storage.raw_container_id
  bronze_container_id   = module.storage.bronze_container_id
  silver_container_id   = module.storage.silver_container_id
  gold_container_id     = module.storage.gold_container_id
  data_engineers_group  = var.data_engineers_group
  data_analysts_group   = var.data_analysts_group
  client_id             = var.client_id
}
