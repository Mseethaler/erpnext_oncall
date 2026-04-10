app_name = "erpnext_oncall"
app_title = "ERPNext On Call"
app_publisher = "Digital Sovereignty"
app_description = "Manages on-call staff list for inbound call routing via N8n"
app_version = "0.0.1"
app_email = "info@digital-sovereignty.cc"
app_license = "MIT"

after_install = "erpnext_oncall.setup.install.after_install"

fixtures = [
    {
        "dt": "DocType",
        "filters": [["name", "in", ["On Call Settings", "On Call Staff"]]]
    },
]
