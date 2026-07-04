from config import load_node_config
from sensors import read_ds18b20, read_bme280


def main():

    config = load_node_config()

    print(f"\nNode: {config['node']['id']}\n")

    print("Sensors")
    print("-------")

    for sensor in config["sensors"]:

        print(f"ID:      {sensor['id']}")
        print(f"Type:    {sensor['type']}")

        if sensor["type"] == "ds18b20":
            read_ds18b20(sensor)

        elif sensor["type"] == "bme280":
            read_bme280(sensor)

        print()


if __name__ == "__main__":
    main()
