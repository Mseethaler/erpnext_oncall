import frappe

def after_install():
    create_setup_tasks()

def create_setup_tasks():
    tasks = [
        "Add on-call staff in ERPNext On Call Settings",
        "Ensure all staff have phone numbers on their Employee records",
        "Import N8n workflow: inbound call routing",
        "Wire call provider credentials in N8n (Twilio or other)",
        "Set default voicemail number in N8n workflow",
        "Activate N8n workflow",
        "Test: call inbound number, confirm routing to on-call staff",
    ]

    for task in tasks:
        frappe.get_doc({
            "doctype": "ToDo",
            "description": task,
            "status": "Open",
            "owner": frappe.session.user
        }).insert(ignore_permissions=True)
