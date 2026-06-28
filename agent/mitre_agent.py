from agent.llm_agent import LLMAgent
from mcp_tools.mitre_tools import search_mitre

class MITREAgent(LLMAgent):
    """
    Specialist agent for MITRE ATT&CK mapping.
    Returns structured MITRE data.
    """

    def map_to_mitre(self, incident: dict) -> dict:
       request = incident.get("request", "").lower()

       if "' or '1'='1" in request or "union select" in request:
          mitre_result = search_mitre("sql injection")

          return {
               "technique_id": mitre_result["technique_id"],
                "technique_name": mitre_result["technique_name"],
                "tactic": mitre_result["tactic"],
                "confidence": "High",
                "explanation": (
                "The request contains SQL injection syntax targeting a public-facing "
                "login endpoint. MITRE mapping was retrieved from the MCP-style MITRE tool."
                ),
            }

       if "<script>" in request:
        mitre_result = search_mitre("xss")

        return {
            "technique_id": mitre_result["technique_id"],
            "technique_name": mitre_result["technique_name"],
            "tactic": mitre_result["tactic"],
            "confidence": "Medium",
            "explanation": (
                "The request contains XSS-style script syntax targeting a web application. "
                "MITRE mapping was retrieved from the MCP-style MITRE tool."
            ),
        }

        return {
        "technique_id": "Unknown",
        "technique_name": "Unknown",
        "tactic": "Unknown",
        "confidence": "Low",
        "explanation": "No clear MITRE ATT&CK mapping was identified from the incident.",
    }
if __name__ == "__main__":
    agent = MITREAgent()

    test_incident = {
        "user": "guest",
        "source_ip": "103.22.55.9",
        "request": "/login?username=admin' OR '1'='1",
    }

    result = agent.map_to_mitre(test_incident)

    print("\n=== MITRE AGENT TEST ===")
    print(result)