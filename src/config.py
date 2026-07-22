#!/usr/bin/env python3

"""
SEMP Configuration Module

Functions for locating and loading project configuration files.
"""

from pathlib import Path
import yaml


# ---------------------------------------------------------------------
# Project Paths
# ---------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_DIR = PROJECT_ROOT / "config"

NODE_FILE = CONFIG_DIR / "sensors.yaml"


# ---------------------------------------------------------------------
# Configuration Functions
# ---------------------------------------------------------------------

def load_node_config():
    """
    Load node.yaml and return its contents as a dictionary.
    """

    with NODE_FILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
