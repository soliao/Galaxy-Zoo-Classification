"""
This file creates the Pytorch data transform for the Galaxy Zoo dataset on Kaggle:

Data source: https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data

Pytorch torchvision transforms: https://pytorch.org/vision/stable/transforms.html

"""

from torchvision import transforms


def create_data_transforms(is_for_inception=False):
    """
    Create Pytorch data transforms for the GalaxyZoo datasets.
    Args:
        is_for_inception (bool): True for inception neural networks
    Outputs:
        train_transform: transform for the training data
        test_transform: transform for the testing data
    """
    if is_for_inception:
        input_size = 299
    else:
        input_size = 224

    train_transform = transforms.Compose([transforms.Resize((input_size, input_size)),
                                          transforms.RandomResizedCrop(input_size, scale=(0.8, 1.0),
                                                                       ratio=(0.999, 1.001)),
                                          transforms.RandomHorizontalFlip(),
                                          transforms.RandomVerticalFlip(),
                                          transforms.ToTensor(),
                                          transforms.Normalize([0, 0, 0], [255, 255, 255]),
                                          transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    test_transform = transforms.Compose([transforms.Resize((input_size, input_size)),
                                         transforms.ToTensor(),
                                         transforms.Normalize([0, 0, 0], [255, 255, 255]),
                                         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    return train_transform, test_transform