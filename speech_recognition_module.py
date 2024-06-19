import speech_recognition as sr
import queue

# Function to recognize speech and put commands into a queue
def recognize_speech(command_queue):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Set energy threshold
    recognizer.energy_threshold = 5000

    with mic as source:
        print("Listening for commands...")
        while True:
            try:
                audio = recognizer.listen(source)
                print("Audio captured...")
                command = recognizer.recognize_google(audio).lower()
                print(f"Heard command: {command}")
                if command == "done":
                    command_queue.put(command)
                    break
                commands = command.split()
                for cmd in commands:
                    command_queue.put(cmd)
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print(f"Error requesting recognition results: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    command_queue = queue.Queue()
    recognize_speech(command_queue)
