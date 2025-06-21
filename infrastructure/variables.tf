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
}

variable "client_secret" {
  description = "Azure Service Principal Client Secret"
  type        = string
  sensitive   = true
}

variable "tenant_id" {
  description = "Azure Tenant ID"
  type        = string
  sensitive   = true
}

variable "git_repo_url" {
  description = "URL do repositório Git para vincular no Databricks"
  type        = string
}

variable "git_repo_branch" {
  description = "Branch do repositório Git"
  type        = string
  default     = "develop"
}
