"""
SEMP CSV Writer

Writes observation dictionaries to CSV files.
"""

import csv
from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def write_observation(observation):
    """
    Append one observation to the node's CSV file.

    If the file does not yet exist, create it and write
    a header row first.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    node_id = observation["NodeID"]

    csv_file = OUTPUT_DIR / f"{node_id.lower()}_observations.csv"

    file_exists = csv_file.exists()

    with open(csv_file, "a", newline="") as outfile:

        writer = csv.DictWriter(
            outfile,
            fieldnames=observation.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(observation)
