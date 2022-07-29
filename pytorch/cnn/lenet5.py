import torch
from torch import nn


class LeNet5(nn.Module):

    def __init__(self):
        super(LeNet5, self).__init__()
        self.conv_unit = nn.Sequential(
            # x: (batch_size, 3, 32, 32) => (batch_size, 6, 5, 5)
            nn.Conv2d(3, 6, kernel_size=5, stride=1, padding=0),
            nn.AvgPool2d(kernel_size=2, stride=2),
            #
            nn.Conv2d(6, 16, kernel_size=5, stride=1, padding=0),
            nn.AvgPool2d(kernel_size=2, stride=2, padding=0),
        )

        # flatten
        self.fc_unit = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10),
        )
        # [batch_size, 3, 32, 32]
        tmp = torch.randn(2, 3, 32, 32)
        out = self.conv_unit(tmp)
        # [batch_size, 16, 5, 5]
        print(f"conv_out: {out.shape}")

    def forward(self, x):
        batch_size = x.size(0)
        # [batch_size, 3, 32, 32] => [batch_size, 16, 5, 5]
        x = self.conv_unit(x)
        # [batch_size, 16, 5, 5] => [batch_size, 16 * 5 * 5]
        x = x.view(batch_size, 16 * 5 * 5)
        #
        logits = self.fc_unit(x)
        return logits
