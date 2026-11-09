import os
import sys
import torch
sys.path.append(os.path.join(os.path.dirname(__file__), "Depth-Anything-V2"))
from depth_anything_v2.dpt import DepthAnythingV2


class DepthEstimation:
    def __init__(self, input_size: int = 252):
        self._input_size = input_size
        self._depth_model_config = { "encoder": "vits", "features": 64, "out_channels": [48, 96, 192, 384] }
        self._depth_model = DepthAnythingV2(**self._depth_model_config)
        self._depth_model.load_state_dict(torch.load("models/depth_anything_v2_vits.pth", map_location = "cpu"))
        self._depth_model = torch.ao.quantization.quantize_dynamic(self._depth_model, {torch.nn.Linear}, dtype = torch.qint8)

    def __call__(self, frame):
        return self._depth_model.infer_image(frame, self._input_size)