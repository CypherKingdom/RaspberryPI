# This program uses an ultrasonic sensor to detect nearby objects
# When objects are detected within 60cm, it activates a buzzer and LED alert
# The closer the object, the faster the buzzer and LED will blink

import RPi.GPIO as GPIO
import time

# Pin definitions
trigger = 36  # Ultrasonic sensor trigger pin
echo = 40     # Ultrasonic sensor echo pin
buzzer = 16   # Buzzer output pin
led = 10      # LED output pin

# Setup GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

def ultrasonic_read(trig_pin, echo_pin):
    """
    Measure distance using ultrasonic sensor
    Returns the distance in centimeters
    """
    # Send a 10μs pulse to trigger the sensor
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)  # 10 microsecond pulse
    GPIO.output(trig_pin, GPIO.LOW)
    
    # Wait for the echo pin to go HIGH (pulse start)
    while GPIO.input(echo_pin) == 0:
        pulseStart = time.time()
        
    # Wait for the echo pin to go LOW (pulse end)
    while GPIO.input(echo_pin) == 1:
        pulseEnd = time.time()
        
    # Calculate the pulse duration and convert to distance
    pulseDuration = pulseEnd - pulseStart
    # Speed of sound is 343 m/s or 34300 cm/s
    # Distance = (time × speed) / 2 (divide by 2 because sound travels to object and back)
    distance = pulseDuration * 17150  # (34300 / 2)
    return distance

# Main program loop
while True:
    # Read the distance from the sensor
    distance = ultrasonic_read(trigger, echo)
    print("Distance: ", distance, " cm")
    
    # If an object is detected within 60cm, activate alerts
    if(distance < 60):
        # Turn on buzzer and LED
        GPIO.output(buzzer, GPIO.HIGH)
        GPIO.output(led, GPIO.HIGH)
        # Wait for a time proportional to the distance (closer = shorter wait)
        time.sleep(distance/50)
        # Turn off buzzer and LED
        GPIO.output(buzzer, GPIO.LOW)
        GPIO.output(led, GPIO.LOW)
        # Wait again, creating a blinking effect that speeds up as objects get closer
        time.sleep(distance/50)
    
    # Brief pause before next reading
    time.sleep(0.1)