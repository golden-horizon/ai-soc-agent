import json


def mitre_summary(filename="mcp_incident_reports.json"):
    with open(filename, "r") as file:
        reports = json.load(file)

    print("\n===== MITRE ATT&CK Summary =====")

    for report in reports:
        print(
            f"{report['attack_type']} → {report['mitre']}"
        )


if __name__ == "__main__":
    mitre_summary()