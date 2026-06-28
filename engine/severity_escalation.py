class SeverityEscalationEngine:
    """
    Escalates cases based on repeated activity.
    """

    @staticmethod
    def evaluate(case: dict) -> dict:
        event_count = case.get("event_count", 1)
        current_decision = case.get("soc_decision", "Monitor")

        if event_count >= 20:
            case["severity"] = "Critical"
            case["soc_decision"] = "Escalate Immediately"
            case["escalation_reason"] = (
                f"High recurrence detected: {event_count} related events."
            )

        elif event_count >= 10:
            case["severity"] = "High"
            case["soc_decision"] = "Investigate Within 15 Minutes"
            case["escalation_reason"] = (
                f"Repeated suspicious activity detected: {event_count} related events."
            )

        else:
            case["severity"] = case.get("severity", "Medium")
            case["soc_decision"] = current_decision
            case["escalation_reason"] = case.get(
                "escalation_reason",
                "No escalation threshold reached.",
            )

        return case


if __name__ == "__main__":
    test_case = {
        "case_id": "CASE-TEST",
        "event_count": 24,
        "soc_decision": "Investigate Within 15 Minutes",
    }

    result = SeverityEscalationEngine.evaluate(test_case)

    print("\n=== SEVERITY ESCALATION TEST ===")
    print(result)