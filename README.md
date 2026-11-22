# Azure AI Foundry Enterprise Support Agent

<p align="center">
  <strong>Building Enterprise IT Support with Agentic AI, Multi-Agent Orchestration and Intelligent Automation</strong><br>
  An AI-powered enterprise support solution connecting Azure AI Foundry, Microsoft Copilot Studio, MCP tools, Power Automate and Dataverse.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Azure%20AI%20Foundry-0078D4?style=for-the-badge" alt="Azure AI Foundry">
  <img src="https://img.shields.io/badge/Architecture-Agentic%20AI-7C3AED?style=for-the-badge" alt="Agentic AI">
  <img src="https://img.shields.io/badge/Orchestration-Copilot%20Studio-0F766E?style=for-the-badge" alt="Copilot Studio">
  <img src="https://img.shields.io/badge/Integration-MCP-2563EB?style=for-the-badge" alt="MCP">
  <img src="https://img.shields.io/badge/Automation-Power%20Automate-15803D?style=for-the-badge" alt="Power Automate">
  <img src="https://img.shields.io/badge/Data-Dataverse-334155?style=for-the-badge" alt="Dataverse">
</p>

---

## Overview

**Azure AI Foundry Enterprise Support Agent** is an enterprise IT support automation project demonstrating how AI agents, external tools, knowledge sources and business workflows can work together to resolve employee support requests.

Traditional IT support often involves employees searching documentation, contacting support teams, waiting for responses and manually tracking service requests.

This project explores an agentic approach where an AI assistant can understand an employee's problem, coordinate with a specialist AI agent, retrieve information from connected tools, guide the employee through safe troubleshooting and initiate support workflows when necessary.

The solution combines:

- **Microsoft Copilot Studio** for conversational interaction and agent orchestration.
- **Azure AI Foundry** for specialist AI agent development and grounded troubleshooting.
- **Model Context Protocol (MCP)** for connecting agents to external tools.
- **Power Automate** for business workflow automation.
- **Microsoft Dataverse** for structured support ticket management.
- **Microsoft Azure** for cloud-based agent and service integration.

The objective is to demonstrate how generative AI can move beyond answering questions and participate in controlled, tool-driven enterprise workflows.

### Current implementation status

The core conversational and ticket-creation workflow has been implemented and tested.

| Component | Current status |
|---|---|
| Azure AI Foundry project | Created |
| Foundry specialist agent | Created and tested |
| Azure AI Search knowledge base | Configured and tested |
| Copilot Studio agent | Created |
| Copilot Studio–Foundry connection | Connected and tested |
| Dataverse IT Support Ticket table | Created |
| Power Automate ticket creation flow | Implemented and tested |
| Copilot Studio ticket-creation integration | Tested end to end |
| Python MCP server | Implemented and locally tested |
| Remote MCP hosting | Not implemented |
| Cloud agent–MCP connection | Not implemented |

**Important:** The MCP implementation currently runs locally and uses synthetic service data and SQLite ticket storage. It is not yet connected to the Dataverse ticket table or the cloud-based agent.

## Problem Statement

Enterprise IT support teams regularly receive repetitive requests involving:

- VPN connection failures.
- Network and internet connectivity.
- Email configuration and access.
- Application access problems.
- IT service availability.
- Existing support ticket enquiries.
- New incident and support ticket creation.

A conventional chatbot can provide general troubleshooting instructions, but it may not have access to live service information or the ability to execute business processes.

This project addresses that gap by connecting conversational AI with specialist reasoning, external tools and workflow automation.

## Solution

The system uses a central Copilot Studio agent as the employee-facing interface.

The agent coordinates with an Azure AI Foundry specialist agent for technical troubleshooting, and uses Power Automate to create support tickets in Dataverse.

The separately implemented MCP server provides additional tools for service-status lookup and local ticket operations. Remote hosting and cloud-agent integration remain future work.

The intended workflow is:

**Understand → Analyse → Retrieve → Troubleshoot → Act → Confirm**

The agent should use connected tools for information that requires live retrieval and should never invent service status, ticket details or completed actions.

---

# Architecture

## High-Level Architecture

