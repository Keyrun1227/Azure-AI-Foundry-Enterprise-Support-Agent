import os
from mcp.server.fastmcp import FastMCP

from support_data import (
    check_service_status as check_service_status_data,
    create_support_ticket as create_support_ticket_data,
    get_ticket_status as get_ticket_status_data,
)

mcp = FastMCP(
    "Enterprise Support MCP Server",
    instructions=(
        "Tools for a synthetic enterprise IT support demonstration. "
        "Service status and ticket records are local demo data, not live corporate systems."
    ),
    host=os.getenv("MCP_HOST", "127.0.0.1"),
    port=int(os.getenv("MCP_PORT", "8000")),
)

@mcp.tool()
def check_service_status(service_name: str) -> dict:
    """Check the demo status of a supported IT service such as VPN, Wi-Fi, DNS, or Email."""
    return check_service_status_data(service_name)

@mcp.tool()
def get_ticket_status(ticket_id: str) -> dict:
    """Retrieve the current status and details of a support ticket by its reference."""
    return get_ticket_status_data(ticket_id)

@mcp.tool()
def create_support_ticket(
    issue_summary: str,
    description: str,
    category: str,
    priority: str,
    affected_service: str,
    location: str = "Not provided",
) -> dict:
    """Create a support ticket in the local SQLite demo database."""
    return create_support_ticket_data(
        issue_summary=issue_summary,
        description=description,
        category=category,
        priority=priority,
        affected_service=affected_service,
        location=location,
    )

if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    mcp.run(transport=transport)