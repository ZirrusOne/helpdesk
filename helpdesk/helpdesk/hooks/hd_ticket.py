import frappe

def update_email_account(doc, method):
    # Check if the communication linked to the HD Ticket has an email account
    communication = frappe.get_all("Communication", filters={"reference_doctype": "HD Ticket", "reference_name": doc.name}, fields=["email_account"], limit=1)

    if communication and communication[0].get("email_account"):
        # Update the Email Account field in the HD Ticket
        doc.email_account = communication[0].get("email_account")
        doc.save()
