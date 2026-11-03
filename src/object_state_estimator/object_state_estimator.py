from .depth_estimator.depth_estimation import *
from .human_state_estimator.human_landmarks import HumanLandmarks
from .depth_estimator.depth_estimation import DepthEstimation


class ObjectStateEstimator:
    def __init__(self):
        self.human_landmarks = HumanLandmarks(configuration = 0.5, verbose = False)
        self.depth_estimation = DepthEstimation("depth-anything/DA3-SMALL")

    def __call__(self, frame):
        # return self.human_landmarks(frame)
        return self.depth_estimation(frame) 