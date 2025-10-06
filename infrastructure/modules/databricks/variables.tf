variable "prefix" {
  description = "Prefix for all resource names"
  type        = string
}

variable "random_id" {
  description = "Unique random suffix to avoid naming collisions"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group where resources will be deployed"
  type        = string
}

variable "storage_account_name" {
  type        = string
  description = "Name of the Azure Storage Account for Jobs"
}

variable "db_access_connector_principal_id" {
  type        = string
  description = "Principal ID da Managed Identity do Access Connector do Databricks"
}

variable "storage_account_id" {
  type        = string
  description = "ID do Storage Account que será usado para role assignment e external locations"
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
}

variable "client_id" {
  description = "Azure Service Principal Client ID"
  type        = string
  sensitive   = true
  default     = ""
}

variable "client_secret" {
  description = "Azure Service Principal Client Secret"
  type        = string
  sensitive   = true
  default     = ""
}

variable "tenant_id" {
  description = "Azure Tenant ID"
  type        = string
  sensitive   = true
  default     = ""
}

variable "git_repo_url" {
  description = "URL of the Git repository to link with the Databricks workspace"
  type        = string
  default     = ""
}

variable "git_repo_branch" {
  description = "Git branch to be used in the Databricks repo integration"
  type        = string
  default     = "develop"
}

variable "enable" {
  type    = bool
  default = false
}
