# Copyright (c) 2014, Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cint
from frappe.model.naming import make_autoname

def get_certificates(sales_order):
	return frappe.db.sql_list("""select name from `tabSerial No`
			where sales_order=%s and docstatus < 2""", sales_order)

def validate_if_certificates_exist(doc, method):
	"""called on on_cancel of Sales Order"""
	certificates = get_certificates(doc.name)
	if certificates:
		frappe.throw(_("""Cannot cancel Sales Order because one or more certificates exist against this Sales Order. Certificate Nos: {}""").format(", ".join(certificates)))

def autoname(doc, method):
	if not doc.sales_order:
		frappe.throw("Sales Order is required")

	doc.name = make_autoname("CR/{}/.####".format(doc.sales_order))

def block_rename(doc, method, old, new, merge):
	frappe.throw("Certificate cannot be renamed")

def update_certificates_in_sales_order(doc, method):
	certificates = get_certificates(doc.sales_order)
	if method=="on_trash" and doc.name in certificates:
		certificates.remove(doc.name)

	max_certificates = cint(frappe.db.get_value("Sales Order", doc.sales_order, "no_of_certificate"))

	if len(certificates) > max_certificates:
		frappe.throw(_("You cannot create more than {0} certificates against Sales Order {1}").format(max_certificates, doc.sales_order))

	else:
		frappe.db.set_value("Sales Order", doc.sales_order, "certificates_created", ", ".join(certificates))
