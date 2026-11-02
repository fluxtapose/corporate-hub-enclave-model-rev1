"""Main discrete-time simulation engine for Corporate Hub Enclaves."""

from .config import EnclaveConfig
from .core.state import YearState, SimulationHistory
from .modules.demographics import DemographicsModule
from .modules.housing import HousingModule
from .modules.operations import OperationsModule
from .modules.economy import EconomyModule


class EnclaveSimulation:
    """Orchestrates multi-year discrete step simulation of an enclave."""

    def __init__(self, config: EnclaveConfig):
        self.config = config
        self.demographics = DemographicsModule(config.demographics)
        self.housing = HousingModule(config.housing)
        self.operations = OperationsModule(config.operations)
        self.economy = EconomyModule(config.economy)
        self.history = SimulationHistory()

    def run(self) -> SimulationHistory:
        """Run the simulation across the configured number of years."""
        cumulative_savings = 0.0
        cumulative_telemetry_value = 0.0
        cumulative_enterprise_surplus = 0.0

        for year in range(1, self.config.simulation_years + 1):
            # Step 1: Demographics
            demo_out = self.demographics.step(year)

            # Step 2: Housing demand (workers + contractors)
            households_needed = demo_out["workforce"] + demo_out["contractors"]
            housing_out = self.housing.step(households_needed)

            # Step 3: Operations & Utilities
            ops_out = self.operations.step(demo_out["total_population"])

            # Step 4: Economy balance sheet
            econ_out = self.economy.step(
                workforce=demo_out["workforce"],
                total_population=demo_out["total_population"],
                baseline_turnover_heads=demo_out["baseline_turnover_heads"],
                enclave_turnover_heads=demo_out["enclave_turnover_heads"],
                amortized_housing_capex=housing_out["amortized_housing_capex"],
                facility_maintenance_cost=housing_out["facility_maintenance_cost"],
                enclave_municipal_opex=ops_out["enclave_municipal_opex"],
                enclave_energy_cost=ops_out["enclave_energy_cost"],
                net_regional_symbiosis_benefit=ops_out["net_regional_symbiosis_benefit"],
            )

            cumulative_savings += econ_out["net_annual_savings"]
            cumulative_telemetry_value += econ_out["total_plus_a_telemetry_value"]
            cumulative_enterprise_surplus += econ_out["total_enterprise_economic_surplus"]

            # Record State
            state = YearState(
                year=year,
                workforce=demo_out["workforce"],
                dependents=demo_out["dependents"],
                contractors=demo_out["contractors"],
                total_population=demo_out["total_population"],
                births=demo_out["births"],
                deaths=demo_out["deaths"],
                assimilation_quota=demo_out["assimilation_quota"],
                carrying_headroom=demo_out["carrying_headroom"],
                total_housing_units=housing_out["total_housing_units"],
                occupied_units=housing_out["occupied_units"],
                occupancy_rate=housing_out["occupancy_rate"],
                enclave_payroll=econ_out["enclave_payroll"],
                universal_baseline_cost=econ_out["universal_baseline_cost"],
                total_credits_issued=econ_out["total_credits_issued"],
                net_credit_subsystem_cost=econ_out["net_credit_subsystem_cost"],
                total_exit_settlement_cost=econ_out["total_exit_settlement_cost"],
                enclave_municipal_opex=ops_out["enclave_municipal_opex"],
                enclave_energy_cost=ops_out["enclave_energy_cost"],
                turbine_regenerated_value=ops_out["turbine_regenerated_value"],
                thermal_heating_savings=ops_out["thermal_heating_savings"],
                net_regional_symbiosis_benefit=ops_out["net_regional_symbiosis_benefit"],
                amortized_housing_capex=housing_out["amortized_housing_capex"],
                facility_maintenance_cost=housing_out["facility_maintenance_cost"],
                total_enclave_cost=econ_out["total_enclave_cost"],
                baseline_payroll=econ_out["baseline_payroll"],
                baseline_office_lease=econ_out["baseline_office_lease"],
                baseline_turnover_cost=econ_out["baseline_turnover_cost"],
                total_baseline_cost=econ_out["total_baseline_cost"],
                net_annual_savings=econ_out["net_annual_savings"],
                cumulative_net_savings=cumulative_savings,
                total_plus_a_telemetry_value=econ_out["total_plus_a_telemetry_value"],
                cumulative_plus_a_telemetry_value=cumulative_telemetry_value,
                total_enterprise_economic_surplus=econ_out["total_enterprise_economic_surplus"],
                cumulative_enterprise_surplus=cumulative_enterprise_surplus,
                turnover_rate=demo_out["turnover_rate"],
                retained_workers_delta=demo_out["retained_workers_delta"],
            )
            self.history.add(state)

        return self.history
