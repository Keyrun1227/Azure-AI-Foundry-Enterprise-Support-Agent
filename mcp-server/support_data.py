import json
import os
import re
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from contextlib import closing

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DB_PATH = Path(os.getenv("SUPPORT_DB_PATH", str(DATA_DIR / "support_tickets.db")))
SERVICES_PATH = DATA_DIR / "services.json"

ALLOWED_CATEGORIES = {"Network", "VPN", "DNS", "Wi-Fi", "Email", "Application", "Other"}
ALLOWED_PRIORITIES = {"Low", "Medium", "High", "Critical"}
ALLOWED_SERVICES = {"VPN", "Wi-Fi", "DNS", "Email", "Internet", "Business Application"}

def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def _connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    with closing(_connect()) as conn, conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS support_tickets (
                ticket_id TEXT PRIMARY KEY,
                issue_summary TEXT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL,
                affected_service TEXT NOT NULL,
                location TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)

def check_service_status(service_name: str) -> dict:
    if not isinstance(service_name, str) or not service_name.strip():
        return {"success": False, "error": "service_name is required."}
    try:
        services = json.loads(SERVICES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"success": False, "error": "Demo service data is unavailable."}

    requested = service_name.strip().casefold()
    match = next((v for k, v in services.items() if k.casefold() == requested), None)
    if match is None:
        return {
            "success": False,
            "error": "Unsupported service.",
            "supported_services": sorted(services.keys()),
        }
    return {
        "success": True,
        "data_source": "synthetic_local_demo_data",
        "service": service_name.strip(),
        **match,
    }

def create_support_ticket(
    issue_summary: str,
    description: str,
    category: str,
    priority: str,
    affected_service: str,
    location: str = "Not provided",
) -> dict:
    fields = {
        "issue_summary": issue_summary,
        "description": description,
        "category": category,
        "priority": priority,
        "affected_service": affected_service,
        "location": location,
    }
    for name, value in fields.items():
        if not isinstance(value, str) or not value.strip():
            return {"success": False, "error": f"{name} is required."}
        if len(value.strip()) > (2000 if name == "description" else 200):
            return {"success": False, "error": f"{name} exceeds the allowed length."}

    if category not in ALLOWED_CATEGORIES:
        return {"success": False, "error": "Invalid category.", "allowed": sorted(ALLOWED_CATEGORIES)}
    if priority not in ALLOWED_PRIORITIES:
        return {"success": False, "error": "Invalid priority.", "allowed": sorted(ALLOWED_PRIORITIES)}
    if affected_service not in ALLOWED_SERVICES:
        return {"success": False, "error": "Invalid affected_service.", "allowed": sorted(ALLOWED_SERVICES)}

    # Prevent accidental storage of obvious secrets in demo ticket text.
    sensitive_patterns = [
        r"(?i)\bpassword\s*[:=]\s*\S+",
        r"(?i)\b(one[- ]time password|otp)\s*[:=]\s*\S+",
    ]
    combined = issue_summary + "\n" + description
    if any(re.search(pattern, combined) for pattern in sensitive_patterns):
        return {"success": False, "error": "Remove passwords or one-time codes before creating a ticket."}

    initialize_database()
    ticket_id = "INC-" + uuid.uuid4().hex[:8].upper()
    timestamp = _now()
    with closing(_connect()) as conn, conn:
        conn.execute("""
            INSERT INTO support_tickets
            (ticket_id, issue_summary, description, category, priority,
             affected_service, location, status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'Open', ?, ?)
        """, (
            ticket_id, issue_summary.strip(), description.strip(), category,
            priority, affected_service, location.strip(), timestamp, timestamp
        ))
    return {
        "success": True,
        "data_source": "local_sqlite_demo",
        "ticket": {
            "ticket_id": ticket_id,
            "status": "Open",
            "issue_summary": issue_summary.strip(),
            "category": category,
            "priority": priority,
            "affected_service": affected_service,
            "created_at": timestamp,
        },
    }

def get_ticket_status(ticket_id: str) -> dict:
    if not isinstance(ticket_id, str) or not ticket_id.strip():
        return {"success": False, "error": "ticket_id is required."}
    initialize_database()
    with closing(_connect()) as conn, conn:
        row = conn.execute(
            "SELECT * FROM support_tickets WHERE ticket_id = ?",
            (ticket_id.strip().upper(),)
        ).fetchone()
    if row is None:
        return {"success": False, "error": "Ticket not found in the local demo database."}
    return {
        "success": True,
        "data_source": "local_sqlite_demo",
        "ticket": dict(row),
    }

initialize_database()
