variable "raw_container_id" {
  type        = string
  description = "ID of the Raw container in the Storage Account"
}

variable "bronze_container_id" {
  type        = string
  description = "ID of the Bronze container in the Storage Account"
}

variable "silver_container_id" {
  type        = string
  description = "ID of the Silver container in the Storage Account"
}

variable "gold_container_id" {
  type        = string
  description = "ID of the Gold container in the Storage Account"
}

variable "data_engineers_group" {
  type        = string
  description = "Name of the Data Engineers group in Azure AD"
}

variable "data_analysts_group" {
  type        = string
  description = "Name of the Data Analysts group in Azure AD"
}

variable "client_id" {
  type        = string
  description = "Client ID of the Service Principal used by GitHub Actions"
}
