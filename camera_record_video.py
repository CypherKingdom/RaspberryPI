from picamera2 import PiCamera  # Import the PiCamera module
import time

# Initialize the camera
camera = PiCamera()

# Start recording video and save to file named 'video.h264'
camera.start_recording('video.h264')
print("Recording video...")

time.sleep(5)  # Record for 5 seconds

# Stop recording and clean up
camera.stop_recording()
print("Video recording stopped.")
camera.close()  # Release camera resources