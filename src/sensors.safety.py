"""
SEMP Sensor Module
"""

from w1thermsensor import W1ThermSensor

import board
import busio

import adafruit_bme280.basic as adafruit_bme280


def read_ds18b20(sensor):
    """
    Read a DS18B20 temperature sensor.

    Returns:
        {
            "C": 29.94
        }
    """

    sensor_id = sensor["address"].removeprefix("28-")

    thermometer = W1ThermSensor(sensor_id=sensor_id)

    temperature = thermometer.get_temperature()

    return {
        sensor["id"]: round(temperature, 2)
    }


def read_bme280(sensor):
    """
    Read a BME280 environmental sensor.

    Returns:
        {
            "THP01_T": 32.47,
            "THP01_H": 24.61,
            "THP01_P": 816.52
        }
    """

    i2c = busio.I2C(board.SCL, board.SDA)

    bme280 = adafruit_bme280.Adafruit_BME280_I2C(
        i2c,
        address=sensor["address"]
    )

    return {
        f"{sensor['id']}_T": round(bme280.temperature, 2),
        f"{sensor['id']}_H": round(bme280.humidity, 2),
        f"{sensor['id']}_P": round(bme280.pressure, 2),
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