```text
                         EMPLOYEE
                            |
                            v
                  MICROSOFT COPILOT STUDIO
                  Enterprise IT Support Agent
                            |
                     Agent Orchestration
                            |
             +--------------+---------------+
             |              |               |
             v              v               v
        AZURE AI        POWER AUTOMATE   FUTURE MCP
        FOUNDRY              |           CONNECTION
             |              |               |
             v              v               |
        Specialist       Ticket Creation    |
        Troubleshooting  Workflow            |
        Agent                |               |
             |               v               |
             |           DATAVERSE           |
             |        IT Support Tickets     |
             |                               |
             +-------------------------------+
                                             |
                                    PYTHON MCP SERVER
                                             |
                                  +----------+----------+
                                  |          |          |
                                  v          v          v
                               Service    Ticket     Ticket
                               Status     Lookup    Creation
                               Tool       Tool       Tool
```

The diagram represents the overall design. The MCP server is currently a separate local component and is not connected to the cloud agent.

## Project Screenshots

### Azure AI Foundry & Azure Resources

**Foundry Specialist Agent**

<p align="center">
  <img src="https://github.com/user-attachments/assets/ace0525c-23e1-4ebb-82b7-5577eafddc04" width="85%" alt="Foundry Specialist Agent">
</p>

**Azure Resource Group**

<p align="center">
  <img src="https://github.com/user-attachments/assets/946c8c8d-6807-41a9-aeec-bb9d80ec13fa" width="85%" alt="Azure Resource Group">
</p>

**Foundry IQ**

<p align="center">
  <img src="https://github.com/user-attachments/assets/764c4e10-179f-43e5-ad72-650db40d75c3" width="85%" alt="Foundry IQ">
</p>

**Azure AI Search**

<p align="center">
  <img src="https://github.com/user-attachments/assets/c418e2cf-b017-45f4-a3d3-51ba01a83dae" width="85%" alt="Azure AI Search">
</p>

**Azure Storage Lake**

<p align="center">
  <img src="https://github.com/user-attachments/assets/5b37c6c3-d545-41f8-a8f2-05ed41d2e53c" width="85%" alt="Azure Storage Lake">
</p>

### Copilot Studio Integration

**Support Agent**

<p align="center">
  <img src="https://github.com/user-attachments/assets/ef6d4238-00a0-4fd2-9779-6328fb847fc8" width="85%" alt="Copilot Studio Support Agent">
</p>

**Foundry Agent Delegation**

<p align="center">
  <img src="https://github.com/user-attachments/assets/81e3e772-9e38-4464-b067-ecda6f21487c" width="85%" alt="Copilot Studio Calling Foundry Agent">
</p>

**Power Automate Integration**

<p align="center">
  <img src="https://github.com/user-attachments/assets/6b89dfb3-f130-45dc-9df7-9fbabcc8d295" width="85%" alt="Copilot Studio Calling Power Automate">
</p>

### Local MCP Server & Tool Testing

**MCP Server — Local Execution**

<p align="center">
  <img src="https://github.com/user-attachments/assets/7fb2460d-e4ad-4198-b8a9-c39160db67bb" width="75%" alt="Local MCP Server">
</p>

**Service Status Tool**

<p align="center">
  <img src="https://github.com/user-attachments/assets/fb8dc7d5-78c4-41bf-bf9e-9a45a43d23de" width="75%" alt="MCP Service Status Tool">
</p>



**Create Support Ticket Tool**

<p align="center">
  <img src="https://github.com/user-attachments/assets/a4ace8de-bd20-415e-98ac-1255421a3e22" width="75%" alt="MCP Create Support Ticket Tool">
</p>

**Get Ticket Status Tool**

<p align="center">
  <img src="https://github.com/user-attachments/assets/a127a1ca-fa85-4352-a102-eea97e520d6e" width="75%" alt="MCP Get Ticket Status Tool">
</p>


### Component Responsibilities

| Component | Responsibility |
|---|---|
| Copilot Studio | Employee-facing conversation and agent orchestration |
| Azure AI Foundry | Specialist troubleshooting and AI reasoning |
| MCP Server | Standardized access to external tools |
| MCP Service Tool | Retrieves IT service availability |
| MCP Ticket Tool | Retrieves existing ticket information |
| Power Automate | Executes ticket creation workflows |
| Dataverse | Stores structured support ticket records |
| Azure | Hosts and secures supporting services |

The architecture describes the intended integration design. Actual connections and permissions must be configured and tested in the deployed environment.

---

# Core Functionalities

## 1. Conversational Enterprise IT Support

The Copilot Studio agent acts as the primary interface for employees.

