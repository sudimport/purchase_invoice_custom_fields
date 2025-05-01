import frappe
# importiamo la funzione ufficiale con un alias
from frappe.custom.doctype.custom_field.custom_field import create_custom_field as _create_custom_field

def create_supplier_part_field():
    """Patch: crea custom_supplier_part_number su Purchase Invoice Item."""
    if not frappe.db.exists("Custom Field", {
            "dt": "Purchase Invoice Item",
            "fieldname": "custom_supplier_part_number"
        }):
        # chiamiamo l’alias per evitare ricorsione
        _create_custom_field("Purchase Invoice Item", {
            "fieldname": "custom_supplier_part_number",
            "label": "Supplier Part Number",
            "fieldtype": "Data",
            "insert_after": "item_code",
            "in_list_view": 1
        })
