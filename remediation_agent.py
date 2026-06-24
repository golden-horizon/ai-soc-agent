import json


def remediation_summary(filename="mcp_incident_reports.json"):
    with open(filename, "r") as file:
        reports = json.load(file)

    print("\n===== Recommended Actions =====")

    for report in reports:
        print(f"\n{report['attack_type']}:")

        for action in report["recommended_actions"]:
            print("-", action)


if __name__ == "__main__":
    remediation_summary()