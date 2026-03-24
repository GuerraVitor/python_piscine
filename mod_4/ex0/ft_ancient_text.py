"""Module for executing the data recovery protocol on a text file."""


def recover_data() -> None:
    """Ensure safe handling of resources and error in data recovery."""
    vault_name: str = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {vault_name}")

    try:
        with open(vault_name, "r", encoding="utf-8") as vault:
            print("Connection established...\n")
            print("RECOVERED DATA:")

            ancient_data: str = vault.read()
            print(ancient_data)
            print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_data()
