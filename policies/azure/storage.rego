package cloudvalidator.azure

deny contains msg if {
    input.resource.type == "azurerm_storage_account"
    input.resource.public_access == true

    msg := "Storage Account should not allow public access."
}