FROM python:3.10-slim-bookworm

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

# cpu lub cu121
ARG TORCH_VARIANT=cpu

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    wget \
    nano \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir \
        torch torchvision --index-url https://download.pytorch.org/whl/${TORCH_VARIANT} && \
    pip3 install --no-cache-dir \
        "numpy<2" \
        ultralytics \
        opencv-python \
        scipy

RUN apt-get update && apt-get install -y --no-install-recommends \
    libsm6 \
    libice6 \
    libxcb1 \
    libx11-6 \
    libx11-xcb1 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libdbus-1-3 \
    libfontconfig1 \
    libfreetype6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /object_state_estimator

CMD ["tail", "-f", "/dev/null"]
