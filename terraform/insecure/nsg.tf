resource "azurerm_network_security_group" "bad_nsg" {
  name                = "bad-nsg"
  location            = "East US"
  resource_group_name = "demo-rg"

  security_rule {
    name                       = "allow-rdp"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "3389"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

