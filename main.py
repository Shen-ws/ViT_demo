import torch
#检查cuda是否可以使用

print (torch.cuda.is_available())
#查看当前gpu索引号
print(torch.cuda.current_device())
#查看当前cuda流
torch.cuda.current_stream(device=0)
#选择device
torch.cuda.device(1)
#查看有多少个GPU设备
torch.cuda.device_count()
#查看gpu的容量
print(torch.cuda.get_device_capability(device=0))

