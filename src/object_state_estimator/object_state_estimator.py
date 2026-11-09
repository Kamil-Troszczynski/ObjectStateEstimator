from .depth_estimator.depth_estimation import *
from .human_state_estimator.human_landmarks import HumanLandmarks
from .depth_estimator.depth_estimation import DepthEstimation


class ObjectStateEstimator:
    def __init__(self):
        self.human_landmarks = HumanLandmarks(configuration = 0.5, verbose = False)
        self.depth_estimation = DepthEstimation()

    def __call__(self, frame) -> tuple:
        human_landmarks = self.human_landmarks(frame)
        depth_estimation = self.depth_estimation(frame) 
        return human_landmarks, depth_estimation