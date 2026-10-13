# First PyTorch test: one matrix multiply on the Intel Arc GPU (XPU).
import time
import torch

device = "xpu" if torch.xpu.is_available() else "cpu"
print("PyTorch", torch.__version__, "on", device)

a = torch.rand(2000, 2000, device=device)
start = time.time()
c = a @ a
if device == "xpu":
    torch.xpu.synchronize()
print("sum:", c.sum().item(), f"({time.time() - start:.3f}s)")
