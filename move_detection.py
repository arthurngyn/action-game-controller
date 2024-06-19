import numpy as np

class MoveDetector:
    def __init__(self, threshold=0.05, cooldown=10):
        self.previous_landmarks = None
        self.threshold = threshold
        self.cooldown_counter = 0
        self.cooldown = cooldown  # Number of frames cooldown lasts
        self.current_move = "block"  # Default move
        self.temporary_move = None
        self.temporary_move_counter = 0
        self.temporary_move_duration = 20  # Frames to hold temporary move before reverting

    def detect_move(self, landmarks, mp_pose):
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
        left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
        right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]

        current_landmarks = np.array([
            [left_wrist.x, left_wrist.y],
            [left_elbow.x, left_elbow.y],
            [right_wrist.x, right_wrist.y],
            [right_elbow.x, right_elbow.y]
        ])

        if self.previous_landmarks is None:
            self.previous_landmarks = current_landmarks
            return self.current_move

        movement = np.linalg.norm(current_landmarks - self.previous_landmarks, axis=1)
        self.previous_landmarks = current_landmarks

        if np.any(movement > self.threshold):
            self.cooldown_counter = self.cooldown  # Reset cooldown counter
            return "punch"
        elif self.cooldown_counter > 0:
            self.cooldown_counter -= 1
            return "punch"
        elif self.temporary_move is not None and self.temporary_move_counter > 0:
            self.temporary_move_counter -= 1
            return self.temporary_move
        else:
            return self.current_move

    def set_temporary_move(self, move):
        self.temporary_move = move
        self.temporary_move_counter = self.temporary_move_duration

    def clear_temporary_move(self):
        self.temporary_move = None
        self.temporary_move_counter = 0

    def get_current_move(self):
        return self.current_move
