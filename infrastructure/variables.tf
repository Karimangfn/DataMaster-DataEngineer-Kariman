variable "prefix" {
  description = "Prefix for all resource names"
  type        = string
  default     = "dtmstr001"
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
  default     = "East US"
}

variable "suffix" {
  description = "Suffix for all resource names"
  type        = string
}

