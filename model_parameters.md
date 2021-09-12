## Resnet-50


## ViT

**gz2_vit_09112021_1110**
```
patch_size = 28
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 16
dropout = 0.1
batch_size = 64
lr = 0.0003
step_size = 5
gamma = 0.9
max_epoch = 200
===============================
Number of trainable parameters: 2785416
===============================
transform mean = [0.094, 0.0815, 0.063]
transform std = [0.1303, 0.11, 0.0913]
```
0.8076 / 0.7979 / 0.7959


**gz2_vit_09092021_2125**
```
patch_size = 14
depth = 12
hidden_dim = 256
k_dim = 64
num_heads = 8
dropout = 0.1
batch_size = 64
lr = 0.0003
step_size = 5
gamma = 0.9
max_epoch = 200
===============================
Number of trainable parameters: 10082056
===============================
transform mean = [0.094, 0.0815, 0.063]
transform std = [0.1303, 0.11, 0.0913]
===============================
torch.FloatTensor([4.6, 4.0, 20.9, 9.6, 7.7, 5.1, 26.5, 73.3])
```

**gz2_vit_09092021_0940**
```
patch_size = 14
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 8
dropout = 0.1
batch_size = 64
lr = 0.0003
step_size = 5
gamma = 0.9
max_epoch = 200
===============================
Number of trainable parameters: 2879112
===============================
transform mean = [0.094, 0.0815, 0.063]
transform std = [0.1303, 0.11, 0.0913]
===============================
class_weights = torch.FloatTensor([1., 1., 2., 1., 1., 1., 2., 2.])
```

0.819 / 0.8021 / 0.8008

[![gz2-vit-09092021-0940.png](https://i.postimg.cc/rwTWcqSQ/gz2-vit-09092021-0940.png)](https://postimg.cc/0btr0RXw)



**gz2_vit_09092021_0937**
```
patch_size = 28
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 8
dropout = 0.1
batch_size = 64
lr = 0.001
step_size = 5
gamma = 0.9
max_epoch = 200
===============================
Number of trainable parameters: 2785416
===============================
transform mean = [0.094, 0.0815, 0.063]
transform std = [0.1303, 0.11, 0.0913]
===============================
class_weights = torch.FloatTensor([4.6, 4.0, 20.9, 9.6, 7.7, 5.1, 26.5, 73.3])
```

0.6318 / 0.6585 / 0.6504

[![gz2-vit-09092021-0937.png](https://i.postimg.cc/RCHxYp9Y/gz2-vit-09092021-0937.png)](https://postimg.cc/CdS2BNRC)

**gz2_vit_09082021_1211**
```
patch_size = 28
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 8
dropout = 0.1
batch_size = 64
lr = 0.0003
step_size = 5
gamma = 0.9
max_epoch = 200
===============================
Number of trainable parameters: 2785416
===============================
transform mean = [0.094, 0.0815, 0.063]
transform std = [0.1303, 0.11, 0.0913]
===============================
class_weights = torch.FloatTensor([4.6, 4.0, 20.9, 9.6, 7.7, 5.1, 26.5, 73.3])
```

0.7618 / 0.7654 / 0.7691

[![gz2-vit-09082021-1211.png](https://i.postimg.cc/RZLgG6qF/gz2-vit-09082021-1211.png)](https://postimg.cc/QFVgdMQG)

[![gz2-vit-09082021-1211-metrics.png](https://i.postimg.cc/Fs2MwL9V/gz2-vit-09082021-1211-metrics.png)](https://postimg.cc/F7VCL1kY)

**gz2_vit_09072021_2341**
```
patch_size = 28
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 8
dropout = 0.1
batch_size = 64
lr = 0.0003
step_size = 5
gamma = 0.9
max_epoch = 200
===============================
transform mean = [0.094, 0.0815, 0.063]
transform std = [0.1303, 0.11, 0.0913]
===============================
Number of trainable parameters: 2785416
```

**gz2_vit_09072021_2155**
```
patch_size = 28
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 8
dropout = 0.2
batch_size = 64
lr = 5e-05
step_size = 20
gamma = 0.1
max_epoch = 200
===============================
Number of trainable parameters: 2785416
```

0.7557 / 0.7602 / 0.7592

[![gz2-vit-09072021-2155.png](https://i.postimg.cc/8cQNZ3dH/gz2-vit-09072021-2155.png)](https://postimg.cc/1nHktvjn)

**gz2_vit_09072021_1409**
```
patch_size = 28
depth = 12
hidden_dim = 512
k_dim = 64
num_heads = 8
dropout = 0.1
batch_size = 64
lr = 5e-05
step_size = 10
gamma = 0.1
max_epoch = 200
===============================
Number of trainable parameters: 39153672
```
[![gz2-vit-09072021-1409.png](https://i.postimg.cc/7ZXQVJNs/gz2-vit-09072021-1409.png)](https://postimg.cc/gxXDcJQ8)


**gz2_vit_09072021_1048**
```
patch_size = 28
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 8
dropout = 0.2
batch_size = 64
lr = 5e-05
step_size = 10
gamma = 0.1
max_epoch = 200
===============================
Number of trainable parameters: 2785416
```
0.7171 / 0.7258 / 0.7252

[![gz2-vit-09072021-1048.png](https://i.postimg.cc/Dzfny2tb/gz2-vit-09072021-1048.png)](https://postimg.cc/0z4LVq58)

**gz2_vit_09072021_0243**
```
patch_size = 28
depth = 12
hidden_dim = 128
k_dim = 64
num_heads = 8
dropout = 0.5
batch_size = 64
lr = 5e-05
step_size = 10
gamma = 0.1
max_epoch = 200
===============================
Number of trainable parameters: 2785416
```
0.6900 / 0.6996 / 0.6959

[![gz2-vit-09072021-0243.png](https://i.postimg.cc/D0Df4rbL/gz2-vit-09072021-0243.png)](https://postimg.cc/m1YW0Fjg)


**gz2_vit_09072021_0252**
```
patch_size = 28
depth = 12
hidden_dim = 512
k_dim = 64
num_heads = 8
dropout = 0.2
batch_size = 64
lr = 0.0003
step_size = 10
gamma = 0.1
max_epoch = 200
===============================
Number of trainable parameters: 39153672
```
0.6391 / 0.6500 / 0.6398

[![gz2-vit-09072021-0252.png](https://i.postimg.cc/TwPPGtTr/gz2-vit-09072021-0252.png)](https://postimg.cc/qt9rxXhR)
