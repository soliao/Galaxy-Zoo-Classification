# Kaggle-Galaxy-Zoo-Classification
Classify the morphologies of distant galaxies









## Old Galaxy Zoo Classification

Below shows the performance of using ResNet-50 and Vision Transformer (ViT) to classify old galaxy zoo dataset (61,578 images in total).

## ResNet-50

Training acc: 0.830
Validation acc: 0.813
Test acc: 0.8241


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
| Total trainable params | 10,926,085 | 10,019,845 | 10,188,805 | 10,346,245 | 11,909,125 |


### Starting learning rate (lr)

| Model | benchmark | lr_1e2 | lr_5e3 | lr_1e3 | lr_5e4 | lr_1e4 | lr_5e5 |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | **0.7736** | 0.6133 | 0.6240 | 0.7103 | 0.7539 | 0.7554 | 0.7222 |
| **Val Acc** | **0.7627** | 0.6119 | 0.6226 | 0.7040 | 0.7447 | 0.7460 | 0.7179 |
| **Test Acc** | **0.7625** | 0.6164 | 0.6256 | 0.7094 | 0.7450 | 0.7488 | 0.7229 |
| PATCH_SIZE | 28 | - | - | - | - | - | - |
| SEQ_LEN | 65 | -  | -  | -  | - | - | - |
| DEPTH | 12 | - | - | - | - | - | -  |
| HIDDEN_DIM | 256 | - | - | - | - | - | - |
| k_DIM | 64 | - | - | - | - | - | - |
| NUM_HEADS | 8 | - | - | - | - | - | - |
| BATCH_SIZE | 64 | - | - | - | - | - | - |
| lr | 3e-4 | 1e-2 | 5e-3 | 1e-3 | 5e-4 | 1e-4 | 5e-5 |
| step_size | 1 | - | - | - | - | - | - |
| gamma | 0.9 | - | - | - | - | - | - |
| best_epoch | 32 | 25 | 42 | 37 | 52 | 39 | 42 |
| stop_epoch | 42 | 35 | 52 | 47 | 62 | 49 | 52 |
| Total trainable params | 10,188,805 | - | - | - | - | - | -  |


### Learning rate decay step size (step_size)

| Model | benchmark | ss_5 | ss_10 | ss_20 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | 0.7736 | 0.7916 | 0.7869 | 0.7861 |
| **Val Acc** | 0.7627 | 0.7728 | 0.7721 | 0.7715 |
| **Test Acc** | 0.7625 | **0.7731** | 0.7720 | 0.7725 |
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
| best_epoch | 32 | 56 | 52 | 62 |
| stop_epoch | 42 | 66 | 62 | 72 |
| Total trainable params | 10,188,805 | - | - | - |


### Depth

| Model | benchmark | depth_2 | depth_4 | depth_6 | depth_8 | depth_24 |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | **0.7736** | 0.7434 | 0.7626 | 0.7717 | 0.7722 | 0.7514 |
| **Val Acc** | **0.7627** | 0.7354 | 0.7533 | 0.7589 | 0.7597 | 0.7408 |
| **Test Acc** | **0.7625** | 0.7375 | 0.7589 | 0.7619 | 0.7624 | 0.7431 |
| PATCH_SIZE | 28 |  |  |  |  |  |
| SEQ_LEN | 65 |  |  |  |  |  |
| DEPTH | 12 | 2 | 4 | 6 | 8 | 24 |
| HIDDEN_DIM | 256 | | | |  |  |
| k_DIM | 64 | | | |  |  |
| NUM_HEADS | 8 | | | |  |  |
| BATCH_SIZE | 64 | | | |  |  |
| lr | 3e-4 | | | |  |  |
| step_size | 1 | | | |  |  |
| gamma | 0.9 | | | |  |  |
| best_epoch | 32 | 36 | 44 | 39 | 57 | 40 |
| stop_epoch | 42 | 46 | 54 | 49 | 67 | 50 |
| Total trainable params | 10,346,245 | 2,215,685 | 3,810,309 | 5,404,933 | 6,999,557 | 19,756,549 |


### Hidden dim

| Model | benchmark | hiddendim_128 | hiddendim_512 | hiddendim_1024 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | 0.7916 | 0.7923 |  |  |
| **Val Acc** | 0.7728 | 0.7741 |  |  |
| **Test Acc** | **0.7731** | 0.7746 |  |  |
| PATCH_SIZE | 28 | - | - | -  |
| SEQ_LEN | 65 | -  | -  | -  |
| DEPTH | 12 | - | - | - |
| HIDDEN_DIM | 256 | 128 | - | - |
| k_DIM | 64 | - | - | - |
| NUM_HEADS | 8 | - | - | - |
| BATCH_SIZE | 64 | - | - | - |
| lr | 3e-4 | - | - | - |
| step_size | 5 | - | - | - |
| gamma | 0.9 | - | - | - |
| best_epoch | 56 | 54 |  |  |
| stop_epoch | 66 | 64 |  |  |
| Total trainable params | 10,188,805 | 2,785,029 | - | - |


### Dropout

| Model | benchmark | dropout_05 | dropout_01 |
| ----------- | ----------- | ----------- | ----------- |
| **Train Acc** | 0.7923 | 0.7647 |  |
| **Val Acc** | 0.7741 | 0.7591 |  |
| **Test Acc** | **0.7746** | 0.7554 |  |
| PATCH_SIZE | 28 | - | - |
| SEQ_LEN | 65 | -  | -  |
| DEPTH | 12 | - | - |
| HIDDEN_DIM | 128 |  | - |
| k_DIM | 64 | - | - |
| NUM_HEADS | 8 | - | - |
| BATCH_SIZE | 64 | - | - |
| lr | 3e-4 | - | - |
| step_size | 5 | - | - |
| gamma | 0.9 | - | - |
| dropout | 0.0 | 0.5 | 0.1 |
| best_epoch | 54 | 31 |  |
| stop_epoch | 64 | 41 |  |
| Total trainable params | 2,785,029 | - | - |
