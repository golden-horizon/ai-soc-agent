from coordinator import summarize_reports
from incident_analyzer_agent import analyze_reports
from mitre_agent import mitre_summary
from remediation_agent import remediation_summary
from threat_intel_agent import threat_intel_summary
from report_agent import generate_final_report


def run_supervisor():
    print("\n===== AI SOC SUPERVISOR AGENT =====")

    summarize_reports()
    analyze_reports()
    mitre_summary()
    threat_intel_summary()
    remediation_summary()
    generate_final_report()

    print("\nSupervisor completed all SOC workflows.")


if __name__ == "__main__":
    run_supervisor()