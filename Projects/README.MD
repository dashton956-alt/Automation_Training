🚀 Real‑World Automation Projects (End‑to‑End, Portfolio‑Ready)
Each project grows in complexity and touches multiple areas of your training path.

📦 PROJECT 1 — NetBox → Golden Config Automation Pipeline
(Python + Jinja2 + Nornir + NetBox SoT + GitHub Actions)
Problem
Infra engineers struggle with inconsistent device configs, outdated docs, and manual CLI pushes.
What you build
A fully automated pipeline:

NetBox as Source-of-Truth

Sites, racks, IPAM, interfaces, VLANs


Python Jinja2 Templates

Arista cEOS spine
Nokia SR Linux leaf


Nornir Execution

Render configs
Validate diffs
Push only if clean


GitHub Actions CI

Lint templates (ruff)
Run pytest on Jinja renders
Generate & upload config artifacts


End Result

Golden config bundle per site
Fully reproducible via IaC



Skills Covered
✔ Core Python
✔ REST + NetBox API
✔ Jinja2
✔ IaC execution
✔ Testing
✔ CI/CD
✔ Dev productivity (uv)

📦 PROJECT 2 — FastAPI “Infra Normalizer” Microservice
(REST APIs + FastAPI + Pydantic + JSON schemas + uv)
Problem
Different systems return messy API fields (NetBox, InfraHub, Gluware, Meraki, Mist).
What you build
A small FastAPI service that normalizes data into a clean schema for automation tools.
Example:
/device/<hostname> returns:
JSON{  "hostname": "srl-leaf-01",  "mgmt_ip": "10.1.0.10/32",  "role": "leaf",  "vendor": "Nokia",  "asn": 65010,  "interfaces": [...]}Show more lines
Add features

Caching layer (Redis optional)
Async API calls
Swagger/OpenAPI docs
JSON schema validation using Pydantic

Skills Covered
✔ REST APIs
✔ Schema validation
✔ API design
✔ Tooling for automation pipelines

📦 PROJECT 3 — Event‑Driven Auto‑Config Platform
(n8n + NetBox Webhooks + OPA/Rego + Nornir)
Problem
Humans shouldn’t push device configs.
The SoT should drive everything.
What you build
An event-driven pipeline:

NetBox Webhook → n8n trigger
Detect changes on:

interface
IP address
device role


n8n Node → GAIT-style validation
Run OPA/Rego rules such as:

interface names follow standards
max TX power is within RF limits
no duplicate IPs


If pass → auto-build config
n8n calls your FastAPI service
n8n → Nornir deploy
Push only validated changes
If fail → GitHub issue + Slack alert

Skills Covered
✔ Event-driven automation
✔ Policy-as-Code
✔ Multi-system orchestration
✔ Integration patterns

📦 PROJECT 4 — Network Change Impact AI Agent
(RAG + NetBox +-docs index + AI summarization + n8n/AnythingLLM)
Problem
Engineers need quick summaries:

"What changes if I modify vlan 100?"
"What devices are impacted?"
"Is there a risk?"

What you build
An AI-powered impact analysis engine:

Index

LLDs
HLDs
Standard configs
NetBox device details


Query pipeline

n8n LLM node (Anthropic / LocalAI)
RAG lookup
Pass NetBox graph data


Output

risk summary
devices impacted
compliance concerns
recommended remediation



Skills Covered
✔ RAG
✔ Context engineering
✔ AI safety & eval
✔ Knowledge indexing

📦 PROJECT 5 — Private 5G RF Design Calculator
(Python backend + Excel front-end + Jinja2 reports)
This directly matches your RF/5G work.
What you build
A tool that calculates:

Max conducted Tx (dBm)
Total cable loss (coax or feeder)
Antenna gain lookup
EIRP output
RACH format selector
UL/DL separation (0 for TDD, automatic for FDD)
Validations vs Ofcom limits (Shared spectrum N77/N78)

Input options:

Radio model
Cable type + length
Antenna model
Internal vs external antenna
Band and channel centre freq

Output:

Auto-generated LLD-ready PDF
Excel calculator (formulas you already use)
Jinja2 RF summary template

