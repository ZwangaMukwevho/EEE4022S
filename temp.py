from time import sleep
import asyncio

GPIO.setmode(GPIO.BCM)
class temp:
    def __init__(self):
               
                # GPIO.setmode(GPIO.BCM)
                pass
    
    async def readTemp(self):
        i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
        mlx = adafruit_mlx90614.MLX90614(i2c)

        accumulated_temp = 0

        for i in range(10):
            ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
            targetTemp = "{:.2f}".format(mlx.object_temperature)
            targetTemp = float(targetTemp) 

            await asyncio.sleep(0.3)
            # time.sleep(0.3)

            # print("Ambient Temperature:", ambientTemp, "°C")
            # print("Target Temperature:", targetTemp,"°C")

            accumulated_temp = accumulated_temp + float(targetTemp)

        accumulated_temp = round(accumulated_temp/10,2)
        # print("\nAccumulated Temps: "+str(accumulated_temp))
        
        return accumulated_temp

# tempObj = temp()
# tempObj.readTemp()