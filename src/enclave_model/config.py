"""Configuration schemas and default parameters for Enclave models."""

from dataclasses import dataclass, field


@dataclass
class DeploymentConfig:
    """Black start, skeleton renovation crew, and cultural flow seeding."""
    # Phase 1: Hard Skeleton Crew Caps
    max_system_architects: int = 3
    max_lead_engineers: int = 15
    max_construction_integration_workforce: int = 100
    skeleton_crew_renovation_months: int = 8
    skeleton_crew_monthly_stipend: float = 14_000.0  # Competitive hazard/buildout stipend

    # Phase 3 & Year 1: Flow Seeding & Hyperscaler Triad
    cohort_1_existing_employees_seeded: int = 1000  # First internal transferred cohort of existing staff
    flow_productivity_velocity_boost: float = 0.25  # +25% innovation velocity from intact teams & zero friction
    flow_turnover_suppression_pct: float = 0.85     # 85% turnover suppression in Cohort 1
    year_1_work_as_usual_velocity_retention: float = 1.0  # 100% baseline sprint velocity maintained from Day 1
    telemetry_incremental_improvement_gain: float = 0.04  # 4% annual operational compounding from human telemetry assimilation


@dataclass
class DemographicsConfig:
    """Workforce, retention, telemetry-optimized burnout, and logarithmic population governor."""
    initial_workforce: int = 2500
    carrying_capacity_workforce: int = 5000  # Asymptotic maximum workforce limit (K_workforce)
    target_annual_growth: float = 0.08       # Unconstrained baseline expansion rate (r)
    dependent_ratio: float = 0.40            # 40 dependents per 100 workers
    contractor_ratio: float = 0.15           # Service and support staff per worker
    external_turnover_rate: float = 0.18     # Traditional market churn (18%/yr)
    enclave_retention_bonus: float = 0.50     # Baseline cut in turnover (50%)
    ai_telemetry_burnout_reduction: float = 0.25  # Additional 25% reduction in burnout attrition
    wearable_compliance_rate: float = 1.0     # Mandatory sign-off for residency (100%)

    # Vital Dynamics for Pre-Assimilation Balance
    annual_birth_rate: float = 0.022         # 22 births per 1,000 residents per year
    annual_death_rate: float = 0.004         # 4 natural deaths per 1,000 residents per year


@dataclass
class HousingConfig:
    """Spatial facilities and housing infrastructure."""
    initial_units: int = 3500
    capex_per_unit: float = 280_000.0  # Modular, high-density construction
    capex_amortization_years: int = 35
    annual_maintenance_pct: float = 0.02  # 2% of asset value / year
    max_capacity_units: int = 15_000


@dataclass
class EconomyConfig:
    """Labor costs, real estate offset, universal baseline, and internal credit mechanics."""
    # Traditional distributed market baseline
    traditional_avg_cash_salary: float = 165_000.0
    traditional_office_lease_per_head: float = 14_000.0
    replacement_cost_pct_salary: float = 0.60  # Cost to re-hire and train

    # Enclave model: Dual-Layer Economy & Exit Settlements
    enclave_avg_cash_salary: float = 65_000.0  # Modest external fiat salary for external ties/savings
    universal_baseline_per_capita: float = 16_000.0  # Food, clean water, healthcare, zero-friction baseline
    annual_credits_issued_per_worker: float = 25_000.0  # Internal credits for work inputs (discretionary luxuries)
    internal_credit_burn_recovery_pct: float = 0.70  # Closed-loop recovery rate (credits spent recycle into operations)
    recruitment_savings_factor: float = 0.35  # Lower onboarding friction due to on-site immersion

    # Separation & Exit Settlement
    credit_exit_conversion_rate: float = 0.75  # Lower-end market rate ($0.75 per 1.0 credit)
    avg_unredeemed_credit_balance_at_exit: float = 8_000.0
    severance_weeks_unemployment_equiv: int = 12  # Standard 12 weeks unemployment equivalent pay
    standard_weekly_unemployment_benefit: float = 600.0  # Regional baseline unemployment level

    # The +a Telemetry Asset Valuation (Hyperscaler RLHF & Foundation Model Training)
    telemetry_expert_hours_per_worker_annual: float = 1_800.0
    telemetry_hourly_market_value: float = 80.0  # Equivalent market cost of expert RLHF / code reasoning data
    telemetry_frontier_ai_multiplier: float = 1.20  # Frontier strategic proprietary multiplier
    biometric_health_telemetry_value_per_capita: float = 30_000.0  # Annual value of non-invasive continuous clinical/ergonomic data


