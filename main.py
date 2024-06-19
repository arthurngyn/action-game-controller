import cv2
import queue
import threading
import time
import pydirectinput as pdi
import pygetwindow as gw
from pose_detection import PoseDetector
from move_detection import MoveDetector
from speech_recognition_module import recognize_speech  # Import recognize_speech function

# Initialize PoseDetector
pose_detector = PoseDetector()

# Initialize MoveDetector with a cooldown of 2 frames (adjust as needed)
move_detector = MoveDetector(cooldown=2)

# Initialize video capture from the camera
cap = cv2.VideoCapture(0)

# Command queue for speech recognition
command_queue = queue.Queue()

# Start speech recognition in a separate thread
speech_thread = threading.Thread(target=recognize_speech, args=(command_queue,), daemon=True)
speech_thread.start()

# Initialize command variable
command = None

# Define constants for key press durations
BLOCK_HOLD_DURATION = 1.0  # Adjust as needed (in seconds)

# Initialize block state variables
block_active = False
block_start_time = 0

def activate_roblox_window():
    """Activate the Roblox window."""
    try:
        roblox_window = gw.getWindowsWithTitle('Roblox')[0]
        roblox_window.activate()
    except IndexError:
        print("Roblox window not found. Make sure it is open and titled 'Roblox'.")

def reset_keys():
    """Reset all keys to their default state."""
    pdi.keyUp('q')
    pdi.keyUp('r')
    pdi.keyUp('t')

# Set up Mediapipe instance
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame and get pose landmarks
    results, image = pose_detector.process_frame(frame)

    # Draw the pose annotation on the image
    image = pose_detector.draw_landmarks(image, results)

    # Detect moves based on vision
    if results.pose_landmarks:
        move = move_detector.detect_move(results.pose_landmarks.landmark, pose_detector.mp_pose)
        cv2.putText(image, f'Move: {move}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Handle vision-based moves
        if move == "punch":
            pdi.click()  # Perform left click (punch)

        elif move == "block":
            if not block_active:
                pdi.keyDown('q')
                block_active = True
                block_start_time = time.time()
            else:
                # Check if block duration has been reached
                current_time = time.time()
                if current_time - block_start_time >= BLOCK_HOLD_DURATION:
                    block_active = False
                    pdi.keyUp('q')

    # Check command queue for speech commands
    while not command_queue.empty():
        command = command_queue.get()
        if command == "blast":
            reset_keys()
            pdi.keyDown('r')
            time.sleep(0.1)
            pdi.keyUp('r')
        elif command == "dash":
            reset_keys()
            pdi.keyDown('t')
            time.sleep(0.1)
            pdi.keyUp('t')
        elif command == "block":
            reset_keys()
            pdi.keyDown('q')
            block_active = True
            block_start_time = time.time()
        elif command == "stop":
            break  # Exit the loop if "stop" command is received

    # Ensure block key state is maintained correctly
    if block_active:
        current_time = time.time()
        if current_time - block_start_time >= BLOCK_HOLD_DURATION:
            pdi.keyUp('q')
            block_active = False

    # Exit the loop if "stop" command is received
    if command == "stop":
        break

    # Display the image
    cv2.imshow('Mediapipe Feed', image)

    # Switch focus to Roblox window
    activate_roblox_window()

    # Exit on pressing 'x'
    if cv2.waitKey(10) & 0xFF == ord('x'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

# Release the PoseDetector
pose_detector.release()

# Reset all keys
reset_keys()
