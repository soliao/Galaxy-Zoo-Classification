# Kaggle-Galaxy-Zoo-Classification
Classify the morphologies of distant galaxies


## ResNet-50

Training acc: 0.830
Validation acc: 0.813
Test acc: 






## Vision Transformer

### Patch Size

| Model | pathsize_8 | pathsize_16 | pathsize_28 | pathsize_32 | pathsize_56 |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | 0.7000 | 0.7465 | **0.7736** | 0.7697 | 0.7494 |
| **Val Acc** | 0.6904 | 0.7289 | **0.7627** | 0.7579 | 0.7387 |
| **Test Acc** | 0.7020 | 0.7373 | **0.7625** | 0.7623 | 0.7408 |
| PATCH_SIZE | 8 | 16 | 28 | 32 | 56 |
| SEQ_LEN | 785 | 197 | 65 | 50 | 17 |
| DEPTH | 12 | - | - | - | - |
| HIDDEN_DIM | 256 | - | - | - | - |
| k_DIM | 64 | - | - | - | - |
| NUM_HEADS | 8 | - | - | - | - |
| BATCH_SIZE | 64 | - | - | - | - |
| lr | 3e-4 | - | - | - | - |
| step_size | 1 | - | - | - | - |
| gamma | 0.9 | - | - | - | - |
| best_epoch | 39 | 42 | 44 | 32 | 39 |
| stop_epoch | 49 | 52 | 54 | 42 | 49 |
| Total trainable params | 10926085 | 10019845 | 10188805 | 10346245 | 11909125 |


### Learning rate decay step size (step_size)

| Model | benchmark | ss_5 | ss_10 | ss_20 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | **0.7736** |  |  |  |
| **Val Acc** | **0.7627** |  |  |  |
| **Test Acc** | **0.7625** |  |  |
| PATCH_SIZE | 28 | - | - | -  |
| SEQ_LEN | 65 | -  | -  | -  |
| DEPTH | 12 | - | - | - |
| HIDDEN_DIM | 256 | - | - | - |
| k_DIM | 64 | - | - | - |
| NUM_HEADS | 8 | - | - | - |
| BATCH_SIZE | 64 | - | - | - |
| lr | 3e-4 | - | - | - |
| step_size | 1 | 5 | 10 | 20 |
| gamma | 0.9 | - | - | - |
| best_epoch | 32 |  |  |  |
| stop_epoch | 42 |  |  |  |
| Total trainable params | 10188805 | - | - | - |


### Depth

| Model | benchmark | depth_8 | depth_24 | depth_32 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | **0.7697** |  |  |  |
| **Val Acc** | **0.7579** |  |  |  |
| **Test Acc** | **0.7623** |  |  |
| PATCH_SIZE | 32 |  |  |  |
| SEQ_LEN | 50 |  |  |  |
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
| Total trainable params | 10346245 |  |  |  |
