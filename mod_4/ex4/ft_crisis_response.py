"""Crisis response module for handling archive access failures safely."""


def read_archive_data(archive_name: str) -> str:
    """Read archive data only from the current exercise directory."""
    with open(archive_name, "r", encoding="utf-8") as archive:
        return archive.read().strip()


def handle_archive_access(
    archive_name: str,
    routine_access: bool = False,
) -> None:
    """Attempt archive access and respond with the correct crisis protocol."""
    access_type: str = (
        "\nROUTINE ACCESS" if routine_access else "\nCRISIS ALERT"
    )
    print(f"{access_type}: Attempting access to '{archive_name}'...")

    try:
        if archive_name == "classified_vault.txt":
            raise PermissionError("Security clearance required")

        recovered_data: str = read_archive_data(archive_name)
        print(f"SUCCESS: Archive recovered - ``{recovered_data}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, emergency protocols engaged")


def crisis_response_system() -> None:
    """Run all crisis scenarios and verify archive stability."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_archive_access("lost_archive.txt")
    handle_archive_access("classified_vault.txt")
    handle_archive_access("standard_archive.txt", routine_access=True)

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response_system()
