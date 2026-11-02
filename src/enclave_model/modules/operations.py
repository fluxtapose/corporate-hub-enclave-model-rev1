"""Municipal operations and utilities module."""

from ..config import OperationsConfig


class OperationsModule:
    """Simulates internal utilities, energy consumption, and municipal services."""

    def __init__(self, config: OperationsConfig):
        self.config = config

    def step(self, total_population: int) -> dict:
        """Calculate annual municipal operating costs, datacenter thermal recycling, and energy recovery."""
        # 1. Base human habitat electrical demand
        annual_kwh_per_person = self.config.power_kwh_per_capita_day * 365.25
        base_habitat_kwh_demand = annual_kwh_per_person * total_population

        # 2. Subterranean Datacenter & Geothermal Thermodynamic Engine
        # 1 MW = 1,000 kW * 8,760 hours/yr = 8,760,000 kWh/yr
        datacenter_annual_kwh = self.config.datacenter_mw_capacity * 1000 * 8760
        # Turbine power co-generation: ORC turbines recover a portion of dissipated thermal energy as electricity
        turbine_regenerated_kwh = datacenter_annual_kwh * self.config.turbine_electric_recovery_pct
        turbine_regenerated_value = turbine_regenerated_kwh * self.config.grid_cost_per_kwh

        # Net grid demand after turbine co-generation offset
        net_grid_kwh_demand = max(0.0, base_habitat_kwh_demand - turbine_regenerated_kwh)
        total_energy_cost = net_grid_kwh_demand * self.config.grid_cost_per_kwh

        # 3. Direct Thermodynamic Offsets (Free heat for agriculture & district residential heating)
        thermal_heating_savings = (
            self.config.agricultural_heating_offset_annual
            + self.config.district_heating_offset_annual
        )

        # 4. Regional Symbiosis & Local Distribution Partnership Balance
        # Revenue from exporting industrial steam to surrounding laundries and plants
        steam_export_revenue = self.config.regional_steam_export_revenue_annual
        # Subsidized revenue from export power to local municipal grid
        power_export_revenue = (
            self.config.regional_power_export_kwh_annual
            * self.config.regional_power_export_rate_per_kwh
        )
        # Corporate value from tax breaks, food priority, and AI optimization licensing
        ai_partnership_dividend = self.config.local_ai_partnership_dividend_annual
        total_symbiosis_inflow = steam_export_revenue + power_export_revenue + ai_partnership_dividend

        # Operational costs to subsidize local logistics chargers and fleet integration
        local_logistics_subsidy = self.config.local_logistics_subsidy_cost_annual
        net_regional_symbiosis_benefit = total_symbiosis_inflow - local_logistics_subsidy

        # 5. Municipal services (security, waste, transit, physical maintenance)
        municipal_opex = total_population * self.config.municipal_services_opex_per_capita

        return {
            "total_kwh_demand": base_habitat_kwh_demand,
            "turbine_regenerated_kwh": turbine_regenerated_kwh,
            "turbine_regenerated_value": turbine_regenerated_value,
            "net_grid_kwh_demand": net_grid_kwh_demand,
            "enclave_energy_cost": total_energy_cost,
            "thermal_heating_savings": thermal_heating_savings,
            "net_regional_symbiosis_benefit": net_regional_symbiosis_benefit,
            "steam_export_revenue": steam_export_revenue,
            "power_export_revenue": power_export_revenue,
            "ai_partnership_dividend": ai_partnership_dividend,
            "local_logistics_subsidy": local_logistics_subsidy,
            "enclave_municipal_opex": municipal_opex,
            "logistics_buffer_days": self.config.logistics_buffer_days,
        }
