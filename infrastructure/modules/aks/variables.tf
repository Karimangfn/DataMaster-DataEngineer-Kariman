variable "prefix" {
  description = "Prefix for all resource names"
  type        = string
}

variable "random_id" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
}

variable "container_registry_id" {
  type = string
}
