# Enterprise Support MCP Server

A local MCP server for the Enterprise Support Intelligence demonstration.

## What it provides

| MCP tool | Purpose | Data source |
|---|---|---|
| `check_service_status` | Check VPN, Wi-Fi, DNS, Email, Internet or Business Application status | `data/services.json` synthetic data |
| `get_ticket_status` | Retrieve a ticket by reference | Local SQLite |
| `create_support_ticket` | Validate and create a support ticket | Local SQLite |

## Important scope

This is a **local demonstration**, not a connection to a real company network,
service-monitoring platform, ticketing system, Power Automate flow or Dataverse.
The service status records are synthetic and must never be presented as live
corporate service status.

The server uses standard input/output (stdio) as its default MCP transport.
This is appropriate for a local MCP client. It is not directly reachable by a
cloud-hosted Foundry agent. A later cloud integration requires a reachable
MCP endpoint, suitable hosting and authentication.

## Requirements

- Python 3.11 or later
- pip

## Windows setup (PowerShell)

From this folder:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Run tests

```powershell
python -m unittest discover -s tests -v
```

## Start the MCP server

```powershell
python server.py
```

The process waits for an MCP client over stdio. It may appear to do nothing
when started directly in a terminal; that is expected. Do not type normal
messages into its terminal.

## Database

The SQLite database is created automatically at:

```text
data/support_tickets.db
```

To use another path, set `SUPPORT_DB_PATH` before starting the server.

## Tool behavior

### check_service_status(service_name)

Example service names: `VPN`, `Wi-Fi`, `DNS`, `Email`, `Internet`,
`Business Application`.

Returns `data_source: synthetic_local_demo_data`.

### create_support_ticket(...)

Required fields:
- `issue_summary`
- `description`
- `category`: Network, VPN, DNS, Wi-Fi, Email, Application, Other
- `priority`: Low, Medium, High, Critical
- `affected_service`: VPN, Wi-Fi, DNS, Email, Internet, Business Application

Optional field:
- `location`

Returns a generated `INC-XXXXXXXX` reference only after the SQLite insert succeeds.
The agent should obtain user confirmation before invoking this tool.

### get_ticket_status(ticket_id)

Returns the stored ticket if it exists, otherwise a not-found response.

## Security notes

- Do not enter real employee records or production incidents.
- Never include passwords, OTPs or other secrets in ticket descriptions.
- The server binds to localhost by default.
- Do not expose it to the internet without authentication, authorization,
  transport security, input controls and operational review.
