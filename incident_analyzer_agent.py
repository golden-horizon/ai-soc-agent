import json


def analyze_reports(filename="mcp_incident_reports.json"):
    with open(filename, "r") as file:
        reports = json.load(file)

    print("\n===== Incident Analyzer Agent =====")

    for report in reports:
        print(f"\nReport ID: {report['report_id']}")
        print(f"Attack Type: {report['attack_type']}")
        print(f"Severity: {report['severity']}")
        print(f"Reason: {report['reason']}")

        if report["severity"] == "Critical":
            print("Priority: Immediate response required")
        elif report["severity"] == "High":
            print("Priority: Investigate as soon as possible")
        else:
            print("Priority: Monitor")


if __name__ == "__main__":
    analyze_reports()