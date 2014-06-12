app_name = "southwest_certification"
app_title = "Southwest Certification ERPNext Extension"
app_publisher = "Anand Doshi"
app_description = "Southwest Certification ERPNext Extension"
app_icon = "icon-certificate"
app_color = "#03BDD6"
app_email = "anand@frappe.io"
app_url = "https://github.com/anandpdoshi/southwest_certification"
app_version = "0.0.1"
hide_in_installer = True

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/southwest_certification/css/southwest_certification.css"
# app_include_js = "/assets/southwest_certification/js/southwest_certification.js"

# include js, css files in header of web template
# web_include_css = "/assets/southwest_certification/css/southwest_certification.css"
# web_include_js = "/assets/southwest_certification/js/southwest_certification.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Installation
# ------------

# before_install = "southwest_certification.install.before_install"
# after_install = "southwest_certification.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "southwest_certification.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"on_cancel": "southwest_certification.southwest_certification.serial_no.validate_if_certificates_exist"
	},
	"Serial No": {
		"autoname": "southwest_certification.southwest_certification.serial_no.autoname",
		"on_update": "southwest_certification.southwest_certification.serial_no.update_certificates_in_sales_order",
		"before_rename": "southwest_certification.southwest_certification.serial_no.block_rename",
		"on_trash": "southwest_certification.southwest_certification.serial_no.update_certificates_in_sales_order"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"southwest_certification.tasks.all"
# 	],
# 	"daily": [
# 		"southwest_certification.tasks.daily"
# 	],
# 	"hourly": [
# 		"southwest_certification.tasks.hourly"
# 	],
# 	"weekly": [
# 		"southwest_certification.tasks.weekly"
# 	]
# 	"monthly": [
# 		"southwest_certification.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "southwest_certification.install.before_tests"

