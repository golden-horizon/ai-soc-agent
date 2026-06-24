import json


def load_reports(filename="mcp_incident_reports.json"):
    with open(filename, "r") as file:
        return json.load(file)


def answer_question(question):
    reports = load_reports()
    question = question.lower()

    if "critical" in question:
        critical = [r for r in reports if r["severity"] == "Critical"]
        return (
            f"There are {len(critical)} critical incidents: "
            + ", ".join(r["attack_type"] for r in critical)
        )

    if "mitre" in question:
        return "\n".join(
            f"{r['attack_type']}: {r['mitre']}"
            for r in reports
        )

    if "action" in question or "remediation" in question:
        response = []

        for r in reports:
            response.append(f"\n{r['attack_type']}:")

            for action in r["recommended_actions"]:
                response.append(f"- {action}")

        return "\n".join(response)

    if "summary" in question:
        critical_count = len(
            [r for r in reports if r["severity"] == "Critical"]
        )

        high_count = len(
            [r for r in reports if r["severity"] == "High"]
        )

        return (
            f"Total incidents: {len(reports)}. "
            f"Critical: {critical_count}. "
            f"High: {high_count}."
        )

    if "escalate" in question or "priority" in question:
        critical = [r for r in reports if r["severity"] == "Critical"]
        high = [r for r in reports if r["severity"] == "High"]

        response = ["Escalation recommendation:"]

        for r in critical:
            response.append(
                f"- Escalate immediately: {r['attack_type']} from {r['source_ip']}"
            )

        for r in high:
            response.append(
                f"- Investigate soon: {r['attack_type']} from {r['source_ip']}"
            )

        return "\n".join(response)

    return (
        "I can answer questions about critical incidents, MITRE mapping, "
        "remediation actions, summaries, and escalation recommendations."
    )


if __name__ == "__main__":
    print("=== AI SOC Assistant ===")
    question = input("Ask a SOC question: ")

    print("\nAnswer:")
    print(answer_question(question))