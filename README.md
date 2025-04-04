# RaspberryPI Code Examples

This repository contains a collection of Python scripts for Raspberry Pi projects, including:

- LED control
- Servo motor control
- Camera operations
- Button and buzzer interactions
- Ultrasonic sensor implementation

## Contents

- `alternating_leds.py` - Script to create an alternating blinking pattern between two LEDs
- `button_controlled_buzzer.py` - Control a buzzer with a push button input
- `camera_record_video.py` - Record video using the Raspberry Pi camera
- `camera_take_picture.py` - Take pictures using the Raspberry Pi camera
- `servo_motor_control.py` - Control a servo motor with sweeping motion
- `ultrasonic_proximity_alert.py` - Detect nearby objects using an ultrasonic sensor and trigger alerts

## Requirements

- Raspberry Pi (any model with GPIO pins)
- Python 3
- RPi.GPIO library
- PiCamera library (for camera operations)
- Appropriate hardware components (LEDs, servo motors, buttons, etc.)

## Usage

Each script is independent and can be run directly on a Raspberry Pi:

```bash
python3 script_name.py
```

Make sure to connect the hardware components to the GPIO pins as specified in each script.
