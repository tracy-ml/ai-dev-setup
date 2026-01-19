# AI Development Environment Setup

This repository documents a reproducible Ubuntu-based AI development
environment with NVIDIA GPU acceleration.

## What this repo proves

- NVIDIA driver + CUDA runtime are correctly installed
- PyTorch (CUDA 12.8, Blackwell / sm_120) works on RTX 5090
- GPU workloads run both natively and inside Docker containers
- Environment can be reproduced via conda or Docker

## Structure

```
ai-dev-setup/
├── environment.yml # Conda environment definition
├── docker/
│ └── Dockerfile # GPU-enabled Docker image
└── validation/
└── gpu_test.py # CUDA validation script
```

## Reproduce conda environment

```bash
conda env create -f environment.yml
conda activate ai
python validation/gpu_test.py
```

## Test GPU inside Docker

```bash
docker build -t ai-dev-gpu-test -f docker/Dockerfile .
docker run --rm --gpus all ai-dev-gpu-test
```

## Notes

- Host system: Ubuntu 24.04
- GPU: NVIDIA GeForce RTX 5090
- CUDA runtime: 12.8