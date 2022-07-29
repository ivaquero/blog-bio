from torch import nn
import torch


class ResBlock(nn.Module):

    def __init__(self, chn_in, chn_out, stride=1):
        super(ResBlock, self).__init__()
        self.conv1 = nn.Conv2d(chn_in,
                               chn_out,
                               kernel_size=3,
                               stride=stride,
                               padding=1)
        self.bn1 = nn.BatchNorm2d(chn_out)
        self.conv2 = nn.Conv2d(chn_out,
                               chn_out,
                               kernel_size=3,
                               stride=1,
                               padding=1)
        self.bn2 = nn.BatchNorm2d(chn_out)

        self.extra = nn.Sequential()
        if chn_out != chn_in:
            self.extra = nn.Sequential(
                nn.Conv2d(chn_in, chn_out, kernel_size=1, stride=stride),
                nn.BatchNorm2d(chn_out))

    def forward(self, x):
        # out: [batch_size, channel, h, w]
        out = nn.functional.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        # [batch_size, chn_in, h, w] => [batch_size, chn_out, h, w]
        out = out + self.extra(x)

        return out


class ResNet18(nn.Module):

    def __init__(self):
        super(ResNet18, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=0),
            nn.BatchNorm2d(64))
        # [batch_size, 64, h, w] => [batch_size, 128, h, w]
        self.block1 = ResBlock(64, 128, stride=2)
        # [batch_size, 128, h, w] => [batch_size, 256, h, w]
        self.block2 = ResBlock(128, 256, stride=2)
        # [batch_size, 256, h, w] => [batch_size, 512, h, w]
        self.block3 = ResBlock(256, 512, stride=2)
        # [batch_size, 512, h, w] => [batch_size, 1024, h, w]
        self.block4 = ResBlock(512, 512, stride=2)

        self.outlayer = nn.Linear(512 * 1 * 1, 10)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        # out: [batch_size, 64, h, w] => [batch_size, 1024, h, w]
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        x = self.block4(x)

        print(f"after conv: {x.shape}")
        x = nn.functional.adaptive_avg_pool2d(x, [1, 1])
        print(f"after pool: {x.shape}")
        x = x.view(x.size(0), -1)
        x = self.outlayer(x)

        return x
