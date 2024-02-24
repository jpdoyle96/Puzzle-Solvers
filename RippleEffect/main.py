# Ripple Effect
# 
# Header here

_VERSION_ = "1.0.0"

import sys

def solve_puzzle(args):
    """Docstring here"""
    print("UNIMPLEMENTED")

def create_puzzle(args):
    """Docstring here"""
    print("UNIMPLEMENTED")

def print_version():
    """Docstring here"""
    print(f"Version: {_VERSION_}")

def print_help():
    """Docstring here"""
    print("Ripple Effect\n")
    print("Usage:")
    print("  ripple.py solve <file> (bfs | dfs | human) [options]")
    print("  ripple.py create <size> <rooms> <difficulty> [options]")
    print("  ripple.py -h | --help")
    print("  ripple.py --version")
    print("Options:")
    print(f"  {"-h --help":14} Show this screen.")
    print(f"  {"--version":14} Show's the current version.")

def print_error(arg_type=None):
    """Docstring here"""
    if arg_type != None:
        print(f"Error: Invalid argument provided for {arg_type}")
        print("  Type ripple.py -h for usage details")
    else:
        print("Error: Invalid argument provided")
        print("  Type ripple.py -h for usage details")

# Process command line arguments
arguments = sys.argv

if len(arguments) == 1:
    print_help()
if (arguments[1] == "-h" or arguments[1] == "--help"):
    # Check for valid formatting
    if (len(arguments) == 2):
        print_help()
    else:
        print_error()
if (arguments[1] == "-version"):
    if (len(arguments) == 2):
        print_version()
    else:
        print_error()
if (arguments[1] == "solve"):
    # Temporary routing
    solve_puzzle()
if (arguments[1] == "create"):
    # Temporary routing
    create_puzzle()
