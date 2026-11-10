# ObjectStateEstimator

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch2012.1-EE4C2C?logo=pytorch&logoColor=white)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO-111F68?logo=yolo&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)

State estimation of people from a camera image, running inside a Docker container. Another step will be creation object state estimation feature.

## Models

Weights are stored in `models/`.

| Model | Task |
|---|---|
| YOLO26n-pose | Human pose estimation (keypoints) |

## Requirements

- Linux with Docker installed
- USB camera available as `/dev/video2` (set in `setup.sh`)
- X11 server, if you want the preview window (`cv2.imshow`)

## 1. Building the image

From the repository root:

```bash
docker build -t object_state_estimator:latest .
```

## 2. Running the container

```bash
chmod +x setup.sh
./setup.sh
```

The script removes any previous container with the same name and starts a new one in the background, with the camera attached, X11 display access, and the repository mounted at `/object_state_estimator`.

If your camera has a different device number, change `--device /dev/video2` in `setup.sh`. List the available devices with `v4l2-ctl --list-devices`.

## 3. Entering the container

```bash
docker exec -it object_state_estimator bash
```

Then run the program inside:

```bash
python3 main.py
```

Press `q` to close the preview window.

## Stopping and removing the container

```bash
docker stop object_state_estimator
docker rm object_state_estimator
```
