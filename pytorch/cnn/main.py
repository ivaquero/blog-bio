import torch
from torch import nn
from torch import optim
from torch.utils import data
from torchvision import transforms
from torchvision.datasets import *
from lenet5 import LeNet5
from resnet import ResNet18


def main():
    image_path = '../../../datasets/torch'

    cifar_train = CIFAR10(image_path,
                          train=True,
                          transform=transforms.Compose([
                              transforms.Resize((32, 32)),
                              transforms.ToTensor()
                          ]),
                          download=True)
    cifar_test = CIFAR10(image_path,
                         train=True,
                         transform=transforms.Compose([
                             transforms.Resize((32, 32)),
                             transforms.ToTensor()
                         ]),
                         download=True)

    batch_size = 32
    cifar_train = data.DataLoader(cifar_train,
                                  batch_size=batch_size,
                                  shuffle=True)
    cifar_test = data.DataLoader(cifar_test,
                                 batch_size=batch_size,
                                 shuffle=True)

    x, label = iter(cifar_train).next()

    print(f'x: {x.shape}')
    print(f'label: {label.shape}')

    # model = LeNet5()
    model = ResNet18()
    print(model)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    # train
    model.train()
    for epoch in range(1_000):
        for batch_ind, (x, label) in enumerate(cifar_train):
            # [batch_size, 3, 32, 32]
            logits = model(x)
            # [batch_size, 10]
            loss = criterion(logits, label)
            #
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f'epoch: {epoch}, loss: {loss.item()}')

    # test
    model.eval()
    with torch.no_grad():
        total_correct = 0
        total_num = 0
        for x, label in cifar_test:
            logits = model(x)
            # [batch_size]
            pred = logits.argmax(dim=1)
            total_correct += torch.eq(pred, label).float().sum().item()
            total_num += x.size(0)

    acc = total_correct / total_num
    print(f'{epoch} acc: {acc}')


if __name__ == '__main__':
    main()
