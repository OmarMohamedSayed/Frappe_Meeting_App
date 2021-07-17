# Copyright (c) 2021, Omar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		"""Calling before saving model"""
		"""Set Missing Names"""
		found = []
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee)
			
			if attendee.attendee in found:
				frappe.throw(_(f"Attendee {attendee.attendee} entered twice"))
			
			found.append(attendee.attendee)

# to make function accessable from client side
@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User",attendee)
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))
	