app_name = "purchase_invoice_custom_fields"
app_title = "Purchase Invoice Custom Fields"
app_publisher = "Thomas"
app_description = "Aggiunge il campo 'Codice fornitore' alla tabella delle fatture di acquisto"
app_email = "thomas@example.com"
app_license = "MIT"

after_migrate = ["purchase_invoice_custom_fields.patches.create_supplier_part_field"]
