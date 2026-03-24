"""
Module responsible for managing sacred data flows (Streams).

Demonstrates the correct separation between input channels, standard output,
and alerts.
"""

import sys


def manage_streams() -> None:
    """Collect data via input stream and route messages."""
    print("=== CYBER ARCHIVES - COMMUNICATIONS SYSTEM ===")

    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {archivist_id}: {status_report}",
          file=sys.stdout)

    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)

    print("[STANDARD] Data transmission complete\n", file=sys.stdout)

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    manage_streams()
