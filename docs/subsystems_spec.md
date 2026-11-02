# Subsystems Specification

This document details the mechanics, mathematical relationships, and variables modeled across the enclave's subsystems.

---

## 1. Demographics & Workforce Engine (`src/enclave_model/modules/demographics.py`)

- **Full-Time Employment Status**:
  - All working residents are full-time employees with complete Tier 0 baseline protection and internal credit earning rights—eliminating fragmented gig contractors or second-class labor.
- **Workforce Cohorts**:
  - `Tier 1 (Core Talent)`: High-skill engineers, researchers, strategists, software/hardware architects.
  - `Tier 2 (Operational Leads & Systems Architects)`: Functional coordinators and architects elevated by AI for systemic efficiency rather than political status.
  - `Tier 3 (Operations & Facilities)`: Power plant operators, microgrid engineers, robotic technicians.
  - `Tier 4 (Service Providers & Community Care)`: Healthcare staff, culinary operators, educators, childcare providers (all full corporate enclave employees).
  - `Dependents`: Partners, children, elder dependents.
- **AI-Driven Shift & Skillset Allocation**:
  - Multi-watch continuous scheduling (e.g., Alpha, Beta, Gamma watches covering 24/7 cycles).
  - Shifts mapped algorithmically by Central Governing AI to individual cognitive strengths, skillsets, and biometric circadian peak-focus windows.
- **Objective Upward Mobility**:
  - Promotions and leadership appointments are determined algorithmically:
    $$\text{Mobility Score } (\mathcal{M}) = \frac{\text{Deliverable Velocity} \times \text{Quality Index} + \text{Civic Mentoring}}{\text{Systemic Friction} + \text{Error Rate}}$$
  - Optimizes for operational throughput and eliminates corporate political games, status bias, and managerial favoritism.
- **Attrition Dynamics**:
  - Base external turnover rate ($T_{\text{ext}}$) vs. Enclave turnover rate ($T_{\text{enc}}$).
  - Enclave retention factor:
    $$T_{\text{enc}} = T_{\text{ext}} \times (1 - \text{RetentionBonus})$$
    where $\text{RetentionBonus} = f(\text{ZeroFrictionQoL}, \text{CreditPurchasingPower}, \text{BurnoutMitigation})$.
- **Resident Well-Being Conditioning (The Anti-Drift Engine)**:
  - Dynamically calculates the Well-Being Index ($\text{WBI}$):
    $$\text{WBI} = \alpha \cdot \mathcal{S}_{\text{somatic}} + \beta \cdot \mathcal{E}_{\text{eustress}} - \gamma \cdot \mathcal{D}_{\text{distress}} - \theta \cdot \mathcal{A}_{\text{drift}}$$
  - Modulates accommodations (acoustic isolation, dopaminergic culinary drops, sensory decompression) vs. tension vectors (synthetic sprint deadlines, task complexity escalation, unannounced drills).
  - Keeps workforce in the optimal Yerkes-Dodson band: content enough to remain loyal and healthy, but stressed enough to avoid cognitive drift.
  - **Ambient Macro-Stressors & Self-Policing**:
    - Leverages 4 background existential realities (immediate eviction upon exit, volatility of the external world, scarcity of external technical work, and everyday life friction).
    - Eliminates managerial policing by instilling organic **self-monitoring**, **self-correcting**, and **cohort peer self-policing**.

---

## 2. Housing & Modular Spatial Infrastructure (`src/enclave_model/modules/housing.py`)

- **Standardized Modular Architecture**:
  - Enclave grows via modular **Hab-Cells (HC)** (e.g., 250–500 units per module) connected to the core utility spine.
- **Unit Typologies**:
  - **Tier 0 Baseline Pods**: Efficient, acoustically isolated studio micro-units guaranteed to every worker.
  - **Upgraded Credit Suites**: 1–2 bedroom units or multi-room family residences unlocked through internal credits.
- **Metrics**:
  - `Capacity utilization`: Target between 80% and 92% to preserve expansion headroom.
  - `Automated Expansion Trigger`: When occupancy exceeds 90%, auto-scaffold next modular phase.
  - `Amortized CapEx`: Total modular construction cost depreciated over expected lifespan (typically 30–40 years).
  - `Facility Maintenance`: Set as a fixed percentage of physical capital valuation ($2\text{--}3\%/\text{year}$).

---

## 3. Economic & Credit Engine (`src/enclave_model/modules/economy.py`)

The enclave models a **Dual-Layer Closed-Loop Economy**:

### 3.1 Layer 0: The Universal Baseline Floor
- **Zero-Cognitive-Overhead Package**: Guaranteed unconditionally to all residents:
  - Rent-free modular housing and maintenance.
  - Nutrient-complete dining commons and hydration.
  - 100% microgrid electricity, heating, and cooling.
  - On-site healthcare, wellness, and preventive medicine.
  - Automated intra-hub logistics and transit.

