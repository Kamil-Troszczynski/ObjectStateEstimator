from human_landmarks import HumanLandmarks
import numpy as np
import cv2


class HumanStateEstimator:
    def __init__(self):
        self.human_landmarks = HumanLandmarks(configuration = 0.5, verbose = False)
        self._nxy_landmarks = None

    def normalized_landmarks_aquisition(self, frame) -> None:
        landmarks = self.human_landmarks(frame)
        for landmark in landmarks:
            self._nxy_landmarks = landmark.keypoints.xyn

    def main_human_nxy(self, frame) -> tuple[tuple[np.ndarray], tuple[np.ndarray]]:
        """ Tensor with normalized xy coordinates of specific human keypoints """
        # self._nxy_landmarks:

        # Nose
        # Left Eye
        # Right Eye
        # Left Ear
        # Right Ear
        # Left Shoulder
        # Right Shoulder
        # Left Elbow
        # Right Elbow
        # Left Wrist
        # Right Wrist
        # Left Hip
        # Right Hip
        # Left Knee
        # Right Knee
        # Left Ankle
        # Right Ankle

        self.normalized_landmarks_aquisition(frame)
        left_shoulder_nxy = self._nxy_landmarks[:, 5]
        right_shoulder_nxy = self._nxy_landmarks[:, 6]

        left_hip_nxy = self._nxy_landmarks[:, 7]
        right_hip_nxy = self._nxy_landmarks[:, 8]

        return (left_shoulder_nxy, right_shoulder_nxy), (left_hip_nxy, right_hip_nxy)


def linear_params(nxy1: np.ndarray, nxy2: np.ndarray2) -> np.ndarray:
    W = np.array([[nxy1[0], 1], [nxy2[0], 1]])
    y = np.concat([nxy1[1], nxy2[1]])
    return np.linalg.inv(W) @ y


