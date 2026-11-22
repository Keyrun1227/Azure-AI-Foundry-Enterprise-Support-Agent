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

The agent coordinates with an Azure AI Foundry specialist agent for technical troubleshooting, invokes MCP tools to retrieve operational information, and uses Power Automate to create support tickets in Dataverse.

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
       AZURE AI         MCP SERVER      POWER AUTOMATE
       FOUNDRY              |               |
             |              |               |
             v         +----+------+        v
       Specialist      |           |    Ticket Creation
       Troubleshooting |           |       Workflow
       Agent            v           v        |
                    Service     Ticket      v
                    Status      Status   DATAVERSE
                    Tool        Tool      Support Tickets
```

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

### Intended capabilities

- Analyse common IT connectivity problems.
- Understand VPN, network, email and application access issues.
- Retrieve relevant troubleshooting information from its configured knowledge.
- Recommend safe troubleshooting steps.
- Identify restricted operations.
- Recognize when a problem requires IT administrator intervention.
- Return structured troubleshooting guidance to the main agent.

### Knowledge-grounded troubleshooting

The specialist agent should prioritize approved support documentation rather than relying only on general model knowledge.

Its responses should distinguish between:

- Information supported by the handbook.
- Information that requires further investigation.
- Actions that require administrator approval.
- Situations that should be escalated.

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

## 4. Model Context Protocol (MCP) Integration

The project uses MCP to expose external capabilities to the AI agent through standardized tool interfaces.

The MCP server is designed to provide the following tools.

### Tool 1: get_service_status

**Purpose:** Retrieve the current availability of an IT service.

Example input:

```json
{
  "service_name": "VPN"
}
```

Example response:

```json
{
  "service": "VPN",
  "status": "Operational",
  "message": "VPN service is currently operational."
}
```

Expected capabilities:

- Check VPN availability.
- Check email service availability.
- Check network service availability.
- Return structured service information.
- Handle unknown services and unavailable status sources safely.

The initial implementation may use controlled demonstration data. It must not represent simulated values as actual production monitoring data.

### Tool 2: get_ticket_status

**Purpose:** Retrieve the current status of an existing IT support ticket.

Example input:

```json
{
  "ticket_id": "INC-1001"
}
```

Example response:

```json
{
  "ticket_id": "INC-1001",
  "status": "In Progress",
  "priority": "High",
  "category": "VPN",
  "message": "Your support request is currently being investigated."
}
```

Expected capabilities:

- Retrieve ticket details.
- Return ticket status.
- Display ticket priority and category.
- Handle invalid or missing ticket references.
- Avoid exposing tickets to unauthorized employees.

Ticket access must be validated using an appropriate identity and authorization mechanism.

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

### Flow: Create_IT_Support_Ticket

**Trigger:** Agent invokes the configured Power Automate action.

### Expected input parameters

| Parameter | Description |
|---|---|
| Employee Name | Name of the employee |
| Employee Email | Employee contact address |
| Issue Description | Description of the technical problem |
| Category | VPN, Network, Email or Application |
| Priority | Low, Medium, High or Critical |

### Workflow

1. Receive the support request details.
2. Validate required inputs.
3. Check the request information.
4. Create a support ticket record in Dataverse.
5. Generate or retrieve the ticket reference.
6. Return the creation result to Copilot Studio.
7. Display the ticket reference and status to the employee.

### Expected output

```json
{
  "success": true,
  "ticket_id": "INC-1002",
  "status": "New",
  "priority": "High",
  "message": "Your IT support ticket has been created successfully."
}
```

The actual ticket reference and status must come from the workflow execution result.

The agent should obtain employee confirmation before submitting a new ticket.

## 6. Microsoft Dataverse — Support Ticket Management

Dataverse provides structured storage for IT support requests.

### Proposed ticket fields

| Column | Data type |
|---|---|
| Ticket Reference | Text |
| Employee Name | Text |
| Employee Email | Email/Text |
| Issue Description | Multiple lines of text |
| Category | Choice |
| Priority | Choice |
| Status | Choice |
| Created On | Date and time |
| Modified On | Date and time |

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

The initial demonstration can use a simplified ticket lifecycle. Production implementations should also consider reassignment, cancellation, reopening and audit history.

### Data management objectives

- Store ticket information in Dataverse.
- Retrieve tickets through approved tools.
- Maintain ticket status and priority.
- Apply appropriate access controls.
- Return only authorized ticket information.

---

# End-to-End Use Cases

## Use Case 1: VPN Troubleshooting

**Employee:** My VPN is not connecting.

Expected workflow:

1. Copilot Studio understands the issue.
2. The Foundry specialist agent provides knowledge-grounded troubleshooting.
3. The agent asks relevant questions.
4. The MCP service tool checks VPN availability.
5. The agent combines the results and provides troubleshooting instructions.
6. If the problem remains unresolved, the agent offers ticket creation.

## Use Case 2: Check Service Availability

**Employee:** Is the VPN service currently available?

Expected workflow:

1. Identify the requested service.
2. Invoke `get_service_status`.
3. Retrieve the tool response.
4. Present the returned service status.
5. Explain if the status cannot be verified.

## Use Case 3: Track an Existing Ticket

**Employee:** What is happening with ticket INC-1001?

Expected workflow:

1. Extract the ticket reference.
2. Invoke `get_ticket_status`.
3. Validate that the employee is authorized to view the ticket.
4. Retrieve the ticket information.
5. Return the status and relevant details.

## Use Case 4: Create a New Support Ticket

**Employee:** My email access is still not working. Raise a ticket.

Expected workflow:

1. Understand the unresolved issue.
2. Gather required ticket details.
3. Determine the appropriate category and priority.
4. Confirm the details with the employee.
5. Invoke the Power Automate flow.
6. Create the Dataverse record.
7. Return the actual ticket reference and status.

## Use Case 5: Restricted Technical Operation

**Employee:** Should I restart the company firewall?

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
| Tool Integration | Model Context Protocol | External tool access |
| Backend | Python | MCP server implementation |
| Workflow Automation | Microsoft Power Automate | Ticket creation |
| Data Platform | Microsoft Dataverse | Support ticket storage |
| Cloud Platform | Microsoft Azure | Cloud services and identity |
| Identity and Access | Microsoft Entra ID / Azure RBAC | Authentication and authorization |
| Monitoring | Application Insights / Azure monitoring | Operational observability, where configured |

---

# Repository Structure

```text
azure-ai-foundry-enterprise-support-agent/
│
├── copilot-studio/
│   ├── README.md
│   ├── agent-instructions.md
│   └── conversation-scenarios.md
│
├── azure-ai-foundry/
│   ├── README.md
│   ├── agent-instructions.md
│   └── knowledge/
│       └── it-support-handbook.md
│
├── mcp-server/
│   ├── server.py
│   ├── tools/
│   │   ├── service_status.py
│   │   └── ticket_status.py
│   ├── requirements.txt
│   └── README.md
│
├── power-automate/
│   ├── README.md
│   └── create-it-support-ticket.md
│
├── dataverse/
│   ├── README.md
│   └── ticket-schema.md
│
├── docs/
│   ├── architecture.md
│   ├── use-cases.md
│   ├── security.md
│   └── screenshots/
│
├── tests/
│   ├── mcp-tool-tests/
│   └── integration-tests/
│
├── .env.example
├── .gitignore
└── README.md
```

This is the planned documentation and source-code organization. Files should be added as their corresponding components are implemented.

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
git clone https://github.com/Keyrun1227/azure-ai-foundry-enterprise-support-agent.git

cd azure-ai-foundry-enterprise-support-agent
```

