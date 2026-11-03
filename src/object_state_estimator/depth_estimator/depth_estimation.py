import cv2
import torch
from depth_anything_3.api import DepthAnything3


class DepthEstimation:
    def __init__(self, model_name: str):
        self.model = DepthAnything3.from_pretrained(model_name)
    
    def __call__(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        prediction = self.model.inference([rgb_frame], process_res = 504)
        return cv2.resize(prediction.depth[0], (frame.shape[1], frame.shape[0]))