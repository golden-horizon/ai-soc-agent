import sys
from datetime import datetime, timezone

from rich.console import Console

from case_management.case_repository import CaseRepository


console = Console()

VALID_STATUSES = ["Open", "In Progress", "Resolved", "Closed", "Reopened"]


def update_case_status(case_id: str, new_status: str) -> None:
    repository = CaseRepository()
    case = repository.get_case(case_id)

    if not case:
        console.print(f"[bold red]Case not found:[/bold red] {case_id}")
        return

    if new_status not in VALID_STATUSES:
        console.print("[bold red]Invalid status[/bold red]")
        console.print(f"Valid statuses: {', '.join(VALID_STATUSES)}")
        return

    old_status = case.get("status", "Unknown")
    update_time = datetime.now(timezone.utc).isoformat()

    case["status"] = new_status
    case["status_updated_at"] = update_time

    case.setdefault("timeline", [])
    case["timeline"].append(
        {
            "time": update_time,
            "event": f"Status changed from {old_status} to {new_status}",
        }
    )

    repository.save_case(case)

    console.print(f"[bold green]Case status updated:[/bold green] {case_id}")
    console.print(f"[cyan]Old Status:[/cyan] {old_status}")
    console.print(f"[cyan]New Status:[/cyan] {new_status}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        console.print(
            '[yellow]Usage:[/yellow] python -m case_management.case_update CASE-ID "In Progress"'
        )
    else:
        case_id = sys.argv[1]
        new_status = " ".join(sys.argv[2:])

        update_case_status(case_id, new_status)