#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

xhost +local:docker || true

docker rm -f object_state_estimator 2>/dev/null || true

docker run -d \
    --name object_state_estimator \
    --hostname object_state_estimator \
    --device /dev/video2 \
    -e DISPLAY="$DISPLAY" \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v "$SCRIPT_DIR":/object_state_estimator \
    "$@" \
    object_state_estimator:latest
