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

