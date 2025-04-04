from picamea import PiCamera  # Note: This might be a typo, should probably be 'picamera'
import time

# Initialize the camera
my_camera = PiCamera()

# Countdown before taking picture
for i in range(3, 0, -1):
    print(i)  # Display countdown number
    time.sleep(1)  # Wait for 1 second between counts

print("Taking picture...")

# Capture an image and save it as 'image.jpg'
my_camera.capture('image.jpg')
print("Picture taken!")

# Release camera resources
my_camera.close()