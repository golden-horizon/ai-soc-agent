import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from models import IncidentReport


server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)


async def main():
    with open("sample_incidents.json", "r") as file:
        incidents = json.load(file)

    reports = []

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            for index, incident in enumerate(incidents, start=1):
                attack = await session.call_tool("soc_map_attack", {"incident": incident})
                severity = await session.call_tool("soc_calculate_severity", {"incident": incident})
                mitre = await session.call_tool("soc_map_mitre", {"incident": incident})
                actions = await session.call_tool("soc_recommend_actions", {"incident": incident})

                report = IncidentReport(
                    report_id=f"MCP-{index:03}",
                    user=incident.get("user", "N/A"),
                    source_ip=incident.get("source_ip", "N/A"),
                    attack_type=attack.content[0].text,
                    severity=severity.content[0].text,
                    mitre=mitre.content[0].text,
                    reason="Generated through MCP SOC tools.",
                    recommended_actions=[item.text for item in actions.content]
                )

                reports.append(report.model_dump())

    with open("mcp_incident_reports.json", "w") as file:
        json.dump(reports, file, indent=4)

    print("MCP incident reports saved to mcp_incident_reports.json")


asyncio.run(main())