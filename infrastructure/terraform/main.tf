terraform {
  required_version = ">= 1.6.0"
  required_providers { azurerm = { source = "hashicorp/azurerm", version = "~> 4.0" } }
}
provider "azurerm" { features {} }
variable "location" { default = "westeurope" }
variable "resource_group_name" { default = "rg-ecommerce-data-platform" }
resource "azurerm_resource_group" "rg" { name = var.resource_group_name; location = var.location }
resource "azurerm_storage_account" "lake" {
  name = "ecommercedatalake12345"
  resource_group_name = azurerm_resource_group.rg.name
  location = azurerm_resource_group.rg.location
  account_tier = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled = true
}
