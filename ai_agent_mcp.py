import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)


async def main():
    print("=== AI SOC Agent + MCP ===")

    incident_text = input("Paste incident text: ")

    incident = {
        "raw_text": incident_text,
        "failed_attempts": 8 if "failed" in incident_text.lower() else 0
    }

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            attack = await session.call_tool("soc_map_attack", {"incident": incident})
            severity = await session.call_tool("soc_calculate_severity", {"incident": incident})
            mitre = await session.call_tool("soc_map_mitre", {"incident": incident})
            actions = await session.call_tool("soc_recommend_actions", {"incident": incident})

            report = {
                "attack_type": attack.content[0].text,
                "severity": severity.content[0].text,
                "mitre": mitre.content[0].text,
                "reason": "Generated through MCP SOC tools.",
                "recommended_actions": [item.text for item in actions.content]
            }

            print(json.dumps(report, indent=4))


asyncio.run(main())