## 2. Configure the Azure AI Foundry Agent

1. Open the Azure AI Foundry portal.
2. Create or open the relevant Foundry project.
3. Create the specialist IT troubleshooting agent.
4. Configure the agent instructions.
5. Add the approved IT support handbook as knowledge.
6. Test the agent using representative support scenarios.
7. Configure the required identity and access permissions.

## 3. Configure Copilot Studio

1. Create the Enterprise IT Support Agent.
2. Add the main conversational instructions.
3. Connect the Azure AI Foundry specialist agent through the supported connected-agent integration.
4. Configure the appropriate orchestration behavior.
5. Add the MCP server as a tool through the supported integration.
6. Connect the Power Automate ticket creation action.
7. Validate the complete conversation flow.

## 4. Run the MCP Server

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r mcp-server/requirements.txt
```

Run the server using the transport and startup command configured in its implementation.

The MCP server must be reachable through an endpoint and transport supported by the chosen Copilot Studio integration.

## 5. Configure Power Automate

1. Open Power Automate.
2. Create the `Create_IT_Support_Ticket` flow.
3. Configure its supported trigger.
4. Add input validation.
5. Create a Dataverse row.
6. Return the ticket reference and status.
7. Connect the flow to Copilot Studio.
8. Test successful and failed executions.

## 6. Configure Dataverse

1. Create the IT Support Ticket table.
2. Configure the ticket columns.
3. Define appropriate choice values.
4. Configure table permissions and security roles.
5. Connect the table to the Power Automate workflow.
6. Verify that tickets are created and retrieved correctly.

---

# Testing and Evaluation

Testing should cover individual agent behavior, tool execution and end-to-end workflows.

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
- Unauthorized ticket access.
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

| Scenario | Expected result |
|---|---|
| VPN troubleshooting | Grounded troubleshooting guidance |
| VPN status enquiry | Service status returned by MCP |
| Ticket enquiry | Authorized ticket details returned |
| New support request | Dataverse ticket created |
| Restricted operation | Safe refusal and escalation |
| MCP unavailable | Clear tool failure response |
| Power Automate failure | No false ticket creation confirmation |

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

The following roadmap describes the intended implementation scope.

### Phase 1 — AI Agent Foundation

- [x] Create Azure AI Foundry project.
- [x] Build the specialist IT troubleshooting agent.
- [x] Configure the agent instructions and safety restrictions.
- [x] Save and test the Foundry agent.
- [x] Create the Copilot Studio Enterprise IT Support Agent.
- [x] Configure its conversational instructions.
- [x] Connect the Foundry specialist agent to Copilot Studio.

### Phase 2 — MCP Integration

- [ ] Implement the Python MCP server.
- [ ] Implement `get_service_status`.
- [ ] Implement `get_ticket_status`.
- [ ] Configure the supported MCP transport.
- [ ] Connect MCP to Copilot Studio.
- [ ] Validate tool execution and error handling.

### Phase 3 — Business Workflow Automation

- [ ] Create the Dataverse IT Support Ticket table.
- [ ] Build the Power Automate ticket creation flow.
- [ ] Configure request validation.
- [ ] Return the ticket reference and creation status.
- [ ] Connect the workflow to Copilot Studio.
- [ ] Validate ticket creation and retrieval.

### Phase 4 — End-to-End Validation

- [ ] Test VPN troubleshooting.
- [ ] Test service availability checks.
- [ ] Test ticket status retrieval.
- [ ] Test new ticket creation.
- [ ] Validate safety restrictions.
- [ ] Test authorization and failure scenarios.
- [ ] Run agent evaluations.
- [ ] Configure a user-facing channel.
- [ ] Complete deployment and documentation.

---

# Project Scope and Current Status

This repository documents a practical implementation of an enterprise agentic AI support solution.

The Foundry specialist agent and Copilot Studio agent have been created, and the Foundry agent has been connected to Copilot Studio.

MCP server development, external tool execution, Power Automate integration, Dataverse ticket management and end-to-end validation remain implementation tasks until independently tested.

Features in the architecture and roadmap describe the intended system behavior, not necessarily completed functionality.

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
