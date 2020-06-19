import os
import os.path as osp
import random
import xml.etree.ElementTree as ET 
import cv2
import torch.utils.data as data
import torch
import torch.nn as nn
from torch.autograd import Function
import numpy as np
import pandas as pd
import itertools
from math import sqrt

torch.manual_seed(1234)
np.random.seed(1234)
random.seed(1234)
