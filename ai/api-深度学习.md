# 深度学习 API

## 1. 张量

### 1.1. 生成

- `rand()`
- `full()`
- `sparse_coo_tensor(index, value, size)`：存储非零元素的坐标和值

### 1.2. 类型

- 类型转换
  - 构造函数（constructor）
    - 数据类型默认为`float32`
    - `.Tensor()`
  - 工厂函数（factory）
    - 数据类型根据输入推断
    - 副本型：修改原数组，不影响生成数据
      - `.tensor()`：
      - `.numpy()`
    - 共享型
      - `.as_tensor()`
      - `.from_numpy()`
- 数值转换
  - `.to_dense()`

### 1.3. 访问

- 性质
  - `.shape()`
  - `.numel()`：number of elements
  - `len(t.shape)`：rank
- 判断
  - `isfinite()`、`isinf()`、`isnan()`
  - `is_tensor()`、`is_storage()`

### 1.4. 重塑

- 变形
  - `.reshape()`
  - `.squeeze()`：去除所有长度为 1 的轴，相当于减少多余的 rank
  - `.unsqueeze(dim)`：增加 1 个长度为 1 的轴，相当于在指定维度上增加 rank
  - `.flatten(start_dim)`：只保留 1 个轴，相当于 `reshape(1, -1)` + `squeeze()`
  - `.transpose()`
  - `.flip()`、`.rot90)`
- 组合
  - `cat()`：以现有维度拼接
  - `stack()`：以新维度拼接，rank+1
  - `gather()`
- 切分
  - `chunk()`
  - `split()`

## 2. 向量运算

### 2.1. 元素运算

- 基本
  - `.add()`、`.sub()`、`.mul()`、`.div()`
  - `.matmul()`：仅作用于最后 2 个维度
  - `.pow()`
  - `exp()`、`sqrt()`、`log()`、`log2()`、`log10()`
  - `floor()`、`ceil()`、`round()`
  - `trunc()`、`frac()`
  - 广播机制
    - 运算右对齐，缺少的维度补 1
- 过滤
  - `index_select()`
  - `masked_select()`
  - `take()`
  - `nonzero()`

### 2.2. 统计运算

- 分布
  - `.std()`、`.var()`、`.median()`、`.mode()`、`.mean()`
  - `.sum()`、`.prod()`
  - `.histc()`
  - `.bincount()`：只对一维计数
- 排序
  - `min()`、`max()`
  - `sort()`
  - `argmin()`、`argmax()`
  - `topk()`
  - `kthvalue()`
  - `where()`
- 范数
  - `dist()`
  - `norm()`
- 频谱
  - `fft()`、`ifft()`
  - `rfft()`、`rifft()`
  - `stft()`

### 2.3. 网络中运算

- 激活函数
  - `abs()`
  - `sign()`
  - `sigmoid()`
- 梯度
  - `.autograd.grad()`
  - `.backward()`
  - `.clamp(min, max)`：防止梯度离散和爆炸

## 3. 模型

### 3.1. 模型管理

- `save()`、`load()`
- `net`
  - `load_state_dict()`
  - `state_dict()`
- `.to(device)`
- `get_num_threads()`、`set_num_threads()`

### 3.2. 初始化

- 随机抽样
  - 定义种子：`manual_seed()`
  - 定义分布

## 4. 模型构建

### 4.1. 模型结构

- `Parameter()`
- Layer
  - `Linear()`
  - `ReLU()`
  - `Sigmoid()`
  - `BatchNorm2d()`
  - `Conv2d()`
  - `ConvTranspose()`
  - `Dropout()`
- Container
  - `net()`
    - `parameters()`
    - `named_parameters()`
    - `train()`
    - `eval()`
  - `Sequential()`
    - `ModuleList()`
    - `ModuleDict()`
- `functional`：函数接口

### 4.2. 损失函数

- `BCELoss()`
- `BCEWithLogitsLoss()`
- `CrossEntropyLoss()`

## 5. 优化

### 5.1. 学习率

- `ExponentialLR`
- `ReduceLROnPlateau`
- `CyclicLR`

### 5.2. 优化器

## 6. TorchVision

### 6.1. 数据增强

- `Compose()`
- Random
  - `RandomResizeCrop()`
  - `RandomRotation()`
  - `RandomGrayscale()`
  - `RandomHorizontalFlip()`
  - `RandomVerticalFlip()`
- `Normalize()`
- `ColorJitter()`
- `ToTensor()`

### 6.2. 数据

- `utils.data`
  - `Dataset`
  - `DataLoader`

### 6.3. 模型

- `models`
