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

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANSISTOR_PIN, GPIO.OUT)

GPIO.output(TRANSISTOR_PIN, GPIO.LOW)
# transistor.on()

# MCP4725 is a 12-bit DAC, so values range from 0 (0V) to 4095 (Vcc)
# Calculate the appropriate value for 2.5V output
output_voltage = 1.5  # Desired output voltage
vcc = 3.3  # DAC reference voltage
dac_value = int((output_voltage / vcc) * 4095)

# Set DAC output
# dac.raw_value = dac_value

time.sleep(2)

# transistor.off()
GPIO.output(TRANSISTOR_PIN, GPIO.HIGH)

# GPIO.cleanup()
# exit()

print(f"DAC output set to {output_voltage}V")

# Keep the program running to maintain the output
test = input()

if test:
    # output_voltage = 0
    # dac.raw_value = int((output_voltage / vcc) * 4095)
    i2c.deinit()
    # transistor.on()
    GPIO.output(TRANSISTOR_PIN, GPIO.LOW)
    print("Program terminated.")

