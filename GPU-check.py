# GPUが使用可能か確認するスクリプト
import torch

if torch.cuda.is_available():
    print("CUDA is available. GPU is ready for use.")
else:
    print("CUDA is not available. GPU cannot be used.")


import torch
import torchvision

print("torch version:", torch.__version__)
print("torchvision version:", torchvision.__version__)