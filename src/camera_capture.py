import cv2
from src.object_state_estimator.object_state_estimator import ObjectStateEstimator


def objects_estimation() -> None:
    camera_capture = cv2.VideoCapture(2)          
    object_state_estimator = ObjectStateEstimator()

    if not camera_capture.isOpened():
        raise RuntimeError("Can't find camera")

    while True:
        ok, frame = camera_capture.read()
        if not ok:
            break

        human_landmarks = object_state_estimator(frame)
        cv2.imshow("Objects estimation", human_landmarks[0].plot())
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera_capture.release()
    cv2.destroyAllWindows()