@dataclass
class OperationsConfig:
    """Energy, logistics, subterranean datacenter, and thermodynamic recycling."""
    power_kwh_per_capita_day: float = 28.0
    grid_cost_per_kwh: float = 0.11
    municipal_services_opex_per_capita: float = 6_500.0  # Internal security, sanitation, transit
    logistics_buffer_days: int = 45

    # Subterranean Datacenter & Geothermal Energy Recycling
    datacenter_mw_capacity: float = 25.0  # 25 MW underground AI & compute cluster
    turbine_electric_recovery_pct: float = 0.18  # 18% of thermal waste converted to electricity via ORC turbines
    agricultural_heating_offset_annual: float = 4_500_000.0  # Free heat for greenhouses & vertical farms
    district_heating_offset_annual: float = 3_200_000.0  # Free radiant heating & hot water for Hab-Cells

    # Regional Symbiosis & Local Distribution Partnership
    regional_steam_export_revenue_annual: float = 1_850_000.0  # Subsidized industrial steam sales to local cleaning/plants
    regional_power_export_kwh_annual: float = 12_000_000.0     # 12M kWh shared with municipal grid
    regional_power_export_rate_per_kwh: float = 0.065          # Subsidized rate offered to local grid (vs $0.11 baseline)
    local_logistics_subsidy_cost_annual: float = 950_000.0     # Shared EV chargers & fleet sorting hubs
    local_ai_partnership_dividend_annual: float = 2_100_000.0  # Value of host tax abatements & priority supply deals from AI licensing


@dataclass
class WellBeingConfig:
    """Human conditioning layer: calibrated eustress, contentment floor, and anti-drift tuning."""
    target_somatic_contentment: float = 0.85     # High physical satisfaction (sleep, nutrition, zero chores)
    target_productive_eustress: float = 0.75     # Stimulating challenge / urgency to prevent cognitive drift
    max_tolerable_distress: float = 0.25         # Distress ceiling before decompression triggers
    max_tolerable_drift_apathy: float = 0.20     # Drift ceiling before tension vectors trigger
    dopaminergic_reward_interval_days: int = 7   # Micro-dosed artisanal culinary/recreation drops
    synthetic_urgency_sprint_multiplier: float = 1.15 # Pacing acceleration during drift detection

    # Ambient Macro-Stressors & Organic Self-Policing
    ambient_eviction_pressure_factor: float = 0.85   # Immediate loss of shelter upon termination/resignation
    external_world_volatility_anxiety: float = 0.75  # Acute fear/anxiety of rejoining unstable external world
    external_work_scarcity_factor: float = 0.90      # Extreme scarcity of high-value work outside enclave
    organic_self_policing_efficiency: float = 0.92   # Eliminates need for human supervisors via self/peer policing


@dataclass
class EnclaveConfig:
    """Comprehensive configuration for an enclave macro-model."""
    name: str = "Standard Corporate Arcology"
    simulation_years: int = 10
    deployment: DeploymentConfig = field(default_factory=DeploymentConfig)
    demographics: DemographicsConfig = field(default_factory=DemographicsConfig)
    wellbeing: WellBeingConfig = field(default_factory=WellBeingConfig)
    housing: HousingConfig = field(default_factory=HousingConfig)
    economy: EconomyConfig = field(default_factory=EconomyConfig)
    operations: OperationsConfig = field(default_factory=OperationsConfig)
