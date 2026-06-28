MITRE_DATABASE = {
    "sql injection": {
        "technique_id": "T1190",
        "technique_name": "Exploit Public-Facing Application",
        "tactic": "Initial Access",
    },

    "brute force": {
        "technique_id": "T1110",
        "technique_name": "Brute Force",
        "tactic": "Credential Access",
    },

    "session hijacking": {
        "technique_id": "T1185",
        "technique_name": "Browser Session Hijacking",
        "tactic": "Collection",
    },

    "xss": {
        "technique_id": "T1059",
        "technique_name": "Command and Scripting Interpreter",
        "tactic": "Execution",
    },

    "api abuse": {
        "technique_id": "T1190",
        "technique_name": "Exploit Public-Facing Application",
        "tactic": "Initial Access",
    },
}


def search_mitre(attack_pattern: str) -> dict:
    return MITRE_DATABASE.get(
        attack_pattern.lower(),
        {
            "technique_id": "Unknown",
            "technique_name": "Unknown",
            "tactic": "Unknown",
        },
    )


if __name__ == "__main__":
    result = search_mitre("sql injection")

    print("\n=== MCP MITRE TOOL TEST ===")
    print(result)