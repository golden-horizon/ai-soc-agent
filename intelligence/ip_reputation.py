from mcp_tools.threat_intel_tools import lookup_ip_reputation


def check_ip_reputation(ip: str) -> dict:
    return lookup_ip_reputation(ip)