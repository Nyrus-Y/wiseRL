
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import example.dqn.config as config

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(config.N_STATES, 512)  
        self.fc1.weight.data.normal_(0, 0.1) 
        self.out = nn.Linear(512, config.N_ACTIONS) 
        self.out.weight.data.normal_(0, 0.1)
        
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        actions_value = self.out(x)
        return actions_value