# Action Game Controller

This project is designed to control a Roblox game using both voice commands and pose detection via a webcam. The controller can perform various in-game actions like "blast", "dash", "punch", and "block".

## Features

- **Voice Commands**: Use speech recognition to execute game commands.
- **Pose Detection**: Detects body poses and performs actions based on movements.
- **Seamless Integration**: Smooth key presses and actions for a better gaming experience.

## Requirements

- Python 3.6+
- OpenCV
- PyAutoGUI
- PyGetWindow
- SpeechRecognition
- PyAudio
- TensorFlow
- Mediapipe

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/action-game-controller.git
    cd action-game-controller
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure that `pydirectinput` and other packages are correctly installed:
    ```bash
    pip install pydirectinput
    pip install pygetwindow
    pip install opencv-python
    pip install mediapipe
    pip install SpeechRecognition
    pip install pyaudio
    pip install tensorflow
    ```

## Setup

Before running the script, make sure to run your IDE or editor as an administrator. This is crucial for sending keyboard commands to the Roblox game.

## Running the Project

1. Start your Roblox game and ensure it is running in a window titled "Roblox".
2. Run the main script:
    ```bash
    python main.py
    ```
3. The webcam feed will appear, and the program will start listening for voice commands and detecting poses.

## Voice Commands

- **"blast"**: Simulates the 'r' key press for a blast action.
- **"dash"**: Simulates the 't' key press for a dash action.
- **"block"**: Holds down the 'q' key for blocking.
- **"stop"**: Stops the script.

## Pose Detection

- **Punch**: Detected by specific pose movements and simulates a left-click.
- **Block**: Detected by specific pose movements and holds down the 'q' key.

## Troubleshooting

- Ensure you are running the script and your IDE/editor as an administrator.
- Make sure the Roblox window title matches exactly with 'Roblox'.
- If voice commands or pose detection are not working as expected, verify your microphone and webcam settings.
- Adjust key press durations in the script if actions are not smooth.

## Acknowledgements

- [Mediapipe](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [PyGetWindow](https://github.com/asweigart/PyGetWindow)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
