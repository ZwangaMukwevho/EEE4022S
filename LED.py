import RPi.GPIO as GPIO
import time

class LED:
    
    def __init__(self): 
            
            # GPIO.setmode(GPIO.BOARD)
            pass
    
    def swichRfidOnGreen(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
     
        GPIO.setup(24,GPIO.OUT)
        GPIO.output(24,GPIO.HIGH)

        # GPIO.setup(18,GPIO.OUT)
        # GPIO.output(18,GPIO.HIGH)
        time.sleep(1)

        # GPIO.output(18,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
    
    def swichRfidOnRed(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
     
        # GPIO.setup(16,GPIO.OUT)
        # GPIO.output(16,GPIO.HIGH)
        GPIO.setup(23,GPIO.OUT)
        GPIO.output(23,GPIO.HIGH)

        time.sleep(1)
        # GPIO.output(16,GPIO.LOW)  
        GPIO.output(23,GPIO.LOW) 

    def swichOnTempRed(self):
        
        GPIO.setwarnings(False)
     
        GPIO.setup(11,GPIO.OUT)
        
        GPIO.output(11,GPIO.HIGH)
        time.sleep(1)

        GPIO.output(11,GPIO.LOW)

    def swichOnTempGreen(self):
        
        GPIO.setwarnings(False)
     
        GPIO.setup(13,GPIO.OUT)
        
        GPIO.output(13,GPIO.HIGH)
        time.sleep(1)

        GPIO.output(13,GPIO.LOW)
    
# LEDObj = LED()
# LEDObj.swichOnTempRed()
# GPIO.cleanup()      
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(23,GPIO.OUT)
# GPIO.setup(24,GPIO.OUT)
# print("LED on")
# GPIO.output(23,GPIO.HIGH)
# GPIO.output(24,GPIO.HIGH)
# time.sleep(1)
# print("LED off")
# GPIO.output(23,GPIO.LOW)
# GPIO.output(24,GPIO.LOW)
