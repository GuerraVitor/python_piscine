import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_virtual_env():
        print("Status: python is running in a isolated virtual enviroment\n")

        print(f"Current python executable: {sys.executable}\n")

        print(f"Virtual enviroment prefix: {sys.prefix}")
        print(f"Global base prefix: {sys.base_prefix}\n")

        print("Package Locations:")
        print(f" venv packages in:\n \t{site.getsitepackages()[0]}")
        print(
            f" global packages in:\n \t{sys.base_prefix}/lib/python/"
            "{sys.version_info.major}.{sys.version_info.minor}"
             )


if __name__ == "__main__":
    main()
