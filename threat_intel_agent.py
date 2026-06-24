import json


def threat_intel_summary(filename="mcp_incident_reports.json"):
    with open(filename, "r") as file:
        reports = json.load(file)

    print("\n===== Threat Intelligence Agent =====")

    suspicious_ips = set()

    for report in reports:
        suspicious_ips.add(report["source_ip"])

    print("\nObserved Source IPs:")

    for ip in suspicious_ips:
        print("-", ip)

    critical = [
        report for report in reports
        if report["severity"] == "Critical"
    ]

    print(f"\nCritical incidents detected: {len(critical)}")

    if len(critical) > 0:
        print("Recommendation: Escalate to Tier-2 SOC analyst")
    else:
        print("Recommendation: Continue monitoring")


if __name__ == "__main__":
    threat_intel_summary()