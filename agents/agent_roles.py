AGENT_ROLES = {
    "log_collection_agent": {
        "name": "Log Collection Agent",
        "job": "Collects and normalizes security events from multiple sources.",
    },
    "detection_agent": {
        "name": "Detection Agent",
        "job": "Analyzes logs and identifies suspicious activity using detection rules.",
    },
    "mitre_attack_agent": {
        "name": "MITRE ATT&CK Agent",
        "job": "Maps incidents to MITRE ATT&CK techniques and adversary behavior context.",
    },
    "threat_intelligence_agent": {
        "name": "Threat Intelligence Agent",
        "job": "Enriches incidents with IP reputation, country attribution, and threat score.",
    },
    "correlation_agent": {
        "name": "Correlation Agent",
        "job": "Groups related events into cases using attack type, source IP, and user.",
    },
    "severity_escalation_agent": {
        "name": "Severity Escalation Agent",
        "job": "Escalates recurring or high-risk incidents based on event count and severity.",
    },
    "case_management_agent": {
        "name": "Case Management Agent",
        "job": "Creates, updates, searches, and tracks investigation cases.",
    },
    "investigation_agent": {
        "name": "Investigation Agent",
        "job": "Produces final analyst-facing investigation output.",
    },
}