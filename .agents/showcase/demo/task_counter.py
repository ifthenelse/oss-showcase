"""Synthetic CLI fixture for the OSS Showcase demo."""

import argparse

parser = argparse.ArgumentParser(description="Count the tasks listed on the command line.")
parser.add_argument("tasks", nargs="+")
print(f"Tasks: {len(parser.parse_args().tasks)}")
