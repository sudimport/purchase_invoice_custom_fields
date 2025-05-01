app_name = "purchase_invoice_custom_fields"
app_title = "Purchase Invoice Custom Fields"
app_publisher = "Thomas"
app_description = "Aggiunge il campo 'Codice fornitore' alla tabella delle fatture di acquisto"
app_email = "thomas@example.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            ["dt", "=", "Purchase Invoice Item"],
            ["fieldname", "=", "custom_supplier_part_number"]
        ]
    }
]

# -- Aggiungi questa riga:
after_migrate = ["purchase_invoice_custom_fields.patches.create_custom_field"]
