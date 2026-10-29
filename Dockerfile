FROM osrf/ros:humble-desktop

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    ROS_DISTRO=humble

# cpu lub c121
ARG TORCH_VARIANT=cu121

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    wget \
    nano \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-opencv \
    libgl1 \
    libglib2.0-0 \
    ros-humble-cv-bridge \
    ros-humble-vision-opencv \
    ros-humble-vision-msgs \
    ros-humble-image-transport \
    ros-humble-image-transport-plugins \
    ros-humble-rqt-image-view \
    ros-humble-usb-cam \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir \
        torch torchvision --index-url https://download.pytorch.org/whl/${TORCH_VARIANT} && \
    pip3 install --no-cache-dir \
        "numpy<2" \
        ultralytics \
        opencv-python \
        scipy \
        filterpy

WORKDIR /ros2_ws
RUN mkdir -p src && \
    echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc && \
    echo "[ -f /ros2_ws/install/setup.bash ] && source /ros2_ws/install/setup.bash" >> ~/.bashrc

CMD ["tail", "-f", "/dev/null"]
