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

        object_estimation = object_state_estimator(frame)

        depth_view = cv2.normalize(object_estimation, None, 0, 255, cv2.NORM_MINMAX).astype("uint8")
        depth_view = cv2.applyColorMap(depth_view, cv2.COLORMAP_INFERNO)
        
        cv2.imshow("Objects estimation", depth_view)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera_capture.release()
    cv2.destroyAllWindows()