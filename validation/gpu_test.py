import torch

print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))

# Real kernel execution
x = torch.randn(2048, 2048, device="cuda")
y = x @ x
print("CUDA matmul OK, mean:", y.mean().item())