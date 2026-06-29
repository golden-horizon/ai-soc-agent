import sys
from datetime import datetime, timezone

from rich.console import Console

from case_management.case_repository import CaseRepository


console = Console()


def add_note(case_id: str, note_text: str, analyst: str = "Navid") -> None:
    repository = CaseRepository()
    case = repository.get_case(case_id)

    if not case:
        console.print(f"[bold red]Case not found:[/bold red] {case_id}")
        return

    note = {
        "time": datetime.now(timezone.utc).isoformat(),
        "analyst": analyst,
        "note": note_text,
    }

    case.setdefault("analyst_notes", [])
    case["analyst_notes"].append(note)

    case.setdefault("timeline", [])
    case["timeline"].append(
        {
            "time": note["time"],
            "event": f"Analyst note added by {analyst}",
        }
    )

    repository.save_case(case)

    console.print(f"[bold green]Note added to case:[/bold green] {case_id}")
    console.print(f"[cyan]Analyst:[/cyan] {analyst}")
    console.print(f"[cyan]Note:[/cyan] {note_text}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        console.print(
            '[yellow]Usage:[/yellow] python -m case_management.case_note CASE-ID "Note text"'
        )
    else:
        case_id = sys.argv[1]
        note_text = " ".join(sys.argv[2:])

        add_note(case_id, note_text)