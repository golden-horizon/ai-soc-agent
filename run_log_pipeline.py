from datetime import datetime, timezone
import json
from pathlib import Path

from collectors.collector_manager import CollectorManager
from agent.log_analysis_agent import LogAnalysisAgent
from agent.soc_manager_agent import SOCManagerAgent
from case_management.case_repository import CaseRepository
from engine.correlation_engine import CorrelationEngine
from engine.severity_escalation import SeverityEscalationEngine


def main():
    collector_manager = CollectorManager()
    log_agent = LogAnalysisAgent()
    soc_manager = SOCManagerAgent()
    repository = CaseRepository()

    logs = collector_manager.collect_logs()

    analysis_result = log_agent.analyze(logs)
    incidents = log_agent.findings_to_incidents(analysis_result)

    investigations = []

    print("\n=== LOG FINDINGS ===")
    print(f"Findings detected: {analysis_result['finding_count']}")

    print("\n=== GENERATED INCIDENTS ===")
    for index, incident in enumerate(incidents, start=1):
        print(f"{index}. {incident['attack_type']} from {incident['source_ip']}")

    print("\n=== INVESTIGATING INCIDENTS ===")

    for index, incident in enumerate(incidents, start=1):
        print(f"\n{'=' * 60}")
        print(f"INCIDENT {index}")
        print(f"{'=' * 60}")

        existing_case = CorrelationEngine.find_matching_case(
            incident,
            repository.list_cases(),
        )

        if existing_case:
            existing_case["event_count"] = existing_case.get("event_count", 1) + 1
            existing_case["last_seen"] = datetime.now(timezone.utc).isoformat()

            existing_case.setdefault("related_logs", [])
            existing_case["related_logs"].append(incident.get("raw_log", ""))

            existing_case = SeverityEscalationEngine.evaluate(existing_case)

            repository.save_case(existing_case)
            investigations.append(existing_case)

            print(f"Attack Type : {incident['attack_type']}")
            print(f"Source IP   : {incident['source_ip']}")
            print(f"User        : {incident['user']}")
            print(f"\nMatched Existing Case : {existing_case['case_id']}")
            print(f"Event Count           : {existing_case['event_count']}")
            print(f"Severity              : {existing_case.get('severity', 'unknown')}")
            print(f"Decision              : {existing_case.get('soc_decision', 'unknown')}")

            continue

        investigation = soc_manager.investigate(incident)
        investigation = SeverityEscalationEngine.evaluate(investigation)

        repository.save_case(investigation)
        investigations.append(investigation)

        print(f"Attack Type : {incident['attack_type']}")
        print(f"Source IP   : {incident['source_ip']}")
        print(f"User        : {incident['user']}")

        print(f"\nCase ID     : {investigation['case_id']}")
        print(f"Decision    : {investigation['soc_decision']}")
        print(f"Severity    : {investigation.get('severity', 'unknown')}")

    output_file = Path("reports/log_pipeline_cases.json")
    output_file.parent.mkdir(exist_ok=True)

    output_file.write_text(
        json.dumps(investigations, indent=2)
    )

    print("\n=== REPORT SAVED ===")
    print(output_file)


if __name__ == "__main__":
    main()