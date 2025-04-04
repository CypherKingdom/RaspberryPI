import RPi.GPIO as GPIO

# Pin Definitions
button = 10  # GPIO pin for the push button
buzzer = 16  # GPIO pin for the buzzer

# Set up GPIO mode (BOARD uses physical pin numbers)
GPIO.setmode(GPIO.BOARD)

# Configure button as input and buzzer as output
GPIO.setup(button, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

# Main program loop
while True:
    # Check if button is pressed (HIGH)
    if GPIO.input(button) == GPIO.HIGH:
        GPIO.output(buzzer, GPIO.HIGH)  # Activate buzzer
    else:
        GPIO.output(buzzer, GPIO.LOW)   # Deactivate buzzer