import json


def generate_final_report(filename="mcp_incident_reports.json"):
    with open(filename, "r") as file:
        reports = json.load(file)

    with open("final_soc_report.txt", "w") as report_file:
        report_file.write("===== FINAL SOC REPORT =====\n\n")
        report_file.write(f"Total Incidents: {len(reports)}\n\n")

        for report in reports:
            report_file.write(f"Report ID: {report['report_id']}\n")
            report_file.write(f"Attack Type: {report['attack_type']}\n")
            report_file.write(f"Severity: {report['severity']}\n")
            report_file.write(f"MITRE: {report['mitre']}\n")
            report_file.write("Recommended Actions:\n")

            for action in report["recommended_actions"]:
                report_file.write(f"- {action}\n")

            report_file.write("\n" + "-" * 40 + "\n\n")

    print("Final SOC report saved to final_soc_report.txt")


if __name__ == "__main__":
    generate_final_report()
