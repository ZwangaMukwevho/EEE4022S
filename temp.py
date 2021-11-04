import board
import busio as io
import adafruit_mlx90614
import RPi.GPIO as GPIO
from time import sleep
import asyncio

GPIO.setmode(GPIO.BCM)
class temp:
    def __init__(self):
                pass
    
    async def readTemp(self):
        """Samples temperature readings from the and returns the average temperature of the target object.

        :return: [Average Temperature of target object]
        :rtype: [float]
        """
        i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
        mlx = adafruit_mlx90614.MLX90614(i2c)

        accumulated_temp = 0

        for i in range(10):
            ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
            targetTemp = "{:.2f}".format(mlx.object_temperature)
            targetTemp = float(targetTemp) 

            await asyncio.sleep(0.3)
            accumulated_temp = accumulated_temp + float(targetTemp)

        accumulated_temp = round(accumulated_temp/10,2)
        return accumulated_temp