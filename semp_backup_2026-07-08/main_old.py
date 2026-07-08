from datetime import datetime
from pprint import pprint

from config import load_node_config
from sensors import read_ds18b20, read_bme280
from csv_writer import write_observation


def build_observation(config):

    observation = {}

    observation["NodeID"] = config["node"]["id"]
    observation["TimeStamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for sensor in config["sensors"]:

        if sensor["type"] == "ds18b20":

            observation[sensor["id"]] = round(
                read_ds18b20(sensor),
                2
            )

        elif sensor["type"] == "bme280":

            bme = read_bme280(sensor)

            observation[f"{sensor['id']}_T"] = round(
                bme["temperature"],
                2
            )

            observation[f"{sensor['id']}_H"] = round(
                bme["humidity"],
                2
            )

            observation[f"{sensor['id']}_P"] = round(
                bme["pressure"],
                2
            )

    return observation


def main():

    config = load_node_config()

    observation = build_observation(config)

    write_observation(observation)

    print("\nObservation")
    print("-----------")

    pprint(observation)

    print("\nObservation written to CSV.\n")


if __name__ == "__main__":
    main()
