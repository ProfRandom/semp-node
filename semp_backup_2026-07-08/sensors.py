import board
import adafruit_bme280
from w1thermsensor import W1ThermSensor


def read_ds18b20(sensor):
    """
    Read a single DS18B20 sensor.

    Returns:
        {
            "C": 29.94
        }
    """

    ds = W1ThermSensor(sensor_id=sensor["address"])

    temperature = round(ds.get_temperature(), 2)

    return {
        sensor["id"]: temperature
    }


def read_bme280(sensor):
    """
    Read a single BME280 sensor.

    Returns:
        {
            "THP01_T": 32.47,
            "THP01_H": 24.61,
            "THP01_P": 816.52
        }
    """

    i2c = board.I2C()

    bme = adafruit_bme280.Adafruit_BME280_I2C(
        i2c,
        address=sensor["address"]
    )

    return {
        f"{sensor['id']}_T": round(bme.temperature, 2),
        f"{sensor['id']}_H": round(bme.humidity, 2),
        f"{sensor['id']}_P": round(bme.pressure, 2),
    }


def read_all_sensors(config):
    """
    Read every configured sensor and return a
    single observation dictionary.
    """

    observation = {}

    for sensor in config["sensors"]:

        if sensor["type"] == "ds18b20":
            observation.update(read_ds18b20(sensor))

        elif sensor["type"] == "bme280":
            observation.update(read_bme280(sensor))

    return observation
