# Kaggle-Galaxy-Zoo-Classification
Classify the morphologies of distant galaxies


## ResNet-50

Training acc: 0.830
Validation acc: 0.813
Test acc: 






## Vision Transformer

### Patch Size

| Model | benchmark | pathsize_8 | pathsize_16 | pathsize_56 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | **0.7697** | 0.7000 |  |  |
| **Val Acc** | **0.7579** | 0.6904 |  |  |
| **Test Acc** | **0.7623** | 0.7020 |  |
| PATCH_SIZE | 32 | 8 | 16 | 56 |
| SEQ_LEN | 50 | 785 | 197 | 17 |
| DEPTH | 12 | | | |
| HIDDEN_DIM | 256 | | | |
| k_DIM | 64 | | | |
| NUM_HEADS | 8 | | | |
| BATCH_SIZE | 64 | | | |
| lr | 3e-4 | | | |
| step_size | 1 | | | |
| gamma | 0.9 | | | |
| best_epoch | 32 | ? | ? | ? |
| stop_epoch | 42 | ? | ? | ? |
| Total trainable params | 10346245 | 10926085 | 10019845 | 11909125 |