### 3.2 Layer 1: The Closed-Loop Credit System ($\mathcal{C}$)
- **Credit Inflow (Issuance)**:
  $$\mathcal{C}_{\text{issued}} = \text{Base Work Input} + \text{Performance Milestones} + \text{Civic Maintenance Bounties} + \text{Innovation Royalties}$$
- **Credit Outflow (Sinks & Burn)**:
  - Living space upgrades (square footage, balconies, views).
  - Artisanal dining, craft beverages, private dining reservations.
  - Consumer technology, computing hardware allotments, entertainment.
  - External travel / sabbatical leave credits (converted into fiat via corporate escrow).
- **Macro Balance Sheet Comparison**:
  - **Traditional Distributed Model**:
    $$\text{Cost}_{\text{ext}} = \text{Market Cash Salaries} + \text{Commercial Office Leases} + \text{Recruitment Churn Turnover}$$
  - **Enclave Mode**:
    $$\text{Cost}_{\text{enc}} = \text{Adjusted Cash Payroll} + \text{Baseline Floor OpEx} + \text{Amortized CapEx} + \text{Municipal OpEx} + \text{Credit Network Reserve}$$

- **Executive Override Governance (C-Suite vs. AI Bureaucracy)**:
  - While daily management is non-hierarchical, the C-suite possesses ultimate sovereign override power.
  - Any executive override command must navigate a 5-stage algorithmic bureaucracy gauntlet:
    1. Monte Carlo life-support stress simulations.
    2. Workforce biometric friction and attrition calculations.
    3. Formal review of AI-generated Pareto counter-proposals.
    4. Cryptographic personal fiduciary liability underwriting.
    5. A mandatory 72-hour cooling-off window with public disclosure to the hub's Resident Council.

---

## 4. Municipal Operations & Circular Resilience (`src/enclave_model/modules/operations.py`)

- **Year 1 Triad Stabilization (Datacenter, Energy, Food)**:
  - **Subterranean Datacenter Core**: 25–50 MW AI supercomputing cluster encased in conductive graphitic bedrock, stabilizing PUE at $\le 1.05$ with zero open-air cooling towers.
  - **Thermodynamic Co-Gen & Steam Sharing**: Superheated exhaust ($85^\circ\text{C}\text{--}130^\circ\text{C}$) drives ORC micro-turbines, regenerating $15\text{--}20\%$ electrical power, while medium-grade steam is exported to regional commercial laundries and factories at a 50% discount.
  - **In-House Aeroponics & Protein Fermentation**: Medium-grade turbine exhaust warms vertical aeroponic domes to optimal $21^\circ\text{C}\text{--}23^\circ\text{C}$ root temperatures, delivering fresh produce and proteins at zero auxiliary heating fuel cost.
- **Hyperscaler Closed-Loop Telemetry Assimilation**:
  - The corporate hyperscaler ingests biometric and operational telemetry from Cohort 1 residents.
  - Real-time closed-loop tuning dynamically optimizes transit dispatch, circadian lighting, ambient Hab-Cell acoustics, and shift allocations.
  - Core knowledge workers continue unbroken product and engineering velocity ("Work As Usual") free from external municipal friction.
- **24/7 Continuous Capability & Multi-Layer Redundancy Matrix**:
  - Operates around the clock across multi-watch rotations with $N+2$ to $N+3$ redundancy tiers:
    - **Power**: Baseload SMR + Bedrock Geothermal $\to$ ORC Turbines $\to$ 72-hr Subterranean Battery Bank $\to$ Regional Microgrid Tie.
    - **Compute**: Primary 25 MW Cavern Cluster $\to$ Mirror Cavern Backup $\to$ Edge SLM Hab-Cell mesh $\to$ EMP-shielded Vault.
    - **Hydrology & Water**: Multi-stage membrane filtration (96% recovery) $\to$ Bedrock Aquifers $\to$ Atmospheric Water Generators $\to$ 120-Day Reservoir.
    - **Life Support & Food**: Vertical aeroponics $\to$ Subterranean Fermentation $\to$ 90-Day Dry-Goods Climate Buffer $\to$ Bilateral Ag-Coop Priority Corridors.
    - **Human Operators**: Active Shift Operators $\to$ Hot-Standby Watch $\to$ Cross-Trained Shadow Personnel ready to step in immediately upon biometric alert.
- **Power & Utility Microgrid**:
  - Baseline daily power consumption per capita ($25\text{--}45\text{ kWh/day}$) + industrial and compute datacenter loads.
  - Primary generation: Dedicated Small Modular Reactor (SMR) or solar/geothermal microgrid.
  - Waste heat recovery from datacenters routed directly to residential heating and hydroponic agriculture.
- **Hydrological Closed Loop**:
  - Multi-stage membrane filtration targeting $95\text{--}98\%$ greywater and blackwater recovery.
- **Nutritional Buffering**:
  - Vertical aeroponic cultivation producing fresh leafy greens, herbs, and cellular agriculture proteins.
  - 45–90 day dry-goods logistical strategic buffer.
