"""Pre-configured scenario definitions for exploration."""

from typing import Dict, List
from .config import (
    EnclaveConfig,
    DemographicsConfig,
    HousingConfig,
    EconomyConfig,
    OperationsConfig,
)


def get_baseline_scenario() -> EnclaveConfig:
    """Standard balanced corporate arcology."""
    return EnclaveConfig(name="Tech Monolith Arcology (Baseline)")


def get_hyper_dense_scenario() -> EnclaveConfig:
    """High-density computational campus with high energy demand and young demographic."""
    return EnclaveConfig(
        name="High-Density Autonomous Tech Hub",
        demographics=DemographicsConfig(
            initial_workforce=4000,
            dependent_ratio=0.20,
            contractor_ratio=0.10,
            enclave_retention_bonus=0.60,  # 60% turnover reduction
        ),
        housing=HousingConfig(
            initial_units=5000,
            capex_per_unit=210_000.0,  # Modular compact micro-studios
        ),
        operations=OperationsConfig(
            power_kwh_per_capita_day=45.0,  # Higher on-site datacenter / compute loads
            grid_cost_per_kwh=0.09,
        ),
    )


def get_family_first_scenario() -> EnclaveConfig:
    """Family-centric enclave with schooling, spacious units, and high quality of life."""
    return EnclaveConfig(
        name="Family-Centric Suburban Eco-Enclave",
        demographics=DemographicsConfig(
            initial_workforce=1800,
            dependent_ratio=0.85,  # High proportion of children/partners
            contractor_ratio=0.20,
            enclave_retention_bonus=0.70,  # Very high stickiness for families
        ),
        housing=HousingConfig(
            initial_units=3000,
            capex_per_unit=390_000.0,  # Larger multi-room townhomes / suites
        ),
        economy=EconomyConfig(
            universal_baseline_per_capita=22_000.0,  # Expanded family baseline: pediatric care & schooling
            annual_credits_issued_per_worker=20_000.0,
        ),
    )


SCENARIOS: Dict[str, EnclaveConfig] = {
    "baseline": get_baseline_scenario(),
    "hyper_dense": get_hyper_dense_scenario(),
    "family_first": get_family_first_scenario(),
}


def list_scenarios() -> List[str]:
    """Return available scenario identifiers."""
    return list(SCENARIOS.keys())


def get_scenario(name: str) -> EnclaveConfig:
    """Retrieve scenario by key, defaulting to baseline."""
    return SCENARIOS.get(name, get_baseline_scenario())
