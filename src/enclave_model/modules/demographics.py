"""Demographics and population dynamics module with logarithmic carrying capacity governor."""

import math
from ..config import DemographicsConfig


class DemographicsModule:
    """Simulates workforce growth, vital dynamics, logarithmic carrying capacity, and retention."""

    def __init__(self, config: DemographicsConfig):
        self.config = config
        self.workforce = config.initial_workforce

    def step(self, year: int) -> dict:
        """Advance demographic state by one year using pre-assimilation vital calculation."""
        # 1. Base external turnover vs enclave turnover with AI telemetry burnout optimization
        baseline_turnover_rate = self.config.external_turnover_rate
        effective_retention_bonus = min(
            0.90,
            self.config.enclave_retention_bonus
            + (self.config.ai_telemetry_burnout_reduction * self.config.wearable_compliance_rate)
        )
        enclave_turnover_rate = baseline_turnover_rate * (1.0 - effective_retention_bonus)

        baseline_turnover_heads = int(round(self.workforce * baseline_turnover_rate))
        enclave_turnover_heads = int(round(self.workforce * enclave_turnover_rate))
        retained_delta = baseline_turnover_heads - enclave_turnover_heads

        # 2. Vital Dynamics: Calculate internal births and deaths BEFORE external assimilation
        # Total population baseline prior to year adjustments
        est_prior_pop = int(round(self.workforce * (1.0 + self.config.dependent_ratio + self.config.contractor_ratio)))
        births = int(round(est_prior_pop * self.config.annual_birth_rate))
        deaths = int(round(est_prior_pop * self.config.annual_death_rate))

        # 3. Logarithmic Carrying Capacity Governor for Workforce Intake
        # K = Carrying capacity limit for workforce
        K = self.config.carrying_capacity_workforce
        
        # After turnover separations, how many workers remain:
        retained_workers = self.workforce - enclave_turnover_heads
        
        # Available headroom before assimilation
        headroom = max(0, K - retained_workers)
        
        if year > 1 and headroom > 0:
            # Logarithmic dampening: growth = r * workforce * ln(1 + headroom / K)
            # When headroom is large (H/K ~ 1), ln(2) = 0.693
            # As headroom approaches 0, ln(1 + e) -> 0
            log_factor = math.log(1.0 + (headroom / K))
            target_growth_heads = int(round(self.workforce * self.config.target_annual_growth * log_factor))
            
            # Net assimilation quota cannot exceed available carrying capacity headroom
            assimilation_quota = min(headroom, max(0, target_growth_heads + enclave_turnover_heads))
            self.workforce = retained_workers + assimilation_quota
        elif year > 1 and headroom <= 0:
            # Absolute capacity saturated: zero external intake
            assimilation_quota = 0
            self.workforce = min(self.workforce, K)
        else:
            assimilation_quota = 0

        dependents = int(round(self.workforce * self.config.dependent_ratio))
        contractors = int(round(self.workforce * self.config.contractor_ratio))
        total_population = self.workforce + dependents + contractors

        return {
            "workforce": self.workforce,
            "dependents": dependents,
            "contractors": contractors,
            "total_population": total_population,
            "births": births,
            "deaths": deaths,
            "assimilation_quota": assimilation_quota,
            "carrying_capacity_workforce": K,
            "carrying_headroom": max(0, K - self.workforce),
            "turnover_rate": enclave_turnover_rate,
            "retained_workers_delta": retained_delta,
            "baseline_turnover_heads": baseline_turnover_heads,
            "enclave_turnover_heads": enclave_turnover_heads,
        }
