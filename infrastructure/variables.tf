variable "prefix" {
  description = "Prefix for all resource names"
  type        = string
  default     = "dtmstr"
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
  default     = "East US"
}

variable "subscription_id" {
  type = string
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
  default     = "https://github.com/user/repository.git"
}

variable "git_repo_branch" {
  description = "Git branch to be used in the Databricks repo integration"
  type        = string
  default     = "develop"
}

variable "enable_databricks" {
  description = "Control Variable for Databricks"
  type        = bool
  default     = true
}

variable "databricks_access_connector_principal_id" {
  description = "Principal ID da Managed Identity do Access Connector do Databricks"
  type        = string
}
