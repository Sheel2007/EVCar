import time
import board
import busio
import adafruit_mcp4725

# Create the I2C bus interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the MCP4725 instance.
# The default I2C address for the MCP4725 is 0x60.
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)

# Configuration parameters.
# Adjust these as needed.
max_voltage = 2.0    # Maximum voltage you want to achieve (2 V).
ref_voltage = 5.0    # The reference voltage of your DAC (often 5 V on many breakout boards).
max_dac = 4095       # 12-bit resolution gives 4096 discrete levels (0 to 4095).
steps = 100          # Number of steps for the voltage ramp.
delay = 0.05         # Delay (in seconds) between each step.

def voltage_to_dac_value(voltage):
    """
    Convert a desired voltage to the corresponding 12-bit DAC value.
    """
    return int((voltage / ref_voltage) * max_dac)

# Ramp up from 0 V to 2 V.
for i in range(steps + 1):
    # Calculate the current voltage.
    voltage = (i / steps) * max_voltage
    # Convert to a DAC value.
    dac_value = voltage_to_dac_value(voltage)
    # Set the DAC output.
    dac.value = dac_value
    time.sleep(delay)

# Ramp down from 2 V to 0 V.
for i in range(steps, -1, -1):
    voltage = (i / steps) * max_voltage
    dac_value = voltage_to_dac_value(voltage)
    dac.value = dac_value
    time.sleep(delay)
