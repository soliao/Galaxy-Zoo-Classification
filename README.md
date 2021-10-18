# Galaxy Morphological Classification with Efficient Vision Transformer

Repository of the paper **Galaxy Morphological Classification with Efficient Vision Transformer** by Joshua Yao-Yu Lin, Song-Mao Liao, Hung-Jin Huang, Wei-Ting Kuo, and Olivia Hsuan-Min Ou.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2110.01024-yellowgreen.svg)](https://arxiv.org/abs/2110.01024)

[![vit-oo.png](https://i.postimg.cc/dt1gky53/vit-oo.png)](https://postimg.cc/F1MTw75X)

## Abstract
Quantifying the morphology of galaxies has been an important task in astrophysics
to understand the formation and evolution of galaxies. In recent years, the data size
has been dramatically increasing due to several on-going and upcoming surveys.
Labeling and identifying interesting objects for further investigations has been
explored by citizen science through the Galaxy Zoo Project and by machine learning
in particular with the convolutional neural networks (CNNs). In this work, we
explore the usage of Vision Transformer (ViT) for galaxy morphology classification
for the first time. We show that ViT could reach competitive results compared with
CNNs, and is specifically good at classifying smaller-sized and fainter galaxies.
With this promising preliminary result, we believe the ViT network architecture can
be an important tool for galaxy morphological classification for the next generation
surveys. We plan to open source our repository in the near future.

## Dataset

[Galaxy Zoo dataset](https://data.galaxyzoo.org/)

The galaxy dataset used in this study is based on the Galaxy Zoo 2 Project2 (GZ2)[38], with the
morphological information drawn from the catalog of Hart et al. [39], and the galaxy images downloaded from kaggle3. The size of each image is 424  424  3 pixels, with the color channels
corresponding the g, r, i filters of the SDSS[9].
The morphological classification labels of galaxies can be derived by applying thresholds on a series
of voting questions answered by participants in GZ2. Following the criteria suggested in [38, 40], we
construct a clean galaxy dataset with eight distinct classes and label them from 07 in the order of:
round elliptical, in-between elliptical, cigar-shaped elliptical, edge-on, barred spiral, unbarred spiral,
irregular and merger galaxies. Fig. 2 shows example galaxy images of each morphological class.
Our final baseline dataset consists of 155,951 images, which is more than five times larger compared
with previous machine learning studies on galaxy classification problems [26, 40, 41].
We split the data into 64% train set, 16% validation set, and 20% test set. We crop images into
224  224  3, and use data augmentation techniques by flipping and rotating the images. We
normalize pixel values in each color channel by the mean ([0:094; 0:0815; 0:063]) and the standard
deviation ([0:1303; 0:11; 0:0913]) obtained from the dataset.


## Class labels

We classified the galaxies into 8 categories based on the morphologies:

[![vit-fig2.png](https://i.postimg.cc/Ls5zjjJC/vit-fig2.png)](https://postimg.cc/HJGcgc4X)

## Code

## Data loader

```python
## Custom Galaxy Zoo 2 Dataset
class GalaxyZooDataset(Dataset):
    """Galaxy Zoo Dataset"""

    def __init__(self, csv_file, images_dir, transform=None):
        """
        Args:
            csv_file (string): path to the label csv
            images_dir (string): path to the dir containing all images
            transform (callable, optional): transform to apply
        """
        self.labels_df = pd.read_csv(csv_file)
        self.labels_df = self.labels_df[['galaxyID', 'label1']].copy()

        self.images_dir = images_dir
        self.transform = transform

    def __len__(self):
        """
        Returns the size of the dataset
        """
        return len(self.labels_df)

    def __getitem__(self, idx):
        """
        Get the idx-th sample.
        Outputs the image (channel first), true label, and the galaxy ID
        """
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # galaxy ID
        galaxyid = self.labels_df.iloc[idx, 0].astype(str)
        # path of the image
        image_path = os.path.join(self.images_dir, galaxyid + '.jpg')
        # read the image
        image = Image.open(image_path)
        # apply transform (optional)
        if self.transform is not None:
            image = self.transform(image)
        # read the true label
        label = int(self.labels_df.iloc[idx, 1])

        return image, label, int(galaxyid)
```

## Data transform

```python
def create_data_transforms(is_for_inception=False):
    """
    Create Pytorch data transforms for the GalaxyZoo datasets.
    Args:
        is_for_inception (bool): True for inception neural networks
    Outputs:
        train_transform: transform for the training data
        valid_transform: tranform for the validation data
        test_transform: transform for the testing data
    """
    if is_for_inception:
        input_size = 299
    else:
        input_size = 224

    # transforms for training data
    train_transform = transforms.Compose([transforms.CenterCrop(input_size),
                                          transforms.RandomRotation(90),
                                          transforms.RandomHorizontalFlip(),
                                          transforms.RandomVerticalFlip(),
                                          transforms.RandomResizedCrop(input_size, scale=(0.8, 1.0), ratio=(0.99, 1.01)),
                                          transforms.ToTensor(),
                                          transforms.Normalize([0.094, 0.0815, 0.063], [0.1303, 0.11, 0.0913])])

    # transforms for validation data
    valid_transform = transforms.Compose([transforms.CenterCrop(input_size),
                                          transforms.ToTensor(),
                                          transforms.Normalize([0.094, 0.0815, 0.063], [0.1303, 0.11, 0.0913])])

    # transforms for test data
    test_transform = transforms.Compose([transforms.CenterCrop(input_size),
                                         transforms.ToTensor(),
                                         transforms.Normalize([0.094, 0.0815, 0.063], [0.1303, 0.11, 0.0913])])


    return train_transform, valid_transform, test_transform
```

## Models

### Vision Transformer

**Parameters**
```
**gz2_vit_09172021_0000**

PATCH_SIZE = 28
DEPTH = 12
HIDDEN_DIM = 128
K_DIM = 64
NUM_HEADS = 8

LR = 3e-4
STEP_SIZE = 5
GAMMA = 0.9
MAX_EPOCH = 200

LIN_DROPOUT = 0.1

class_weights = [1., 1., 1., 1., 1., 1., 1., 1.]
```

**Results**

(Disconnection during training)\
Train Accuracy = 0.8193\
Validation Accuracy = 0.8035\
Test Accuracy = 0.8055\
Test Recall = 0.7233\
Test F1 Score = 0.7323

[![gz2-vit-09172021-0000-cm.png](https://i.postimg.cc/V6YVSVfW/gz2-vit-09172021-0000-cm.png)](https://postimg.cc/94npK1qD)

### Resnet-50

**Parameters**
```
BATCH_SIZE = 64

LR = 5e-5
STEP_SIZE = 10
GAMMA = 0.1
MAX_EPOCH = 200

class_weights = [1., 1., 1., 1., 1., 1., 1., 1.]
```
**Results**

Train Accuracy = 0.8662\
Validation Accuracy = 0.8534\
Test Accuracy = 0.8558\
Test Recall = 0.7920\
Test F1 Score = 0.8007

[![gz2-resnet50-A-cm.png](https://i.postimg.cc/qR7cBPdV/gz2-resnet50-A-cm.png)](https://postimg.cc/NyW2pPMp)
