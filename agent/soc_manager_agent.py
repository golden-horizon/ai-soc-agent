from agent.display import app_header, success, agent_panel, incident_summary
from agent.mitre_agent import MITREAgent
from agent.threat_intel_agent import ThreatIntelAgent
from agent.remediation_agent import RemediationAgent


class SOCManagerAgent:
    """
    Orchestrates specialist agents and combines their outputs.
    """

    def __init__(self):
        self.mitre_agent = MITREAgent()
        self.threat_intel_agent = ThreatIntelAgent()
        self.remediation_agent = RemediationAgent()

    def investigate(self, incident: dict) -> dict:
        mitre_result = self.mitre_agent.map_to_mitre(incident)
        threat_result = self.threat_intel_agent.analyze_threat_intel(incident)
        remediation_result = self.remediation_agent.recommend_actions(incident)

        return {
            "incident": incident,
            "mitre_analysis": mitre_result,
            "threat_intelligence": threat_result,
            "remediation": remediation_result,
        }


if __name__ == "__main__":
    app_header()

    test_incident = {
        "user": "guest",
        "source_ip": "103.22.55.9",
        "request": "/login?username=admin' OR '1'='1",
    }

    incident_summary(test_incident)

    manager = SOCManagerAgent()
    result = manager.investigate(test_incident)

    success("Multi-agent investigation completed")

    agent_panel("MITRE Agent", result["mitre_analysis"])
    agent_panel("Threat Intel Agent", result["threat_intelligence"])
    agent_panel("Remediation Agent", result["remediation"])