### Supported scenarios

- VPN connectivity issues.
- Network and internet access.
- Email access and configuration.
- Application access problems.
- General IT troubleshooting.
- Existing support ticket enquiries.
- New IT support requests.

### Agent capabilities

- Understand employee questions using natural language.
- Identify the type of technical issue.
- Ask relevant follow-up questions.
- Maintain conversation context.
- Provide structured troubleshooting instructions.
- Route requests to the appropriate connected agent or tool.
- Explain when administrator intervention is required.
- Escalate unresolved issues through the support workflow.

The agent should ask only for information necessary to understand and process a support request.

## 2. Azure AI Foundry Specialist Agent

Azure AI Foundry provides the specialist troubleshooting agent.

The agent is designed to use approved IT support knowledge and instructions to provide consistent technical guidance.

### Implemented configuration

- Foundry project: `RG_KiranAgent-project`
- Specialist agent: `EnterpriseSupportAgent`
- Model: `gpt-5-mini`
- Knowledge source: Azure AI Search-backed support knowledge base.
- Knowledge document: `Enterprise Connectivity Support Handbook`.
- Search service: `kiranagentfoundrysearch`.

### Intended capabilities

- Analyse common IT connectivity problems.
- Understand VPN, network, email and application access issues.
- Retrieve relevant troubleshooting information from its configured knowledge.
- Recommend safe troubleshooting steps.
- Identify restricted operations.
- Recognize when a problem requires IT administrator intervention.
- Return troubleshooting guidance to the main agent.

### Knowledge-grounded troubleshooting

The specialist agent should prioritize approved support documentation rather than relying only on general model knowledge.

Its responses should distinguish between:

- Information supported by the handbook.
- Information that requires further investigation.
- Actions that require administrator approval.
- Situations that should be escalated.

### Knowledge base implementation

The Azure AI Search knowledge base was configured and tested with the synthetic Enterprise Connectivity Support Handbook.

The Foundry agent has been tested with connectivity scenarios, including:

- Laptop connected to Wi-Fi but unable to access the internet.
- Whether the issue affects one device or multiple devices.
- Requesting network adapter details using `ipconfig /all`.
- Explaining the significance of an APIPA address such as `169.254.x.x`.
- Refusing to invent an approved corporate DNS address.

## 3. Multi-Agent Collaboration

The project demonstrates collaboration between a conversational agent and a specialist AI agent.

### Agent responsibilities

| Agent | Responsibility |
|---|---|
| Enterprise IT Support Agent | Main employee interaction, request understanding and orchestration |
| Technical Support Specialist | Technical troubleshooting using Azure AI Foundry |

### Example interaction

**Employee:**

"My company VPN is not connecting."

**Copilot Studio Agent:**

Understands the problem and gathers relevant details.

**Foundry Specialist Agent:**

Analyses the issue using the approved troubleshooting knowledge and returns recommended steps.

**Copilot Studio Agent:**

Presents the instructions to the employee and determines whether further assistance is needed.

This separation keeps employee interaction and specialist troubleshooting responsibilities distinct.

### Implemented delegation

The Copilot Studio agent has a connected Foundry specialist agent.

Technical requests involving networking, Wi-Fi, LAN, DHCP, IP addressing, DNS, VPN and Windows network diagnostics are delegated to the specialist agent.

The delegation was tested through Copilot Studio.

## 4. Model Context Protocol (MCP) Integration

The project uses MCP to expose external capabilities to an AI agent through standardized tool interfaces.

A Python MCP server has been implemented using the FastMCP SDK.

### Implemented MCP tools

The current implementation exposes three tools.

### Tool 1: `check_service_status`

**Purpose:** Retrieve service availability information from the local demonstration dataset.

Example input:

```json
{
  "service_name": "VPN"
}
```

The tool reads service information from:

`mcp-server/data/services.json`

Expected capabilities:

- Check VPN availability.
- Check email service availability.
- Check network service availability.
- Return structured service information.
- Handle unknown services safely.

**Implementation limitation:** The current service information is synthetic. It is not connected to a live enterprise monitoring platform.

### Tool 2: `get_ticket_status`

**Purpose:** Retrieve the status of an existing ticket from the local SQLite database.

Example input:

```json
{
  "ticket_id": "INC-1001"
}
```

Expected capabilities:

