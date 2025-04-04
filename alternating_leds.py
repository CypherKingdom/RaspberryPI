import RPi.GPIO as GPIO
import time

# Pin Definitions
led1 = 10  # GPIO pin for first LED
led2 = 16  # GPIO pin for second LED

# Set up GPIO mode (BOARD uses physical pin numbers)
GPIO.setmode(GPIO.BOARD)

# Configure pins as outputs
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

# Initialize both LEDs as OFF
GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)

# Main loop for alternating LED blinking pattern
while True:
    # First LED ON, second LED OFF
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(0.5)  # Pause for 0.5 seconds
    
    # First LED OFF, second LED ON
    GPIO.output(led2, GPIO.HIGH)
    GPIO.output(led1, GPIO.LOW)
    time.sleep(0.5)  # Pause for 0.5 seconds