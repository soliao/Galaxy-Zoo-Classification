"""
This file creates the Pytorch dataset from the Galaxy Zoo dataset on Kaggle:

Data source: https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data

This file was inspired and modified from the following resources:

1. https://pytorch.org/tutorials/beginner/data_loading_tutorial.html

2. https://github.com/joshualin24/vit-pytorch/blob/main/examples/cats_and_dogs.ipynb


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from PIL import Image

import torch
from torch.utils.data import Dataset
from torchvision import transforms


## Custom Galaxy Zoo Dataset

class GalaxyZooDataset(Dataset):
    """Galaxy Zoo Dataset"""

    def __init__(self, csv_file, images_dir, transform=None):
        """
        Args:
            csv_file (string): path to the label csv
            images_dir (string): path to the dir containing all images
            transform (callable, optional): transform to apply
        """
        self.labels = pd.read_csv(csv_file)
        self.images_dir = images_dir
        self.transform = transform
    
    def __len__(self):
        """
        Returns the size of the dataset
        """
        return len(self.labels)

    def __getitem__(self, idx):
        """
        Get the idx-th sample.
		Outputs the image (channel first) and the true label
        """
        if torch.is_tensor(idx):
            idx = idx.tolist()
	
		# path of the image
        image_path = os.path.join(self.images_dir, self.labels.iloc[idx, 0].astype(str) + '.jpg')
		
		# read the image
        image = Image.open(image_path)
		
		# apply transform (optional)
        if self.transform:
            image = self.transform(image)
		
		# read the true label
        label = self.labels.iloc[idx, 1]

        return image, label