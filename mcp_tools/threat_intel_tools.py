IP_REPUTATION_DATABASE = {
    "103.22.55.9": {
        "reputation": "malicious",
        "confidence": 95,
        "reason": "Known web attack source in sample threat intel",
    },

    "45.83.12.10": {
        "reputation": "malicious",
        "confidence": 90,
        "reason": "Repeated brute force activity observed",
    },

    "88.12.44.7": {
        "reputation": "suspicious",
        "confidence": 70,
        "reason": "Associated with XSS scanning activity",
    },
}


def lookup_ip_reputation(ip: str) -> dict:

    if ip in IP_REPUTATION_DATABASE:
        return {
            "found": True,
            "ip": ip,
            **IP_REPUTATION_DATABASE[ip],
        }

    return {
        "found": False,
        "ip": ip,
        "reputation": "unknown",
        "confidence": 0,
        "reason": "No reputation data found",
    }


if __name__ == "__main__":

    result = lookup_ip_reputation("103.22.55.9")

    print("\n=== IP REPUTATION TEST ===")
    print(result)