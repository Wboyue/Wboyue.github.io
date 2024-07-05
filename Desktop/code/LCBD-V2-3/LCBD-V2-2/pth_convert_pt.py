#
import torch
import torchvision

# import torch.nn as nn
# import torch.nn.functional as F
# import torchvision.models as models
# from torchsummary import summary
#
#
model = torch.load("mobilenetv3_small_67.4.pth")
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#
# #summary(model, input_size=(1, 480, 640))
# model = model.to(device)
# traced_script_module = torch.jit.trace(model, torch.ones(1, 3, 480, 640).to(device))
# traced_script_module.save("mobilenetv3_small_67_4.pt")
#


# An instance of your model.
model = torchvision.models.mobilenet_v3_small()


# An example input you would normally provide to your model's forward() method.
example = torch.rand(1, 3, 480, 640)

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)
traced_script_module.save("traced_resnet_model.pt")
