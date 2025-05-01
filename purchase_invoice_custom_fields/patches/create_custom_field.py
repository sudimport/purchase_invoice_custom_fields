import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def create_custom_field():
    """Patch: crea custom_supplier_part_number su Purchase Invoice Item."""
    if not frappe.db.exists("Custom Field", {
            "dt": "Purchase Invoice Item",
            "fieldname": "custom_supplier_part_number"
        }):
        create_custom_field("Purchase Invoice Item", {
            "fieldname": "custom_supplier_part_number",
            "label": "Supplier Part Number",
            "fieldtype": "Data",
            "insert_after": "item_code",
            "in_list_view": 1
        })
