"""State tracking and historical snapshot dataclasses."""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class YearState:
    """Metrics snapshot for a single simulation year."""
    year: int
    workforce: int
    dependents: int
    contractors: int
    total_population: int
    births: int
    deaths: int
    assimilation_quota: int
    carrying_headroom: int

    total_housing_units: int
    occupied_units: int
    occupancy_rate: float

    # Economic metrics
    enclave_payroll: float
    universal_baseline_cost: float
    total_credits_issued: float
    net_credit_subsystem_cost: float
    total_exit_settlement_cost: float
    enclave_municipal_opex: float
    enclave_energy_cost: float
    turbine_regenerated_value: float
    thermal_heating_savings: float
    net_regional_symbiosis_benefit: float
    amortized_housing_capex: float
    facility_maintenance_cost: float
    total_enclave_cost: float

    # Baseline comparison (counterfactual if company stayed external)
    baseline_payroll: float
    baseline_office_lease: float
    baseline_turnover_cost: float
    total_baseline_cost: float

    # Comparative outcomes
    net_annual_savings: float
    cumulative_net_savings: float
    total_plus_a_telemetry_value: float
    cumulative_plus_a_telemetry_value: float
    total_enterprise_economic_surplus: float
    cumulative_enterprise_surplus: float
    turnover_rate: float
    retained_workers_delta: int


@dataclass
class SimulationHistory:
    """Stores full timeline of annual states and helper methods."""
    records: List[YearState] = field(default_factory=list)

    def add(self, state: YearState) -> None:
        self.records.append(state)

    def to_dicts(self) -> List[Dict[str, Any]]:
        return [state.__dict__ for state in self.records]
