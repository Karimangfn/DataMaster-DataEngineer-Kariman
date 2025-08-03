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

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
}

variable "container_registry_id" {
  description = "The resource ID of the Azure Container Registry"
  type        = string
}
