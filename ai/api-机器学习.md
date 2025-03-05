# 机器学习 API

## 1. 基础统计

### 1.1. 统计量

- NumPy
  - `np.ptp()`：极差
  - `np.mean()`
  - `np.median()`
  - `np.var()`
  - `np.std()`
- SciPy
  - `stats.mode()`
  - `stats.sem()`：标准误，即样本均值抽样分布的标准差
  - `stats.zscore()`

### 1.2. 正态性检验

- `stats.normaltest()`
- `stats.shapiro()`
- `stats.kstest()`
- `stats.ks_1samp()`
- `stats.ks_2samp()`
- `stats.anderson()`

### 1.3. 显著性检验

- 参数检验
  - 独立样本
    - `stats.ttest_1samp()`
    - `stats.ttest_ind()`
    - `stats.f_oneway()`
  - 配对样本
    - `stats.ttest_rel()`
- 非参数检验
  - 分类样本
    - 独立样本
      - `stats.fisher_exact()`
  - 顺序样本
    - 独立样本
      - `stats.mannwhitneyu()`
      - `stats.kruskal()`
    - 配对样本
      - `stats.wilcoxon()`
      - `stats.friedmanchisquare()`

### 1.4. 相关性检验

- `stats.f()`
- `stats.chi2_contingency()`
- `stats.bartlett()`
- `stats.levene()`
- `stats.fligner()`

### 1.5. 拟合度检验

- `stats.jarque_bera()`
- `stats.ksone()`
- `stats.kstwo()`
- `stats.kstwobign()`

## 2. NumPy

### 2.1. 生成，类型

- `numpy.random`
  - `rand()`：均匀分布
  - `randn()`：标准
  - `randint()`：随机生成整数
  - `normal()`
  - `binomial()`
  - `seed()`
  - `permutation()`, `shuffle()`
- generation
  - `zeros()`, `zeros_like()`
  - `ones()`, `ones_like()`
  - `full()`, `full_like()`
  - `empty()`, `empty_like()`
  - `eye()`
  - `identity()`
  - `meshgrid()`
  - repetition
    - `repeat()`
    - `tile()`
- types
  - `array()`
  - `asarray()`
  - `asmatrix()`
  - `asscalar()`

### 2.2. 查询，索引

- indexes
  - `take()`, `put()`
- inquiry
  - `where(cond, xarr, yarr)`：x if condition else y
  - `searchsorted()`
  - `isnan()`
  - `isfinite()`, `isinf()`

### 2.3. 排序，变换

- rank
  - `sort()`
  - `argsort()`
  - `lexsort()`
- self.method
  - `dtype`
  - `shape`
  - `ndim`
  - `T`
  - `astype()`
  - `reshape()`
  - `transpose()`
  - `swapaxes()`
- reshaping
  - `concatenate()`
  - `hstack()`, `vstack()`, `dstack()`
  - `row_stack()`, `column_stack()`
  - `split()`
  - `hsplit()`, `vsplit()`, `dsplit()`
  - `r*()`, `c*()`

### 2.4. 计算

- `numpy.linalg`
  - `inv()`, `pinv()`
  - `qr()`, `svd()`
  - `eig()`, `eigvals()`
  - `trace()`, `det()`
  - `solve()`, `lstsq()`
- computation
  - `dot()`：内积，矩阵乘法
  - `power()`
  - `add()`, `substract()`, `multiply()`, `divide()`, `mod()`
  - `abs()`, `fabs()`
  - `sqrt()`, `square()`
  - `exp()`, `log()`, `log2()`, `log10()`, `log1p()`
  - `ceil()`, `floor()`
  - `sign()`
  - `maximum()`, `fmax()`, `minimum()`, `fmin()`
- set operation
  - `unique()`
  - `interset1d()`, `union1d()`
  - `in1d()`
  - `setdiff1d()`, `setxor()`

## 3. Pandas

### 3.1. 生成，显示

- Series
  - `Series()`
  - `values`
  - `index`, `index.name`
  - `name`
- DataFrame
  - `DataFrame()`
  - `values`
  - `index`, `index.name`
  - `columns`, `columns.name`
  - `T`
  - `head()`, `tail()`
  - `to_markdown()`

### 3.2. 查询，索引

- Index
  - `Index()`
  - `append()`, `drop()`
  - `insert()`, `delete()`
  - `unique()`
  - `intersection()`, `union()`
  - `difference()`
  - `reindex()`
  - `reset_index()`
