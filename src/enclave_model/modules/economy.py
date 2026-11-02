"""Economic model comparing enclave operations vs. traditional distributed enterprise."""

from ..config import EconomyConfig


class EconomyModule:
    """Computes labor costs, amenity packages, real estate offsets, and net balance sheet."""

    def __init__(self, config: EconomyConfig):
        self.config = config

    def step(
        self,
        workforce: int,
        total_population: int,
        baseline_turnover_heads: int,
        enclave_turnover_heads: int,
        amortized_housing_capex: float,
        facility_maintenance_cost: float,
        enclave_municipal_opex: float,
        enclave_energy_cost: float,
        net_regional_symbiosis_benefit: float = 0.0,
    ) -> dict:
        """Evaluate annual balance sheet for Enclave vs. Traditional Baseline."""

        # --- 1. Traditional Distributed Model (Baseline Counterfactual) ---
        baseline_payroll = workforce * self.config.traditional_avg_cash_salary
        baseline_office_lease = workforce * self.config.traditional_office_lease_per_head
        turnover_cost_per_head = (
            self.config.traditional_avg_cash_salary * self.config.replacement_cost_pct_salary
        )
        baseline_turnover_cost = baseline_turnover_heads * turnover_cost_per_head
        total_baseline_cost = baseline_payroll + baseline_office_lease + baseline_turnover_cost

        # --- 2. Enclave Hub Model ---
        enclave_payroll = workforce * self.config.enclave_avg_cash_salary
        
        # Universal baseline floor (Tier 0: food, clean water, medical, automated logistics)
        universal_baseline_cost = (
            total_population * self.config.universal_baseline_per_capita
        )

        # Internal Credit Economy (Tier 1: discretionary goods, luxury amenities, upgrades)
        total_credits_issued = workforce * self.config.annual_credits_issued_per_worker
        # Net corporate cost for providing discretionary items minus closed-loop internal recovery
        net_credit_subsystem_cost = total_credits_issued * (
            1.0 - self.config.internal_credit_burn_recovery_pct
        )

        # Reduced onboarding friction
        enclave_turnover_cost = (
            enclave_turnover_heads
            * turnover_cost_per_head
            * (1.0 - self.config.recruitment_savings_factor)
        )

        # Separation and Exit Settlements:
        # 1. Converted credit payout at lower-end market rate
        credit_payout_per_exit = (
            self.config.avg_unredeemed_credit_balance_at_exit
            * self.config.credit_exit_conversion_rate
        )
        # 2. Standard unemployment equivalent severance
        statutory_severance_per_exit = (
            self.config.severance_weeks_unemployment_equiv
            * self.config.standard_weekly_unemployment_benefit
        )
        total_exit_settlement_per_head = credit_payout_per_exit + statutory_severance_per_exit
        total_exit_settlement_cost = enclave_turnover_heads * total_exit_settlement_per_head

        total_enclave_cost = (
            enclave_payroll
            + universal_baseline_cost
            + net_credit_subsystem_cost
            + enclave_municipal_opex
            + enclave_energy_cost
            + amortized_housing_capex
            + facility_maintenance_cost
            + enclave_turnover_cost
            + total_exit_settlement_cost
            - net_regional_symbiosis_benefit
        )

        net_annual_savings = total_baseline_cost - total_enclave_cost

        # +a Telemetry Valuation (Proprietary AI Training & RLHF Value)
        expert_telemetry_value = (
            workforce
            * self.config.telemetry_expert_hours_per_worker_annual
            * self.config.telemetry_hourly_market_value
            * self.config.telemetry_frontier_ai_multiplier
        )
        biometric_telemetry_value = total_population * self.config.biometric_health_telemetry_value_per_capita
        total_plus_a_telemetry_value = expert_telemetry_value + biometric_telemetry_value

        # Comprehensive economic surplus including +a asset creation
        total_enterprise_economic_surplus = net_annual_savings + total_plus_a_telemetry_value

        return {
            "baseline_payroll": baseline_payroll,
            "baseline_office_lease": baseline_office_lease,
            "baseline_turnover_cost": baseline_turnover_cost,
            "total_baseline_cost": total_baseline_cost,
            "enclave_payroll": enclave_payroll,
            "universal_baseline_cost": universal_baseline_cost,
            "total_credits_issued": total_credits_issued,
            "net_credit_subsystem_cost": net_credit_subsystem_cost,
            "enclave_turnover_cost": enclave_turnover_cost,
            "total_exit_settlement_cost": total_exit_settlement_cost,
            "credit_payout_per_exit": credit_payout_per_exit,
            "statutory_severance_per_exit": statutory_severance_per_exit,
            "net_regional_symbiosis_benefit": net_regional_symbiosis_benefit,
            "total_enclave_cost": total_enclave_cost,
            "net_annual_savings": net_annual_savings,
            "total_plus_a_telemetry_value": total_plus_a_telemetry_value,
            "total_enterprise_economic_surplus": total_enterprise_economic_surplus,
        }
