terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 4.9.0"
    }
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.20.0"
    }
  }

  required_version = ">= 1.5.7"
}

provider "azurerm" {
  subscription_id = var.subscription_id

  features {}
}
