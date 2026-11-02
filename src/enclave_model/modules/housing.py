"""Housing and spatial infrastructure module."""

from ..config import HousingConfig


class HousingModule:
    """Simulates physical housing units, occupancy constraints, and capital costs."""

    def __init__(self, config: HousingConfig):
        self.config = config
        self.total_units = config.initial_units

    def step(self, total_households_needed: int) -> dict:
        """Calculate spatial usage and annual capital/maintenance expenses.

        Each worker or contractor household typically maps to a living unit.
        """
        # Automatically expand units if occupancy demand exceeds 90%
        if total_households_needed > (self.total_units * 0.90):
            units_to_add = min(
                int(round(total_households_needed * 0.20)),
                self.config.max_capacity_units - self.total_units,
            )
            if units_to_add > 0:
                self.total_units += units_to_add

        occupied_units = min(total_households_needed, self.total_units)
        occupancy_rate = occupied_units / max(1, self.total_units)

        # Asset valuation & capital depreciation
        total_asset_value = self.total_units * self.config.capex_per_unit
        annual_amortized_capex = total_asset_value / self.config.capex_amortization_years
        annual_maintenance_cost = total_asset_value * self.config.annual_maintenance_pct

        return {
            "total_housing_units": self.total_units,
            "occupied_units": occupied_units,
            "occupancy_rate": occupancy_rate,
            "total_asset_value": total_asset_value,
            "amortized_housing_capex": annual_amortized_capex,
            "facility_maintenance_cost": annual_maintenance_cost,
        }