- selection, column
  - `df[cond]`
  - `df[[*col_name]]`
  - `df.loc[col_name]` , `df.loc[:, col_name]`
  - `df.iloc[ind]`, `df.iloc[:, ind]`
- inquiry
  - `isin()`, `notin()`

### 3.3. 归纳，清洗

- summary
  - `describe()`
  - `unique()`
  - `value_counts()`
  - `df.corr(method='spearman')`
- problem values
  - `dropna()`
  - `fillna()`
  - `isna()`, `notna()`
  - `duplicate()`
  - `drop_duplicates()`
  - `interpolate()`
- numerical modification
  - `df.apply(func)`
  - `series.replace()`
  - `series.map(func)`
  - `drop()`
- columns
  - `rename()`
- strings
  - `series.str.func()`

### 3.4. 排序，重塑

- rank
  - `sort_index()`
  - `sort_values()`
- df operation
  - `df.add()`, `df.sub()`, `df.mul()`, `df.div()`
  - `df.floordiv()`, `df.pow()`
- hierarchical indexing
  - `stack()`, `unstack()`
  - `swaplevel()`
- connection
  - `concat()`：stack dataframes
  - `append()`: stack dataframes vertically
  - `join()`：merge by the index
  - `merge()`：SQL JOIN on the selected column(s)
- reshaping
  - `pivot_table()`: long -> wide
  - `melt()`: wide -> long
  - `explode()`
- grouping
  - `groupby()`
    - `agg()`
  - `cut()`, `qcut()`
  - `crosstab()`

### 3.5. 分类数据

- categorical data
  - `Categorical()`
  - `get_dummies()`

## 4. 数据探索

### 4.1. 缺失值

- 丢弃
  - `df.dropna(axis =1)`
  - `df.dropna(subset=['Cabin', 'Age'])`
- 统计
  - `df.isnull().mean() * 100`
  - `df.isna().any().any()`
- 填充
  - `df.fillna(data.median())`
  - `df.fill_empty(columns =["A", "B"], value=10)`
  - `SimpleImputer(strategy='mean').fit_transform()`

### 4.2. 分箱

```python
# Numerical Binning
data['bin'] = pd.cut(data['value'], bins=[0,30,70,100], labels=["Low", "Mid", "High"])

# Categorical Binning
conditions = [
  data['Country'].str.contains('Spain'),
  data['Country'].str.contains('Italy'),
  data['Country'].str.contains('Chile')]

choices = ['Europe', 'Europe', 'South America']

data['Continent'] = np.select(conditions, choices, default='Other')
```

## 5. 数值数据

### 5.1. 放缩

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler, Normalizer

scaler = StandardScaler()
# scaler = MinMaxScaler()
# scaler = MaxAbsScaler()
# scaler = RobustScaler()
# scaler = Normalizer()

scaler.fit_transform(data)

# 对数变换，保证正数
data['log'] = (data['value']-data['value'].min()+1).transform(np.log)
```

### 5.2. 离群值

- `pd.mean()+/-3*pd.std()`

```python
# 基于标准差
upper_lim = df['column'].mean () + df['column'].std () * 3
lower_lim = df['column'].mean () - df['column'].std () * 3
df = df[lower_lim < df['column'] < upper_lim]

# 基于四分位数
upper_lim = df['column'].percentile(.75) * 1.5
lower_lim = df['column'].quantile(.25) * 1.5
df = df[lower_lim < df['column'] < upper_lim]

# 处理离群值的一种方法是将其设置为上限。这样做可以保留数据规模，并且对于最终模型性能来说可能会更好。但也可能会影响数据的分布。
df.loc[(df[column] > upper_lim), column] = upper_lim
df.loc[(df[column] < lower_lim), column] = lower_lim
```

## 6. 类别数据

### 6.1. 基本操作

- 转化
  - `df.astype({"Name": "category"})`
- 替换
  - `df_cat["Name"].cat.rename_categories(str.upper)`
- 合并
  - `df1_cat.astype({"Name": df2_cat["Name"].dtype}).merge(df2_cat, on="Name")`

### 6.2. 字符串

- 提取
  - `df['Name'].str.extract(pattern, expand=False).value_counts()`
- 拆分
  - `df['Name'].str.split(" ").map(lambda x: x[0])`

### 6.3. 哑变量

对于类别数不多的数据，通常使用哑变量。

```python
import pandas as pd

