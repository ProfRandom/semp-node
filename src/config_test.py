from pathlib import Path
import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
NODE_FILE = CONFIG_DIR / "node.yaml"


def load_node_config():
    """Load node.yaml and return its contents."""

    with NODE_FILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():

    print(f"Project Root : {PROJECT_ROOT}")
    print(f"Node Config  : {NODE_FILE}")

    config = load_node_config()

    print("\nContents:\n")
    print(config)


if __name__ == "__main__":
    main()
