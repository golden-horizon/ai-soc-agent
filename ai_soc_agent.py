import json

with open("mcp_incident_reports.json", "r") as file:
    reports = json.load(file)

print("\n========== AI SOC AGENT ==========\n")

print(f"Total Incidents: {len(reports)}")

critical_count = sum(
    1 for report in reports
    if report["severity"].lower() == "critical"
)

high_count = sum(
    1 for report in reports
    if report["severity"].lower() == "high"
)

print(f"Critical Incidents: {critical_count}")
print(f"High Incidents: {high_count}")

print("\n===== Incident Summary =====\n")

for report in reports:
    print(f"Report ID: {report['report_id']}")
    print(f"Attack Type: {report['attack_type']}")
    print(f"Severity: {report['severity']}")
    print(f"MITRE ATT&CK: {report['mitre']}")

    print("Recommended Actions:")
    for action in report["recommended_actions"]:
        print("-", action)

    print("-" * 40)