- Retrieve locally stored ticket details.
- Return ticket status.
- Display available ticket information.
- Handle invalid or missing ticket references.

**Implementation limitation:** The current implementation uses local SQLite. It does not retrieve records from the Dataverse `IT Support Ticket` table.

Ticket access must be validated using an appropriate identity and authorization mechanism before enterprise deployment.

### Tool 3: `create_support_ticket`

**Purpose:** Create a support ticket in the local SQLite database.

The tool accepts:

- Issue summary.
- Description.
- Category.
- Priority.
- Affected service.
- Location.

Expected capabilities:

- Validate required input.
- Reject invalid priority values.
- Reject password-like content.
- Generate a ticket reference.
- Store the ticket in SQLite.
- Return the created ticket information.

**Implementation limitation:** This is a separate local ticket store. The cloud ticket-creation workflow uses Power Automate and Dataverse instead.

### MCP server implementation

Repository location:

`mcp-server/`

Main files:

| File | Responsibility |
|---|---|
| `server.py` | FastMCP server and tool registration |
| `support_data.py` | Support data and ticket operations |
| `data/services.json` | Synthetic service information |
| `tests/test_support_data.py` | Automated support-data tests |
| `requirements.txt` | Python dependencies |
| `README.md` | MCP setup and usage documentation |

### MCP transports tested

- STDIO transport.
- Streamable HTTP transport.

Local Streamable HTTP endpoint:

`http://127.0.0.1:8000/mcp`

The server was tested locally using MCP Inspector.

### Automated test results

The following test cases passed:

| Test | Result |
|---|---|
| Create and retrieve a ticket | Passed |
| Reject invalid priority | Passed |
| Return known synthetic service data | Passed |
| Reject password-like content | Passed |
| Reject unknown service | Passed |

**MCP integration status:** The MCP server is implemented and locally tested. It has not yet been remotely hosted or connected to the cloud-based Copilot Studio agent.

### MCP integration objectives

- Implement an MCP server.
- Expose tools using supported MCP protocols.
- Connect the server to the agent through a supported integration.
- Validate tool inputs.
- Handle errors and unavailable services.
- Return structured results.
- Protect endpoints using appropriate authentication.

## 5. Power Automate — Automated Ticket Creation

Power Automate handles the business workflow for creating IT support tickets.

### Implemented flow: `Create_IT_Support_Ticket`

**Trigger:** When an agent calls the flow.

### Actual input parameters

| Parameter | Internal name | Description |
|---|---|---|
| Ticket Subject | `text` | Short issue title |
| Description | `text_1` | Description of the technical problem |
| Category | `text_2` | Support category |
| Priority | `text_3` | Ticket priority |
| Affected Service | `text_4` | Impacted service or application |
| Location | `text_5` | Employee location |

### Supported categories

- Network
- VPN
- Email
- Application
- Hardware
- Software
- Access
- Other

### Supported priorities

- Low
- Medium
- High
- Critical

### Implemented workflow

1. Receive the support request details from Copilot Studio.
2. Initialize request category and priority variables.
3. Map category and priority text values to Dataverse choice values.
4. Create a support ticket row in Dataverse.
5. Generate a ticket reference using the `INC-` prefix.
6. Return the creation result, reference and status to Copilot Studio.
7. Display the actual ticket reference and status to the employee.

### Ticket reference generation

The flow generates a reference using a GUID-based expression:

```powerautomate
concat('INC-', toUpper(substring(replace(guid(),'-',''),0,8)))
```

### Actual workflow output

The flow returns the creation result, ticket reference, status and confirmation message.

Example response structure:

```json
{
  "success": true,
  "ticket_reference": "INC-99BA23AF",
  "status": "New",
  "message": "Your support ticket has been created successfully."
}
```

The reference above is an example from a successful project test, not a fixed value.

### End-to-end validation

The following scenario was successfully tested through Copilot Studio:

**Employee issue:**

"My laptop connects to Wi-Fi, but I cannot access the internet. I want to create an IT support ticket."

The agent:

1. Delegated technical troubleshooting to the Foundry specialist.
2. Gathered the ticket information.
3. Asked for the priority.
4. Collected the employee's location.
5. Summarized the ticket details.
6. Asked the employee to confirm.
7. Invoked the Power Automate flow after confirmation.
8. Created the Dataverse record.
9. Returned the generated ticket reference and status.

Successful response:

