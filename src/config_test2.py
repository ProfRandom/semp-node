#!/usr/bin/env python3

from pathlib import Path
import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
NODE_FILE = PROJECT_ROOT / "config" / "node.yaml"


def load_node_config():
    with NODE_FILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


config = load_node_config()

print(f"\nNode: {config['node']['id']}\n")

print("Sensors")
print("-------")

for sensor in config["sensors"]:

    print(f"ID:      {sensor['id']}")
    print(f"Type:    {sensor['type']}")

    if sensor["type"] == "ds18b20":
        print(f"Address: {sensor['address']}")

    elif sensor["type"] == "bme280":
        print(f"Bus:     {sensor['bus']}")
        print(f"Address: 0x{sensor['address']:02X}")

    print()
