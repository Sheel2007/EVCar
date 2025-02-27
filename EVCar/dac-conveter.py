import time
import board
import busio
from adafruit_mcp4725 import MCP4725
# from smbu2 import SMBus

# Create I2C bus interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create MCP4725 instance
dac = MCP4725(i2c, address=0x60)

# Set the DAC output to 2.5V (assuming Vcc is 3.3V)
# MCP4725 is a 12-bit DAC, so values range from 0 (0V) to 4095 (Vcc)
# Calculate the appropriate value for 2.5V output
output_voltage = 2.5  # Desired output voltage
vcc = 3.3  # DAC reference voltage
dac_value = int((output_voltage / vcc) * 4095)

# Set DAC output
dac.raw_value = dac_value

print(f"DAC output set to {output_voltage}V")

# Keep the program running to maintain the output
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    output_voltage = 0
    dac.raw_value = dac_value
    print("Program terminated.")

