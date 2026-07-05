resource "azurerm_linux_virtual_machine" "bad_vm" {
  name                = "bad-vm"
  resource_group_name = "demo-rg"
  location            = "East US"
  size                = "Standard_B1s"

  admin_username = "adminuser"

  disable_password_authentication = false
}