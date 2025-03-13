import time
import board
import busio
from adafruit_mcp4725 import MCP4725
import RPi.GPIO as GPIO
# from gpiozero import OutputDevice


TRANSISTOR_PIN = 26

# transistor = OutputDevice(TRANSISTOR_PIN)

# Create I2C bus interface
i2c = busio.I2C(board.SCL, board.SDA)
# i2c.deinit()
# exit()

# Create MCP4725 instance
dac = MCP4725(i2c, address=0x60)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(TRANSISTOR_PIN, GPIO.OUT)

# GPIO.output(TRANSISTOR_PIN, GPIO.LOW)
# transistor.on()

# MCP4725 is a 12-bit DAC, so values range from 0 (0V) to 4095 (Vcc)
start_voltage = 1
output_voltage = 3  # Desired output voltage
vcc = 3.3  # DAC reference voltage
dac_value = int((output_voltage / vcc) * 4095)

# Set DAC output

current_voltage = start_voltage

dac.raw_value = int((start_voltage / vcc) * 4095)

step = 0.1
print(f'Starting on {current_voltage}V')

while True:
    time.sleep(1)
    current_voltage += step
    dac.raw_value = int((current_voltage / vcc) * 4095)
    print(f'Changed to {current_voltage}V')
    if current_voltage >= output_voltage:
        current_voltage = output_voltage
        dac.raw_value = dac_value
        print(f'Now ending on {current_voltage}')
        break


# time.sleep(10)

# dac.raw_value = dac_value

# transistor.off()
# GPIO.output(TRANSISTOR_PIN, GPIO.HIGH)

# GPIO.cleanup()
# i2c.deinit()
# exit()

print(f"DAC output set to {output_voltage}V")

# Keep the program running to maintain the output
"""
test = input()

if test:
    dac.raw_value = start_voltage
    i2c.deinit()
    # transistor.on()
    # GPIO.output(TRANSISTOR_PIN, GPIO.LOW)
    print("Program terminated.")
"""

time.sleep(5)

print('Reseting to 0V')
dac.raw_value = 0
i2c.deinit()
# transistor.on()
# GPIO.output(TRANSISTOR_PIN, GPIO.LOW)
print("Program terminated succesfully.")