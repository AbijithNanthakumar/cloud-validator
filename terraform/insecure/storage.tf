resource "azurerm_storage_account" "bad_storage" {
  name                     = "badstorageacct1234"
  resource_group_name      = "demo-rg"
  location                 = "East US"

  account_tier             = "Standard"
  account_replication_type = "LRS"

  allow_nested_items_to_be_public = true
}