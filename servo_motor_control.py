import RPi.GPIO as GPIO
import time

# Define GPIO pin for servo control
servo_motor = 16  # GPIO pin for servo motor signal

# Set up GPIO mode (BOARD uses physical pin numbers)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_motor, GPIO.OUT)

# Initialize PWM for servo control
# Servo motors typically operate at 50Hz frequency
servo = GPIO.PWM(servo_motor, 50)  # Set frequency to 50Hz
servo.start(7.5)  # Initialize the servo position to 90 degrees (center position)

# Main program loop for continuous servo movement
while True:
    # Sweep servo from 0 to 180 degrees
    # The duty cycle values 2.5-12.5 typically represent 0-180 degrees for most servos
    for i in range(2.5, 12.5, 1.25):  # Increasing duty cycle (move clockwise)
        servo.ChangeDutyCycle(i)
        time.sleep(0.05)  # Small delay to allow servo to reach position
        
    # Sweep servo from 180 to 0 degrees
    for i in range(12.5, 2.5, -1.25):  # Decreasing duty cycle (move counterclockwise)
        servo.ChangeDutyCycle(i)
        time.sleep(0.05)  # Small delay to allow servo to reach position