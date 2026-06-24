import json


def summarize_reports(filename="mcp_incident_reports.json"):
    with open(filename, "r") as file:
        reports = json.load(file)

    print("\n===== SOC Executive Summary =====")
    print("Total Incidents:", len(reports))

    severity_counts = {}

    for report in reports:
        severity = report["severity"]
        severity_counts[severity] = severity_counts.get(severity, 0) + 1

    print("\nSeverity Distribution:")
    for severity, count in severity_counts.items():
        print(f"{severity}: {count}")

    print("\nAttack Types:")
    for report in reports:
        print("-", report["attack_type"])


if __name__ == "__main__":
    summarize_reports()