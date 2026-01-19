FROM nvidia/cuda:12.8.0-base-ubuntu24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip \
    && pip3 install torch --index-url https://download.pytorch.org/whl/cu128

WORKDIR /workspace

COPY validation/gpu_test.py /workspace/gpu_test.py

CMD ["python3", "gpu_test.py"]