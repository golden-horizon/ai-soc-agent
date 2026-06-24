import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)


async def main():
    print("=== AI SOC Agent ===")
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

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            attack = await session.call_tool(
                "soc_map_attack",
                {"incident": incident}
            )

            severity = await session.call_tool(
                "soc_calculate_severity",
                {"incident": incident}
            )

            mitre = await session.call_tool(
                "soc_map_mitre",
                {"incident": incident}
            )

            actions = await session.call_tool(
                "soc_recommend_actions",
                {"incident": incident}
            )

            print("\n=== AI SOC Analysis ===")
            print("Attack Type:", attack.content[0].text)
            print("Severity:", severity.content[0].text)
            print("MITRE ATT&CK:", mitre.content[0].text)

            print("Recommended Actions:")
            for item in actions.content:
                print("-", item.text)


asyncio.run(main())