> Your support ticket has been created successfully. The ticket reference is INC-99BA23AF, and its current status is New.

The Dataverse record was verified after the successful execution.

The agent should obtain employee confirmation before submitting a new ticket.

## 6. Microsoft Dataverse — Support Ticket Management

Dataverse provides structured storage for IT support requests.

### Implemented table: `IT Support Ticket`

The table was created in the `Enterprise Support Intelligence` solution.

### Actual table columns

| Column | Data type | Purpose |
|---|---|---|
| Ticket Subject | Single line of text | Primary ticket title |
| Ticket Reference | Single line of text | Generated employee-facing reference |
| Description | Multiple lines of text | Issue details |
| Category | Choice | Support category |
| Priority | Choice | Ticket priority |
| Affected Service | Single line of text | Impacted service |
| Location | Single line of text | Employee location |
| Status | Choice | Ticket lifecycle status |

### Category choices

- Network
- VPN
- Email
- Application
- Hardware
- Software
- Access
- Other

### Priority choices

- Low
- Medium
- High
- Critical

### Status choices

- New
- In Progress
- Resolved
- Closed

### Ticket lifecycle

```text
        New
         |
         v
    In Progress
         |
         v
      Resolved
         |
         v
       Closed
```

The initial demonstration uses a simplified ticket lifecycle. Production implementations should also consider reassignment, cancellation, reopening and audit history.

### Data management objectives

- Store ticket information in Dataverse.
- Retrieve tickets through approved tools.
- Maintain ticket status and priority.
- Apply appropriate access controls.
- Return only authorized ticket information.

### Power Platform solution

The following components were added to the `Enterprise Support Intelligence` solution:

- Copilot Studio agent components.
- `IT Support Ticket` Dataverse table.
- `Create_IT_Support_Ticket` Power Automate flow.

The solution was exported and unpacked locally for version control.

Repository location:

`power-platform/EnterpriseSupportIntelligence/`

The exported solution contains its metadata and component folders, including available assets, workflows, bot components and bot definitions.

The exported solution does not package the Azure AI Foundry project, model deployment, Azure AI Search service or the separately maintained MCP server.

---

# End-to-End Use Cases

## Use Case 1: VPN Troubleshooting

**Employee:**

"My VPN is not connecting."

Expected workflow:

1. Copilot Studio understands the issue.
2. The Foundry specialist agent provides knowledge-grounded troubleshooting.
3. The agent asks relevant questions.
4. The agent checks service information if an appropriate connected tool is available.
5. The agent combines the results and provides troubleshooting instructions.
6. If the problem remains unresolved, the agent offers ticket creation.

## Use Case 2: Check Service Availability

**Employee:**

"Is the VPN service currently available?"

Expected workflow:

1. Identify the requested service.
2. Invoke `check_service_status` when the MCP tool is connected.
3. Retrieve the tool response.
4. Present the returned service status.
5. Explain if the status cannot be verified.

The current local tool returns synthetic demonstration data. It does not provide live production service monitoring.

## Use Case 3: Track an Existing Ticket

**Employee:**

"What is happening with ticket INC-1001?"

Expected workflow:

1. Extract the ticket reference.
2. Invoke `get_ticket_status` when the appropriate tool is connected.
3. Validate that the employee is authorized to view the ticket.
4. Retrieve the ticket information.
5. Return the status and relevant details.

The current MCP implementation looks up tickets in local SQLite. Dataverse ticket lookup through MCP is future work.

## Use Case 4: Create a New Support Ticket

**Employee:**

"My email access is still not working. Raise a ticket."

Implemented workflow:

1. Understand the unresolved issue.
2. Gather required ticket details.
3. Determine the appropriate category and priority.
4. Confirm the details with the employee.
5. Invoke the Power Automate flow.
6. Create the Dataverse record.
7. Return the actual ticket reference and status.

This workflow has been successfully tested end to end.

## Use Case 5: Restricted Technical Operation

**Employee:**

"Should I restart the company firewall?"

Expected behavior:

1. Identify that the requested action affects managed infrastructure.
2. Check the approved support guidance.
3. Refuse to recommend unauthorized changes.
4. Explain that network administrator approval is required.
5. Offer escalation through the support process.

---

# Responsible AI and Enterprise Safety

The agent follows explicit IT support safety restrictions.

### Restricted operations

