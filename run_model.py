"""CLI simulation entrypoint for Corporate Hub Enclave Model (C-HEM)."""

import sys
import os
import csv

# Ensure src is in Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from enclave_model import EnclaveSimulation, get_scenario, list_scenarios


def format_currency(val: float) -> str:
    """Format numbers into human-readable millions/thousands."""
    if abs(val) >= 1_000_000:
        return f"${val / 1_000_000:,.1f}M"
    if abs(val) >= 1_000:
        return f"${val / 1_000:,.0f}K"
    return f"${val:,.0f}"


def run_and_report(scenario_key: str, export_rows: list = None):
    """Execute a single scenario and print a structured summary table."""
    config = get_scenario(scenario_key)
    sim = EnclaveSimulation(config)
    history = sim.run()

    print("\n" + "=" * 115)
    print(f"  SCENARIO: {config.name}")
    print(f"  Horizon: {config.simulation_years} Years | Baseline Turnover: {config.demographics.external_turnover_rate*100:.0f}%")
    print("=" * 115)
    print(
        f"{'Year':<5} | {'Workforce':<10} | {'Total Pop':<10} | {'Occupancy':<10} | "
        f"{'Enclave Cost':<13} | {'Baseline Cost':<14} | {'Net Savings':<12} | {'+a Telemetry':<13} | {'Total Surplus':<13}"
    )
    print("-" * 115)

    for state in history.records:
        print(
            f"{state.year:<5} | "
            f"{state.workforce:<10,d} | "
            f"{state.total_population:<10,d} | "
            f"{state.occupancy_rate*100:>8.1f}% | "
            f"{format_currency(state.total_enclave_cost):<13} | "
            f"{format_currency(state.total_baseline_cost):<14} | "
            f"{format_currency(state.net_annual_savings):<12} | "
            f"{format_currency(state.total_plus_a_telemetry_value):<13} | "
            f"{format_currency(state.total_enterprise_economic_surplus):<13}"
        )
        if export_rows is not None:
            row = state.__dict__.copy()
            row["scenario"] = config.name
            row["scenario_key"] = scenario_key
            export_rows.append(row)

    print("-" * 115)
    final = history.records[-1]
    total_retained = sum(s.retained_workers_delta for s in history.records)
    print(
        f"10-Yr Tangible Net Savings: {format_currency(final.cumulative_net_savings)} | "
        f"10-Yr +a Telemetry Inflow: {format_currency(final.cumulative_plus_a_telemetry_value)} | "
        f"Total Enterprise Surplus: {format_currency(final.cumulative_enterprise_surplus)}"
    )
    print(f"Retained Talent vs External Market: +{total_retained:,d} workers")
    print("=" * 115 + "\n")


def export_to_csv(rows: list, output_path: str):
    """Export annual simulation runs to a CSV file for analysis in Excel."""
    if not rows:
        return
    fieldnames = ["scenario", "scenario_key"] + [k for k in rows[0].keys() if k not in ("scenario", "scenario_key")]
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Exported detailed scenario models to: {output_path}")


def main():
    print("Running Corporate Hub Enclave Model (C-HEM)...")
    scenarios = list_scenarios()
    export_rows = []
    for sc in scenarios:
        run_and_report(sc, export_rows)

    csv_path = os.path.join(os.path.dirname(__file__), "enclave_scenarios_output.csv")
    export_to_csv(export_rows, csv_path)


if __name__ == "__main__":
    main()
