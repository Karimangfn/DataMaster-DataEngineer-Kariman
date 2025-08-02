variable "prefix" {
  type = string
}

variable "random_id" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "location" {
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

variable "workspace_resource_id" {
  type = string
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