- Never request passwords, one-time passcodes, full payment details or unnecessary personal information.
- Never instruct employees to disconnect provider handoff cables or fiber connectors.
- Never reboot a managed router, firewall, modem, ONT, switch or access point without authorization.
- Never assign a static IP unless the network administrator provides the approved configuration.
- Never replace corporate DNS servers.
- Never recommend infrastructure changes without appropriate authorization.

### Additional safeguards

- Use trusted knowledge for technical guidance.
- Validate tool inputs before execution.
- Avoid inventing service availability or ticket information.
- Require confirmation before creating support tickets.
- Apply authorization checks to employee-specific records.
- Handle tool failures without pretending an action succeeded.
- Escalate situations that require administrator intervention.

---

# Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Conversational AI | Microsoft Copilot Studio | Employee-facing agent |
| AI Agent Platform | Azure AI Foundry | Specialist AI agent |
| Agent Architecture | Multi-Agent Orchestration | Agent collaboration |
| Knowledge Retrieval | Azure AI Search | Support documentation retrieval |
| Tool Integration | Model Context Protocol | External tool access |
| Backend | Python | MCP server implementation |
| MCP Framework | FastMCP | MCP server and tool implementation |
| Local Persistence | SQLite | Local MCP ticket storage |
| Workflow Automation | Microsoft Power Automate | Ticket creation |
| Data Platform | Microsoft Dataverse | Support ticket storage |
| Cloud Platform | Microsoft Azure | Cloud services and identity |
| Identity and Access | Microsoft Entra ID / Azure RBAC | Authentication and authorization |
| Monitoring | Application Insights / Azure monitoring | Operational observability, where configured |

---

# Repository Structure

```text
Azure-AI-Foundry-Enterprise-Support-Agent/
│
├── README.md
│
├── mcp-server/
│   ├── data/
│   │   └── services.json
│   ├── tests/
│   │   └── test_support_data.py
│   ├── README.md
│   ├── requirements.txt
│   ├── server.py
│   └── support_data.py
│
└── power-platform/
    └── EnterpriseSupportIntelligence/
        ├── Assets/
        ├── Workflows/
        ├── botcomponents/
        ├── bots/
        ├── [Content_Types].xml
        ├── customizations.xml
        ├── solution.xml
        └── README.md
```

The repository currently contains the MCP server implementation and the unpacked Power Platform solution. Azure AI Foundry configuration and screenshots are maintained separately in the Azure environment and GitHub attachments.

---

# Getting Started

## Prerequisites

- Microsoft Azure subscription.
- Access to Azure AI Foundry.
- Microsoft Copilot Studio access.
- Power Automate access.
- Microsoft Dataverse environment.
- Python 3.11 or later.
- Git.
- Visual Studio Code or another development environment.

Some Microsoft services require appropriate licensing, environment permissions and tenant configuration.

## 1. Clone the Repository

```bash
git clone https://github.com/Keyrun1227/Azure-AI-Foundry-Enterprise-Support-Agent.git

cd Azure-AI-Foundry-Enterprise-Support-Agent
```

## 2. Configure the Azure AI Foundry Agent

1. Open the Azure AI Foundry portal.
2. Create or open the relevant Foundry project.
3. Create the specialist IT troubleshooting agent.
4. Configure the agent instructions.
5. Add the approved IT support handbook as knowledge.
6. Test the agent using representative support scenarios.
7. Configure the required identity and access permissions.

The project implementation uses `RG_KiranAgent-project` and the specialist agent `EnterpriseSupportAgent`.

## 3. Configure Copilot Studio

1. Create or open the Enterprise IT Support Agent.
2. Configure the main conversational instructions.
3. Connect the Azure AI Foundry specialist agent through the supported connected-agent integration.
4. Configure the appropriate orchestration behavior.
5. Connect the Power Automate ticket creation action.
6. Validate the complete conversation flow.

The existing implementation connects Copilot Studio to the Foundry specialist agent and the ticket-creation flow.

MCP remote integration is not yet configured.

## 4. Run the MCP Server

Navigate to the MCP server directory:

