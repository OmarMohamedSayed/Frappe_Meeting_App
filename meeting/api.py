from re import sub
import frappe
from frappe import _
@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("Meeting",meeting)
    meeting.check_permission("email")

    meeting.has_permission

    if meeting.status == "Planned":
        frappe.sendmail(
            recipients=[u.attendee for u in meeting.attendees],
            sender=frappe.session.user,
            subject=meeting.title,
            message=meeting.invitation_message,
            reference_doctype=meeting.doctype,
            reference_name=meeting.name,

        )

        meeting.status = "Invitation Sent"
        meeting.save()
        frappe.msgprint(_("Invitation Sent"))

    else:
        frappe.msgprint(_("Meetin Status must be Planned"))