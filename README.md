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

N8n queries the on-call list via ERPNext REST API:ll