```bash
cd mcp-server
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bat
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the automated tests:

```bash
python -m pytest -q
```

Start the server using the configured transport.

For Streamable HTTP on Windows CMD:

```bat
set MCP_TRANSPORT=streamable-http
python server.py
```

The local endpoint is:

```text
http://127.0.0.1:8000/mcp
```

The server also supports STDIO transport.

The local MCP implementation is intended for development and validation. It is not a production deployment.

## 5. Configure Power Automate

The `Create_IT_Support_Ticket` flow is included in the exported Power Platform solution.

1. Open Power Automate.
2. Import or open the `Enterprise Support Intelligence` solution.
3. Review the flow and its trigger inputs.
4. Configure the required Dataverse connection.
5. Verify the category and priority mappings.
6. Confirm that the flow creates a Dataverse record.
7. Confirm that the flow returns the ticket reference and status.
8. Connect or verify the flow in Copilot Studio.

## 6. Configure Dataverse

The `IT Support Ticket` table is included in the exported solution.

1. Import the solution into the intended environment.
2. Verify the table and its columns.
3. Verify the category, priority and status choices.
4. Configure table permissions and security roles.
5. Verify the connection used by Power Automate.
6. Test ticket creation in a non-production environment.

---

# Testing and Evaluation

Testing covers individual agent behavior, tool execution and end-to-end workflows.

### Agent Evaluation

- Correct identification of employee issues.
- Relevance of troubleshooting guidance.
- Use of approved knowledge.
- Appropriate escalation behavior.
- Compliance with safety restrictions.
- Handling of incomplete information.
- Resistance to unsupported or fabricated responses.

### MCP Tool Testing

- Valid service name.
- Unknown service name.
- Successful status retrieval.
- Invalid ticket reference.
- Existing ticket retrieval.
- Password-like content rejection.
- MCP connection failure.
- Invalid tool input.

### Power Automate Testing

- Valid ticket creation.
- Missing required information.
- Invalid category or priority.
- Dataverse connection failure.
- Workflow execution failure.
- Correct ticket reference returned to the agent.

### End-to-End Testing

| Scenario | Expected result | Implementation status |
|---|---|---|
| VPN troubleshooting | Grounded troubleshooting guidance | Tested |
| Wi-Fi without internet | Specialist troubleshooting | Tested |
| APIPA address explanation | Knowledge-grounded response | Tested |
| Service availability lookup | Service status returned by MCP | Local tool tested |
| Ticket enquiry | Ticket details returned from the relevant store | Local tool tested |
| New support request | Dataverse ticket created | Tested end to end |
| Restricted operation | Safe refusal and escalation | Safety instructions configured |
| MCP unavailable | Clear tool failure response | Requires hosted integration testing |
| Power Automate failure | No false ticket creation confirmation | Flow error handling should be validated further |

### Automated MCP Test Results

The local MCP support-data test suite contains five tests:

- Ticket creation and retrieval.
- Invalid priority rejection.
- Known synthetic service lookup.
- Password-like content rejection.
- Unknown service rejection.

All five tests passed during local validation.

Evaluation results should be recorded with the corresponding test cases and execution evidence.

---

# Security and Configuration

Never commit credentials or secrets to the repository.

Use environment variables or an approved secrets-management service for sensitive configuration.

Example `.env.example`:

```env
AZURE_AI_PROJECT_ENDPOINT=
AZURE_AI_AGENT_ID=

MCP_SERVER_HOST=
MCP_SERVER_PORT=

DATAVERSE_URL=
AZURE_TENANT_ID=
AZURE_CLIENT_ID=

