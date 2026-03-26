import torch
import torch.nn as nn
import torchvision.models as models

class IQAModel(nn.Module):
    def __init__(self):
        super(IQAModel, self).__init__()
        self.base = models.resnet18(pretrained=True)
        self.base.fc = nn.Sequential(
            nn.Linear(self.base.fc.in_features, 1),
            nn.Sigmoid()  # 🔥 forces output between 0 and 1
        )

    def forward(self, x):
        return self.base(x)