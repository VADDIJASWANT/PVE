# pve/cli.py
import argparse
from pve.core import VirtualEnvManager

def main():
    parser = argparse.ArgumentParser(description="Python Virtual Environment Manager (pve)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'create' command
    create_parser = subparsers.add_parser("create", help="Create a virtual environment")
    create_parser.add_argument("env_name", nargs="?", default="venv", help="Name of the virtual environment")

    # 'start' command
    start_parser = subparsers.add_parser("start", help="Activate a virtual environment")
    start_parser.add_argument("env_name", nargs="?", default="venv", help="Name of the virtual environment")

    args = parser.parse_args()

    if args.command == "create":
        manager = VirtualEnvManager(args.env_name)
        manager.create()
    elif args.command == "start":
        manager = VirtualEnvManager(args.env_name)
        if manager.exists():
            manager.start()
        else:
            print(f"Error: Virtual environment '{args.env_name}' does not exist. Create it first with 'pve create {args.env_name}'.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()