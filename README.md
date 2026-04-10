# ERPNext On Call

A lightweight Frappe/ERPNext app that maintains an on-call staff list for 
inbound call routing via N8n or any automation platform.

## What it does

Provides a single **On Call Settings** doctype where managers set which 
staff members are currently on call. Each row automatically pulls the 
employee's mobile number from their Employee record.

N8n (or any webhook consumer) can query this list via the ERPNext REST API 
to determine who to route inbound calls to.

## Doctypes

**On Call Settings** (Single)
- `on_call_staff` — child table of on-call staff

**On Call Staff** (Child Table)
- `employee` — Link → Employee
- `employee_mobile` — Data, auto-fetched from `employee.cell_number`

## How it integrates

N8n queries the on-call list via ERPNext REST API:

GET /api/resource/On Call Settings/On Call Settings


The response includes the `on_call_staff` child table with employee names 
and mobile numbers. N8n then routes the call to the first available person, 
falling back to voicemail if the list is empty.

## Requirements

- ERPNext v15
- Employee records with mobile numbers populated
- N8n (or equivalent) for call routing logic
- Twilio or any call provider that supports webhooks

## Installation

Add to `apps.json` at Docker build time:
```json
{
    "url": "https://github.com/Mseethaler/erpnext_oncall",
    "branch": "main"
}
```

Then install on your site:
```bash
bench --site [your-site] install-app erpnext_oncall
```

## Setup

On install a ToDo checklist is created guiding you through:
- Adding on-call staff in On Call Settings
- Ensuring employee mobile numbers are populated
- Importing and wiring the N8n call routing workflow
- Testing end-to-end call routing
