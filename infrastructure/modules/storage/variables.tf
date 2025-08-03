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
  type        = string
  description = "Client ID of the SPN used in GitHub Actions"
}