Skills Covered
✔ Python
✔ Excel automation
✔ Radio engineering calculations
✔ Jinja2 reporting
Perfect for private 5G project work.

📦 PROJECT 6 — Full IaC Lab Deployment (Containerlab + Terraform)
(IaC + Infra automation + Networking)
What you build

Terraform

Defines lab topology
Defines site variables


Containerlab

Deploys cEOS + SRL nodes
Loads startup configs


Bootstrap automation

Nornir check-mode
Drift detection


GitHub Actions

Run topology validation
Lint configs
Publish topology map



Skills Covered
✔ Terraform
✔ GitOps
✔ IaC Immersion
✔ Lab orchestration

📦 PROJECT 7 — Network Standards Library (Policy-as-Code + RAG)
(Rego + OpenAPI + RAG + GitHub CI)
What you build
A unified repo where you store:

Naming standards
IP addressing rules
Interface patterns
VLAN rules
RF constraints
Max EIRP power tables
Cable-loss models

Everything becomes Policy-as-Code.
Then:

Run weekly validation as CI
Expose policies via an API
Allow external tools (n8n, FastAPI, Nornir) to query
Use RAG to generate plain-English explanations

Skills Covered
✔ Rego
✔ Policy pipelines
✔ API integrations
✔ AI-assisted documentation

📦 PROJECT 8 — Full MCP-Compliant Automation Platform
(GAIT rules + multi-agent tools + GitHub PR automation)
This aligns with your long-term NOVA platform goals.
What you build
A production-ready automation stack:

MCP server (your PoC)
GAIT validation layers
GitHub PR creation & analysis using AI
n8n workflows calling MCP server
Tool calling (run_nornir, get_config, create_change_ticket)
Documentation auto-generation

Skills Covered
✔ Multi-agent system design
✔ Tool calling
✔ Secure AI practices
✔ Governance

📦 Project 1 — NetBox → Golden Config Pipeline
High‑level goal:
Automate the full process of generating network configs from a Source‑of‑Truth.
What it teaches:

Using APIs to fetch inventory
Rendering Jinja2 templates
Running Nornir for dry‑run and real pushes
Using GitHub Actions for CI checks


📦 Project 2 — FastAPI Infrastructure Normalizer
High‑level goal:
Create a simple API service that cleans and standardises network data (NetBox, InfraHub, etc.).
What it teaches:

REST API design
Pydantic data validation
Converting messy fields into clean automation-ready schemas


📦 Project 3 — Event‑Driven Auto‑Config Platform
High‑level goal:
Trigger automation when infrastructure changes — no human needed.
What it teaches:

Webhooks from NetBox
n8n event workflows
OPA/Rego policy validation
Auto-pushing configs only when compliant


📦 Project 4 — AI Change Impact Analysis Agent
High‑level goal:
Use AI to summarise network changes and predict impact.
What it teaches:

RAG knowledge indexing
Combining NetBox data + docs
Building AI tools that explain risk and dependencies


📦 Project 5 — Private 5G RF Calculator
High‑level goal:
Automate RF engineering calculations for private 5G radio design.
What it teaches:

Converting Watts ↔ dBm
Computing cable loss, antenna gain, and EIRP
Generating PDFs or Excel reports
Building tools that support RF/LLD design


📦 Project 6 — IaC Lab Deployment (Terraform + Containerlab)
High‑level goal:
Deploy an entire virtual network lab using Infrastructure-as-Code.
What it teaches:

Writing Terraform modules
Building Containerlab topologies
Automating device bootstrapping
Validating topology in CI


📦 Project 7 — Network Standards Policy Library
High‑level goal:
Turn all network rules into Policies-as-Code.
What it teaches:

Writing OPA/Rego rules
Creating a standards catalogue
Using policies in CI and automation tools
Linking compliance into change workflows


📦 Project 8 — MCP-Compliant Automation Platform
High‑level goal:
Build a complete automation control plane with GAIT rules, n8n workflows, and tool‑calling AI agents.
What it teaches:

Multi-component automation design
Governance and audit trails
Tool calling for actions (run Nornir, fetch configs, create tickets)
AI-assisted PR reviews and change analysis