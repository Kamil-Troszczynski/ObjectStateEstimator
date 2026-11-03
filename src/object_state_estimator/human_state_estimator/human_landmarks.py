from ultralytics import YOLO


class HumanLandmarks:
    def __init__(self, configuration: float, verbose: bool = False):
        self._cnn = YOLO("models/yolo26n-pose.pt")
        self._configuration = configuration
        self._verbose = verbose

    def __call__(self, frame):
        return self._cnn(frame, conf = self._configuration, verbose = self._verbose)