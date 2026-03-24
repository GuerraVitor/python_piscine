"""
Vault Security Module.

Demonstrates the use of Context Managers (with) to ensure absolute data
integrity during I/O operations.
"""


def secure_vault_operations() -> None:
    """
    Execute secure read and write protocols.

    Uses the 'with' statement to guarantee automatic closure (sealing)
    of the vaults, preventing data corruption and resource leaks.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Iniatiating secure vault access...")
    print("Vault connection established with failsafe protocol\n")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r", encoding="utf-8") as read_vault:
            recovered_data: str = read_vault.read()
            print(recovered_data + "\n")
    except FileNotFoundError:
        print("ERROR: 'classified_data.txt' not found in current directory.")
        return

    print("SECURE PRESERVATION:")
    new_protocol: str = "[CLASSIFIED] New security protocols archived"

    with open("security_protocols.txt", "w", encoding="utf-8") as write_vault:
        write_vault.write(new_protocol)
        print(new_protocol + "\n")
    print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    secure_vault_operations()