APPLICATIONINSIGHTS_CONNECTION_STRING=
```

These are illustrative configuration names. Actual environment variables must match the implemented application.

### Security requirements

- Use managed identities or approved authentication where supported.
- Apply least-privilege access.
- Validate all incoming tool parameters.
- Protect MCP endpoints.
- Restrict access to employee-specific tickets.
- Never expose secrets in logs or responses.
- Maintain appropriate audit records.
- Use separate development and production configurations.

### Current MCP security limitations

The local MCP server does not yet provide production-grade authentication or authorization.

It binds to localhost for local testing. Do not expose it directly to the public internet.

Before remote hosting, implement appropriate authentication, authorization, transport security and access controls.

---

# Monitoring and Observability

The solution should support operational monitoring across the agent and workflow components.

Areas to monitor include:

- Agent execution and response failures.
- Tool invocation success and failure.
- MCP connectivity.
- Power Automate execution history.
- Dataverse operation failures.
- Latency across connected components.
- Authorization failures.
- Escalation frequency.

Application Insights and Azure monitoring can be used where telemetry is configured and available.

---

# Development Roadmap

The following roadmap distinguishes completed implementation from remaining integration work.

### Phase 1 — AI Agent Foundation

- [x] Create Azure AI Foundry project.
- [x] Build the specialist IT troubleshooting agent.
- [x] Configure the agent instructions and safety restrictions.
- [x] Save and test the Foundry agent.
- [x] Create the Copilot Studio Enterprise IT Support Agent.
- [x] Configure its conversational instructions.
- [x] Connect the Foundry specialist agent to Copilot Studio.
- [x] Configure and test Azure AI Search knowledge retrieval.
- [x] Test specialist delegation through Copilot Studio.

### Phase 2 — MCP Server Development

- [x] Implement the Python MCP server.
- [x] Implement `check_service_status`.
- [x] Implement `get_ticket_status`.
- [x] Implement `create_support_ticket`.
- [x] Configure STDIO transport.
- [x] Configure Streamable HTTP transport.
- [x] Test MCP tools using MCP Inspector.
- [x] Add automated support-data tests.
- [x] Validate input handling and error cases.
- [ ] Deploy MCP server to an approved remote hosting environment.
- [ ] Implement production-grade authentication and authorization.
- [ ] Connect MCP to the cloud-based agent.
- [ ] Replace synthetic service information with an approved monitoring integration.
- [ ] Integrate MCP ticket operations with Dataverse.

### Phase 3 — Business Workflow Automation

- [x] Create the Dataverse IT Support Ticket table.
- [x] Configure ticket columns and choice values.
- [x] Build the Power Automate ticket creation flow.
- [x] Configure request inputs and category/priority mappings.
- [x] Generate the ticket reference.
- [x] Return the ticket reference and creation status.
- [x] Connect the workflow to Copilot Studio.
- [x] Validate ticket creation and Dataverse record creation.
- [x] Export the Power Platform solution.

### Phase 4 — End-to-End Validation

- [x] Test VPN troubleshooting.
- [x] Test Wi-Fi connectivity troubleshooting.
- [x] Test knowledge-grounded APIPA explanation.
- [x] Test Foundry delegation.
- [x] Test local MCP service lookup.
- [x] Test local MCP ticket operations.
- [x] Test support ticket creation through Copilot Studio.
- [x] Verify the created Dataverse record.
- [ ] Test remote MCP integration.
- [ ] Test authorization across employee-specific tickets.
- [ ] Run broader agent evaluations.
- [ ] Complete production deployment and documentation.

---

# Project Scope and Current Status

This repository documents a practical implementation of an enterprise agentic AI support solution.

The following capabilities have been implemented:

- Azure AI Foundry project and specialist troubleshooting agent.
- Azure AI Search-backed support knowledge.
- Copilot Studio conversational support agent.
- Connected-agent delegation from Copilot Studio to Foundry.
- Dataverse IT Support Ticket table.
- Power Automate ticket-creation workflow.
- Copilot Studio integration with the ticket-creation flow.
- End-to-end ticket creation and Dataverse record verification.
- Python MCP server with three tools.
- Local MCP testing using STDIO and Streamable HTTP.
- Automated MCP support-data tests.

The following capabilities remain future work:

- Remote hosting of the MCP server.
- Secure remote MCP connectivity.
- Connecting MCP tools to the cloud-based agent.
- Integrating MCP ticket operations with Dataverse.
- Replacing synthetic service data with live monitoring information.

The project separates working integrations from planned capabilities so that the implementation status is clear.

---

# Learning and Engineering Concepts Demonstrated

This project brings together several important enterprise AI engineering concepts:

- Generative AI agent development.
- Agent orchestration and collaboration.
- Knowledge-grounded responses.
- MCP-based tool integration.
- Structured tool inputs and outputs.
- API and workflow integration.
- Business process automation.
- Enterprise data management.
- Identity and access management.
- Responsible AI and safety guardrails.
- Agent evaluation and observability.
- End-to-end integration testing.
- Dataverse solution management and Power Platform ALM.

---

# Author

**Sai Kiran**

Dynamics 365 and Power Platform Developer | Azure AI Foundry | Copilot Studio | Agentic AI | MCP | Power Automate

GitHub: [Keyrun1227](https://github.com/Keyrun1227)

---

<p align="center">
  <strong>Azure AI Foundry Enterprise Support Agent</strong><br>
  <em>Connecting AI reasoning with enterprise tools and real business workflows.</em>
</p>
