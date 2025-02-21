import RPi.GPIO as GPIO
import time

# Pin configuration
PWM_PIN = 18  # GPIO18 supports hardware PWM
FREQUENCY = 100  # PWM frequency in Hz
DUTY_CYCLE = 50  # Duty cycle (0 to 100)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Create PWM instance
pwm = GPIO.PWM(PWM_PIN, FREQUENCY)

# Start PWM
pwm.start(DUTY_CYCLE)

try:
    while True:
        # Adjust duty cycle dynamically (optional)
        duty_cycle = float(input("Enter duty cycle (0 to 100): "))
        pwm.ChangeDutyCycle(duty_cycle)
except KeyboardInterrupt:
    # Clean up
    pwm.stop()
    GPIO.cleanup()

