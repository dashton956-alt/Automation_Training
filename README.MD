# Automation Engineering Training Path

**Goal:** Master Python, Infrastructure-as-Code, networking automation, and AI-driven workflows for modern infrastructure environments.

---

## 📋 Table of Contents

1. [Core Python](#1-core-python)
2. [REST APIs with Python](#2-rest-apis-with-python)
3. [Jinja2 for Config Templates](#3-jinja2-for-config-templates)
4. [Source-of-Truth & Data Models](#4-source-of-truth--data-models)
5. [IaC & Execution Engines](#5-iac--execution-engines)
6. [UV & Dev Productivity](#6-uv--dev-productivity)
7. [Git, GitHub & CI/CD](#7-git-github--cicd)
8. [Containers & Environments](#8-containers--environments)
9. [Testing for Automation Engineers](#9-testing-for-automation-engineers)
10. [Policy-as-Code & Governance](#10-policy-as-code--governance)
11. [Event-Driven Automation](#11-event-driven-automation--orchestration)
12. [AI Fundamentals](#-ai-fundamentals-for-automation-engineers)

---

## 1. Core Python

**Goal:** Fast, practical Python fundamentals for infrastructure automation.

- **[You Need to Learn Python RIGHT NOW (EP1) - NetworkChuck](https://www.youtube.com/@NetworkChuck)** -- Fast-paced intro from a top content creator
- **[Python Beginner Tutorials - Corey Schafer](https://www.youtube.com/c/Coreyms)** -- Crystal-clear fundamentals with great production quality

**Practice Project:** Write a small CLI to query NetBox/InfraHub APIs and dump JSON to disk; run it through UV.

---

## 2. REST APIs with Python

**Goal:** Build robust APIs and understand how to integrate with OpsMill, InfraHub, NetBox, and n8n.

- **[FastAPI + Pydantic Series - Corey Schafer](https://www.youtube.com/c/Coreyms)** -- Modern API patterns and validation techniques
- **[FastAPI Part 1: Build a Web App + REST API - Corey](https://www.youtube.com/c/Coreyms)** -- Great for building tiny internal services that your automation workflows can call

**Practice Project:** Wrap a NetBox read-only endpoint in a FastAPI shim that normalizes fields for your Jinja2 templates.

---

## 3. Jinja2 for Config Templates

**Goal:** Master templating for network device configurations.

- **[Python & Jinja2 Cisco Network Automation - David Bombal ft. Hank Preston](https://www.youtube.com/c/davidbombal)** -- CSV → Jinja → configs workflow
- **[Jinja2 for Network Configs - Snack Minute](https://www.youtube.com/ciscolearningnetwork)** -- Compact primer from Cisco University

**Practice Project:** Build a golden-config Jinja2 bundle for your PoC spine/leaf lab (Arista cEOS + Nokia SR Linux), fed by NetBox data.

---

## 4. Source-of-Truth & Data Models

**Goal:** Establish authoritative inventory and design proper data models.

- **[NetBox Zero-to-Hero - NetBox Labs](https://www.youtube.com/c/NetBoxLabs)** -- Official mini-course from NetBox Labs
- **[Manage Your Network Like a PRO (NetBox + Docker)](https://www.youtube.com/@NetBoxLabs)** -- Practical end-to-end walkthrough
- **[NetBox Labs Community](https://www.youtube.com/@NetBoxLabs)** -- Community calls and integrations keep you current

**Practice Project:** Model a site → racks → devices → IPAM → VLANs infrastructure, then export data to your Nornir inventory.

---

## 5. IaC & Execution Engines

**Goal:** Learn Nornir, Ansible, and Terraform to automate infrastructure changes at scale.

- **[Nornir Tutorial - Deep Dive](https://rogerperkin.co.uk/)** -- Conceptual grounding with videos and blog posts
- **[Ansible: What It Is & How It Works - TechWorld with Nana](https://www.youtube.com/c/TechWorldwithNana)** -- Clear mental model before diving into network modules
- **[Terraform Explained in 15 Minutes - Nana](https://www.youtube.com/c/TechWorldwithNana)** -- IaC fundamentals and workflow essentials

**Practice Project:** Nornir inventory from NetBox → test "dry-run" diffs; Ansible check-mode for a small config drift fix; Terraform for lab infrastructure.

---

## 6. UV & Dev Productivity

**Goal:** Use modern Python tooling to speed up development workflows.

- **[UV Day-to-Day Usage - Corey Schafer](https://www.youtube.com/c/Coreyms)** -- Practical patterns for daily development
- **[UV vs pip/Poetry/Conda - DataCamp](https://www.datacamp.com/)** -- When to switch and migration notes

**Practice Project:** Replace pipx tools in your CI Docker images with uv tool equivalents to speed up your pipelines.

---

## 7. Git, GitHub & CI/CD

**Goal:** Master version control and automated deployment pipelines.

- **[Git & GitHub Crash Course - Traversy Media](https://www.youtube.com/c/TraversyMedia)** -- Latest short crash course
- **[GitHub Actions: CI/CD Tutorial - TechWorld with Nana](https://www.youtube.com/c/TechWorldwithNana)** -- From concepts to Docker build/push pipelines

**Practice Project:** Create a GitHub Actions workflow that runs uv run ruff, uv run pytest, builds docs, and publishes artifacts.

---

## 8. Containers & Environments

**Goal:** Containerize automation tools and infrastructure.

- **[Docker Tutorial (Full Course) - Nana](https://www.youtube.com/c/TechWorldwithNana)** -- Solid foundation with Compose and private registries
- **[Exploring Docker - Traversy Media](https://www.youtube.com/c/TraversyMedia)** -- Classic hands-on series for quick wins

**Practice Project:** Containerize your NetBox jobs or FastAPI shim; wire to GitHub Actions for automated builds.

---

## 9. Testing for Automation Engineers

**Goal:** Write reliable tests for your automation code.

- **[Python Testing - Corey Schafer](https://www.youtube.com/c/Coreyms)** -- Covers unittest/pytest, type hints, and Ruff
- **[Corey Schafer Channel Index](https://www.youtube.com/c/Coreyms)** -- Full playlists organized by topic

**Practice Project:** Write pytest tests for Jinja render correctness (input fixtures from NetBox), plus schema validation with Pydantic.

---

## 10. Policy-as-Code & Governance

**Goal:** Enforce compliance and standards through code policies.

- **[OPA Quickstart: Rego + JSON](https://www.openpolicyagent.org/)** -- Run OPA in Docker, write first policies
- **[CNCF: Deploying Policy-as-Code with OPA](https://www.cncf.io/)** -- Why, where, and how with best practices
- **[Rego Basics (Terraform Context)](https://www.openpolicyagent.org/docs/latest/)** -- Mental model before infra policy

**Practice Project:** Express GAIT checks as Rego (naming standards, max TX power constraints, interface patterns) and run in pre-deploy validation.

---

## 11. Event-Driven Automation & Orchestration

**Goal:** Build event-triggered workflows that react to infrastructure changes.

- **[StackStorm 101 / Overview](https://stackstorm.com/)** -- Event → rule → action mental model
- **[n8n Quick Start (Official)](https://n8n.io/)** -- Triggers, data mapping, errors/retries
- **[n8n AI Agents (2025)](https://n8n.io/)** -- Add model calls and tool use to workflows

**Practice Project:** n8n workflow: NetBox change → GAIT/OPA validate → (if pass) call Nornir/Ansible → on failure open GitHub issue + Slack alert.

---

## 🔶 AI Fundamentals for Automation Engineers

### A) Context Windows, Tokens & Performance

**Goal:** Understand how to work effectively with LLMs in your automation pipelines.

- **[Anthropic: Effective Context Engineering](https://www.anthropic.com/research)** -- The shift from prompt → context design for reliable agents
- **[IBM Technology: OWASP Top 10 for LLM Apps](https://www.youtube.com/c/IBMTechnology)** -- Prompt injection, insecure output handling, and security best practices
- **[Interview-Style Primers on Context Windows](https://www.youtube.com/)** -- Concise, interview-ready explanations

**Practice Project:**
- Budget tokens in your n8n LLM nodes: cap conversation history, chunk device docs, and pre-summarize long NetBox diffs
- Add "available input tokens = model_limit − expected_output − margin" to your pipeline config (document in repo)

---

### B) Prompt & Context Engineering

**Goal:** Write effective prompts and structure context for reliable AI outputs.

- **[ChatGPT Prompt Engineering for Developers - DeepLearning.AI + OpenAI](https://www.deeplearning.ai/)** -- Solid best practices and structured prompting
- **[Anthropic: Prompt Engineering Deep-Dive](https://www.anthropic.com/research)** -- How professionals think about iteration and evaluation

**Practice Projects:**
- Create a prompt library in your repos with system prompts for "Network LLD Summarizer", "Jinja Template Reviewer", "Git PR Explainer"
- Version them in Git and run weekly evaluations

---

### C) Retrieval-Augmented Generation (RAG)

**Goal:** Ground AI models with custom knowledge bases.

- **[RAG with Pinecone - James Briggs](https://www.youtube.com/c/JamesBriggs)** -- End-to-end demo with embeddings and vector databases
- **[Making RAG Better - Pinecone Webinar](https://www.pinecone.io/)** -- Design trade-offs and data preparation tips

**Practice Project:** Index your network standards (LLDs, HLDs, RF specs) and device documentation; use RAG to ground "config explanation" and "impact analysis" assistants.

---

### D) Function/Tool Calling

**Goal:** Enable AI agents to call external tools and APIs.

- **[OpenAI Function Calling Tutorial](https://platform.openai.com/docs/)** -- JSON-spec tools and end-to-end loops
- **[OpenAI Function Calling Docs](https://platform.openai.com/docs/guides/function-calling)** -- Canonical reference and best practices

**Practice Project:** Define tools for "get_device_config", "create_change_ticket", "run_nornir_task"; route user intents to tools in your n8n agents.

---

### E) LangChain & Agent Ecosystems (Optional)

**Goal:** Build sophisticated multi-step AI agents.

- **[LangChain Mastery 2025 (v0.3) - James Briggs](https://www.youtube.com/c/JamesBriggs)** -- 5-hour structured course

**Practice Project:** Build a change-impact agent: fetch NetBox objects → summarize diffs → check GAIT policies → propose remediation.

---

### F) Safety & Evaluation

**Goal:** Ensure AI agents are safe, reliable, and auditable.

- **[OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)** -- Threats and mitigations for prompt injection, vector weaknesses, and excessive agency

**Practice Project:**
- Add guardrails: deny external tool calls unless policy passes; sanitize model output; log all tool invocations
- Create a small evaluation set (10-20 test cases) for each AI workflow (e.g., "does it hallucinate interface names?")
- Track eval scores in your CI/CD pipeline

---

## 📚 Quick Reference Links

| Tool | Website | Use Case |
|------|---------|----------|
| **NetBox** | https://netbox.dev/ | Source of truth for network infrastructure |
| **Nornir** | https://nornir.readthedocs.io/ | Python-based network automation |
| **Ansible** | https://www.ansible.com/ | Infrastructure automation & configuration |
| **Terraform** | https://www.terraform.io/ | Infrastructure as Code |
| **FastAPI** | https://fastapi.tiangolo.com/ | Modern Python API framework |
| **Jinja2** | https://jinja.palletsprojects.com/ | Template engine for configs |
| **UV** | https://docs.astral.sh/uv/ | Fast Python package manager |
| **n8n** | https://n8n.io/ | Event-driven automation platform |
| **OPA/Rego** | https://www.openpolicyagent.org/ | Policy-as-Code engine |
| **StackStorm** | https://stackstorm.com/ | Event-driven automation engine |
| **Docker** | https://www.docker.com/ | Container platform |
| **GitHub Actions** | https://github.com/features/actions | CI/CD automation |
| **Pinecone** | https://www.pinecone.io/ | Vector database for RAG |
| **LangChain** | https://www.langchain.com/ | LLM orchestration framework |

---

**Last Updated:** February 2026
