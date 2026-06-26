from agent.llm_agent import LLMAgent


class MITREAgent(LLMAgent):
    """
    AI specialist responsible only for MITRE ATT&CK mapping.
    """

    def map_to_mitre(self, incident: dict) -> str:
        prompt = f"""
You are a MITRE ATT&CK specialist.

Your only responsibility is to identify the SINGLE BEST MITRE ATT&CK technique.

Rules:

- Never invent MITRE IDs.
- Return only ONE technique.
- Do not discuss remediation.
- Do not discuss CVEs.
- Do not discuss business impact.
- For SQL Injection, login bypass attempts, public web endpoint attacks, or malicious web requests, prefer:
  T1190 - Exploit Public-Facing Application
  Tactic: Initial Access
- Do not use API Abuse unless the incident clearly shows API misuse, excessive API calls, or abuse of API authentication.
- Do not invent sub-techniques such as T1018.006.
- If the incident is a web login attack with SQL injection syntax, map it to T1190.

Mapping hints:

- SQL Injection
  -> T1190 - Exploit Public-Facing Application
  -> Tactic: Initial Access

- Cross-Site Scripting (XSS)
  -> T1059 - Command and Scripting Interpreter
  (Low confidence if uncertain)

- Brute Force Login
  -> T1110 - Brute Force

- Session Hijacking
  -> T1185 - Browser Session Hijacking

- API Abuse
  -> Choose the closest ATT&CK technique and explain why.

Incident:

{incident}

Return ONLY:

1. Technique ID:
2. Technique Name:
3. Tactic:
4. Why this mapping fits:
5. Confidence:
"""

        return self.ask_llm(prompt)


if __name__ == "__main__":

    agent = MITREAgent()

    test_incident = {
        "attack_type": "SQL Injection",
        "request": "/login?username=admin' OR '1'='1",
        "source_ip": "103.22.55.9",
        "user": "guest",
    }

    result = agent.map_to_mitre(test_incident)

    print("\n=== MITRE AGENT TEST ===\n")
    print(result)