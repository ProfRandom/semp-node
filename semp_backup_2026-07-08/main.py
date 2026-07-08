from pprint import pprint

from config import load_node_config
from scheduler import get_sync_time, get_obsnum
from sensors import read_all_sensors
from csv_writer import write_observation


def main():

    config = load_node_config()

    observation = {}

    observation["NodeID"] = config["node"]["id"]

    sync_time = get_sync_time()

    observation["SyncTime"] = sync_time.strftime("%Y-%m-%d %H:%M:%S")

    observation["ObsNum"] = f"{get_obsnum(sync_time):03d}"

    observation.update(read_all_sensors(config))

    print("\nObservation")
    print("-----------")
    pprint(observation)

    write_observation(observation)

    print("\nObservation written to CSV.\n")


if __name__ == "__main__":
    main()
