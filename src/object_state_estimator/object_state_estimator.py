from .human_state_estimator.human_landmarks import HumanLandmarks


class ObjectStateEstimator:
    def __init__(self):
        self.human_landmarks = HumanLandmarks(configuration = 0.5, verbose = False)

    def __call__(self, frame):
        human_landmarks = self.human_landmarks(frame)
        return human_landmarks