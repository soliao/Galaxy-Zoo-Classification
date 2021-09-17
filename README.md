# Kaggle-Galaxy-Zoo-Classification
Classify the morphologies of distant galaxies

---

## Galaxy Zoo 2 Dataset

[Galaxy Zoo dataset](https://data.galaxyzoo.org/)

The file `GalaxyZooDataset` contains the Galaxy Zoo 2 dataset object.


## Class labels

We classified the galaxies into 8 categories based on the morphologies:

| Class | Description | Example images |
| ----------- | ----------- | ----------- |
| 0 | Round Elliptical | |
| 1 | In-between Elliptical | |
| 2 | Cigar-shaped Elliptical | |
| 3 | Edge-on Spiral | |
| 4 | Barred Spiral | |
| 5 | Unbarred Spiral | |
| 6 | Irregular | |
| 7 | Merger | |


## Models

### Vision Transformer

**Parameters**

**Results**



### Resnet-50

**Parameters**
```
BATCH_SIZE = 64

LR = 5e-5
STEP_SIZE = 10
GAMMA = 0.1
MAX_EPOCH = 200
```
**Results**

Train Accuracy = 0.8662\
Validation Accuracy = 0.8534\
Test Accuracy = 0.8558\
Test Recall = 0.7920\
Test F1 Score = 0.8007

[![gz2-resnet50-A-cm.png](https://i.postimg.cc/qR7cBPdV/gz2-resnet50-A-cm.png)](https://postimg.cc/NyW2pPMp)
