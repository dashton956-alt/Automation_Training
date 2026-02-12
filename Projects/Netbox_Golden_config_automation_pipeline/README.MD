 PROJECT 1 — NetBox → Golden Config Automation Pipeline
A slow, guided walkthrough for beginners → intermediate → advanced.

🧠 Step 0 — What this project actually is
You are building a pipeline that:


Pulls data from NetBox
(hostname, interfaces, VLANs, IPs, BGP ASN, device role, etc.)


Feeds that data into Jinja2 templates
(spine/leaf configs for cEOS + SRL)


Uses Nornir to run a DRY‑RUN diff
(see what would change)


Optionally deploys the config to your lab


Runs GitHub Actions CI
(lint the code, test Jinja templates, and generate configs automatically)


This is exactly how real automation teams build pipelines.

🧩 Step 1 — The Minimum You Need
This project can be built incrementally.
Here’s the minimum starting toolkit:
Tools

Python
NetBox running locally or remote
uv (your package manager)
Git + GitHub repo
Nornir (later)

Python libraries
Start with only:
httpx
pydantic
jinja2

Later you’ll add:
nornir
nornir-napalm
nornir-utils

Don't install everything at once — we build layer-by-layer.

🔍 Step 2 — Understand the Flow Before Coding
Think of this as a 3‑stage pipeline:
[ NetBox ] → [ Python Data Model ] → [ Jinja Template ] → [ Config Output ]

Let’s break this down slowly.

🧱 Step 3 — NetBox → Python (reading inventory)
Why this matters
Your templates must be driven by a SoT — no hardcoding.
What you do
You write a tiny Python script that:

Connects to NetBox
Asks for a single device
Prints the JSON

Example (NOT code yet, just logic):
GET /api/dcim/devices/?name=srl-leaf-01
GET /api/ipam/ip-addresses/?device_id=<id>
GET /api/dcim/interfaces/?device_id=<id>

Goal of this step
Get comfortable with NetBox API and the shape of the data.

🧱 Step 4 — Turn NetBox JSON into “clean” Python data
Raw API JSON is messy.
You want a clean object like this:
Device:
  hostname: "srl-leaf-01"
  mgmt_ip: "10.10.10.3/32"
  role: "leaf"
  asn: 65011
  interfaces:
    - name: ethernet-1/1
      ip: 10.1.1.1/31
      vlan: 100

This is where Pydantic comes in.
Why Pydantic?

Validates missing fields
Ensures types (string, int, list)
Gives your Jinja templates predictable data

Goal of this step
Create a reliable “device model” class.

🧱 Step 5 — Build Your First Jinja2 Template
Don’t build everything at once.
Start simple. Example template:
hostname {{ device.hostname }}
!
interface mgmt0
  ip address {{ device.mgmt_ip }}
!

Baby step goal
Render a config file into:
output/spine01.cfg

If you can do this, you can build the whole project.

🧱 Step 6 — Add More Template Complexity (Slowly)
Add building blocks one at a time:

Loop over interfaces
Add BGP
Add VLANs
Add OSPF/ISIS (if your lab uses them)

Example interface loop:
{% for interface in device.interfaces %}
interface {{ interface.name }}
  description {{ interface.description }}
  ip address {{ interface.ip }}
{% endfor %}

Goal
Be comfortable feeding structured data → Jinja template.

🧱 Step 7 — Automate Rendering for ALL Devices
Your script evolves:
for device in netbox.get_all_devices():
    model = DeviceModel(**device_json)
    config = render_template(model)
    save_config(device.hostname + ".cfg")

This produces a Golden Config Bundle.

🧱 Step 8 — Introduce Nornir (Dry-Run First)
Now you add Nornir to:

load an inventory generated from NetBox
SSH to devices
run “diff” checks
ensure config matches what you expect

Important:
Start with NAPALM "compare_config".
This shows diffs without making changes.

🧱 Step 9 — Add GitHub Actions CI
Add automation:

Every push to main:

lint Python (ruff)
test Jinja rendering (pytest)
build configs (python generate_configs.py)
upload produced configs as artifacts




🧱 Step 10 — Optional Advanced Features
You can add these later:
⭐ Validation (GAIT-Style)
Check naming, VLAN ranges, IP format.
⭐ Multi-vendor support
cEOS, SRL, EOS, Cisco, Juniper.
⭐ Config Deployment
Let Nornir push configs only when validated.
⭐ Change Reports
Generate HTML summaries of diffs.

🧩 Summary: Your Slow-Burn Learning Path
Here is the step-by-step order I recommend while learning:
1. Query NetBox (print JSON)
2. Build Pydantic model
3. Build simple Jinja2 config
4. Render config for one device
5. Render configs for all devices
6. Add interfaces → routing → VLANs
7. Add Nornir dry-run
8. Add Nornir deploy
9. Add GitHub CI

Each step builds on the last — no overwhelm.