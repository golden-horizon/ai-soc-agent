from tools import analyze_incident

print("=== AI SOC Agent CLI ===")
print("Choose incident type:")
print("1. Brute Force")
print("2. SQL Injection")
print("3. XSS")
print("4. API Abuse")
print("5. Session Hijacking")

choice = input("Enter choice: ")

incident = {
    "user": input("User: "),
    "source_ip": input("Source IP: ")
}

if choice == "1":
    incident["failed_attempts"] = int(input("Failed attempts: "))

elif choice == "2":
    incident["request"] = "/login?username=admin' OR '1'='1"

elif choice == "3":
    incident["request"] = "/search?q=<script>alert(1)</script>"

elif choice == "4":
    incident["request_count"] = int(input("Request count: "))
    incident["endpoint"] = input("Endpoint: ")

elif choice == "5":
    incident["event"] = "impossible travel detected"
    incident["session_anomaly"] = True

result = analyze_incident(incident)

print("\n=== Analysis Result ===")
print("Attack Type:", result["attack_type"])
print("Severity:", result["severity"])
print("MITRE ATT&CK:", result["mitre"])
print("Reason:", result["reason"])

print("Recommended Actions:")
for action in result["recommended_actions"]:
    print("-", action)