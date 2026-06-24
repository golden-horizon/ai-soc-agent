from coordinator import summarize_reports
from mitre_agent import mitre_summary
from remediation_agent import remediation_summary
from incident_analyzer_agent import analyze_reports
from report_agent import generate_final_report


print("\n=== RUNNING AI SOC MULTI-AGENT SYSTEM ===")

summarize_reports()
analyze_reports()
mitre_summary()
remediation_summary()
generate_final_report()

print("\nAll SOC agents completed successfully.")