X_cat = pd.DataFrame({
    "A": [1, None, 3],
    "names": ["Fred,George", "George", "John,Paul"]
})
pd.get_dummies(X_cat, drop_first=True)
```

### 6.4. 标签编码

```python
(X_cat['names'].astype("category").cat.as_ordered().cat.codes + 1)

lab = LabelEncoder()
lab.fit_transform(X_cat.names)
# 解码
lab.inverse_transform([0, 1, 2])

# 将标签编码为对应的频率
X_cat['names'].map(X_cat['names'].value_counts())
```

### 6.5. 其他编码

```python
import category_encoders as ce

size_df = pd.DataFrame({
    "name": ["Fred", "John", "Matt"],
    "size": ["small", "med", "xxl"],
})

ore = ce.OrdinalEncoder(mapping=[{
    "col": "size",
    "mapping": {
        "small": 1,
        "med": 2,
        "lg": 3,
    }
}])

ore.fit_transform(size_df).head()

titles = df['Name'].str.extract("([A-Za-z]+)\.", expand=False)
df1 = df.add_column(column_name='Title', value=titles)

te = ce.TargetEncoder(cols="Title")  # 先验
te.fit_transform(df1, df['Survived'])["Title"].head()
```

## 7. 采样

### 7.1. 上采样

```python
# 方法 1
from sklearn.utils import resample

mask = df.Survived == 1
surv_df, death_df = df[mask], df[~mask]

df_upsample = resample(surv_df,
                       replace=True,
                       n_samples=len(death_df),
                       random_state=42)
df2 = pd.concat([death_df, df_upsample])
df2.Survived.value_counts()

# 方法 2
from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=42)
X_ros, y_ros = ros.fit_sample(X, y)
pd.Series(y_ros).value_counts()
```

### 7.2. 下采样

```python
from sklearn.utils import resample

mask = df.Survived == 1
surv_df, death_df = df[mask], df[~mask]

df_upsample = resample(death_df,
                       replace=True,
                       n_samples=len(surv_df),
                       random_state=42)

df3 = pd.concat([surv_df, df_downsample])
df3.Survived.value_counts()
```

## 8. 特征选择

### 8.1. 分布对称性

```python
from scipy.stats import norm

# 定量
(μ, σ) = norm.fit(data)

# 定类
## skew 以 [0, 0.5, 1.0, inf] 为节点
pd.Series(data).skew()
## kurtosis 以 [-inf, -1, -0.5, 0, 0.5, 1.0, inf] 为节点
pd.Series(data).kurt()
```

### 8.2. 互信息

```python
from sklearn.feature_selection import mutual_info_classif

mic = mutual_info_classif(X, y)

_, ax = plt.subplots()

(pd.DataFrame({
    "feature": X.columns,
    "vimp": mic
}).set_index("feature").plot.barh(ax=ax))
```

## 9. 降维

### 9.1. 基于特征选择

```python
from sklearn.feature_selection import VarianceThreshold, SelectKBest, mutual_info_classif, mutual_info_regression, SelectFromModel, RFE

# 方差过滤
VarianceThreshold(threshold=0.0).fit_transform(X, y)

# 卡方过滤（原假设：相互独立）
SelectKBest(chi2, k).fit_transform(X, y)
# F 检验（不存在显著的线性关系）
SelectKBest(f_classif, k).fit_transform(X, y)
# 互信息
SelectKBest(mutual_info_classif, k).fit_transform(X, y)
SelectKBest(mutual_info_regression, k).fit_transform(X, y)

# 嵌入法：精确度模型本身，是过滤法的进阶版。
SelectFromModel(model, threshold=0.01).fit_transform(X, y)
# 包装法
RFE(sklearn.SVM.SVC(), k).fit_transform(X, y)
```

### 9.2. 基于特征转换

```python
from sklearn.decomposition import PCA

# PCA
pca = PCA().fit()
pca.components_  # 返回模型各个特征向量
pca.explained_variance_ratio_  # 返回各自成分的方差百分比
```

### 9.3. 基于特征组合

```python
from sklearn import ensemble
from sklearn import preprocessing

# GBDT
GradientBoostingClassifier().fit(X, y).apply(X)[:, :, 0]
# [n_samples,n_estimators, n_classes]

# 多项式
PolynomialFeatures.fit_transform(X, y).get_feature_names()
```
