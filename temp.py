# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import torch
from torch.utils.data import DataLoader
import torchvision.dataaets as dsets
import torchvision.transform as transform
batch_size=100
train_dataset=dsets.MNIST(root='/ml/pymnist',
                          train=True,
                          tranform=None,
                          download=True)
test_dataset=dsets.MNIST(root='/ml/pymnist',
                         train=False,
                         transform=None,
                         download=True)
train_loader=torch.utils.data.DataLoader(dataset=train_dataset,
                                         batch_size=batch_size,
                                         shuffle=True)
test_loader=torch.utils.data.DataLoader(dataset=test_dataset,
                                         batch_size=batch_size,
                                         shuffle=True)