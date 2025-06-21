variable "client_id" {
  type = string
}

variable "client_secret" {
  type = string
}

variable "tenant_id" {
  type = string
}

variable "workspace_resource_id" {
  type = string
}

variable "git_repo_url" {
  type = string
}

variable "git_repo_branch" {
  type = string
}

variable "enable" {
  type    = bool
  default = false
}
