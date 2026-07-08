"""
SEMP Sensor Module
"""

from w1thermsensor import W1ThermSensor

import board
import busio

import adafruit_bme280.basic as adafruit_bme280


def read_ds18b20(sensor):
    """
    Read a DS18B20 temperature sensor and display its temperature.
    """

    sensor_id = sensor["address"].removeprefix("28-")

    thermometer = W1ThermSensor(sensor_id=sensor_id)

    temperature = thermometer.get_temperature()

    print(f"{sensor['id']}: {temperature:.2f} °C")


def read_bme280(sensor):
    """
    Read a BME280 environmental sensor and display its readings.
    """

    i2c = busio.I2C(board.SCL, board.SDA)

    bme280 = adafruit_bme280.Adafruit_BME280_I2C(
        i2c,
        address=sensor["address"]
    )

    print(f"{sensor['id']}:")
    print(f"  Temperature : {bme280.temperature:.2f} °C")
    print(f"  Humidity    : {bme280.humidity:.2f} %")
    print(f"  Pressure    : {bme280.pressure:.2f} hPa")
