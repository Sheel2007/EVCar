import time
import board
import busio
from adafruit_mcp4725 import MCP4725
import RPi.GPIO as GPIO

def initialize():

    # Create I2C bus interface
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create MCP4725 instance
    dac = MCP4725(i2c, address=0x60)

    print('Sucessfully initilized MCP4725!')

    return i2c, dac

def volt(dac, i2c, output_voltage=1.5, step=0.1, duration=3):
    # pass
    # MCP4725 is a 12-bit DAC, so values range from 0 (0V) to 4095 (Vcc)
    start_voltage = 1.5
    # output_voltage = 1.5  # Desired output voltage
    vcc = 3.3  # DAC reference voltage
    dac_value = int((output_voltage / vcc) * 4095)

    # Set DAC output

    current_voltage = start_voltage

    dac.raw_value = dac_value = int((start_voltage / vcc) * 4095)

    # step = 0.1
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

    print(f"DAC output set to {output_voltage}V")

    time.sleep(duration)

    dac.raw_value = 0
    # i2c.deinit()
    print('PROGRAM SUCESSFULLY TERMINATED :)')

# test = input()

def reset(dac, i2c, start_voltage=0):
    dac.raw_value = start_voltage
    i2c.deinit()
    print("Program terminated.")

