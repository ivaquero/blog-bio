# 社会学建模

## 1. 博弈论模型

### 1.1. 假设

假设有 2 种策略，扮演”好人“和“骗子”，分别表示为$A$和$B$；用字母$A$和$B$作为状态变量，代表当前采用策略的个体。策略的采用由基因型决定。令$r_A$和$r_B$分别表示携带两种基因型的个体的繁殖率，可得采用策略$A$的个体的变化率$A'$和采用策略$B$的个体的变化率$B'$

$$
\begin{gather}
\begin{aligned}
    A' = r_A⋅A \\
    B' = r_B⋅B
\end{aligned}
\end{gather}
$$

其中，$r_A$和$r_B$是变量，与各自策略的成功率成正比。

### 1.2. 复制子方程

用$X$表示采用策略$A$的个体占比（即基因型的主导率，Prevalence），有

$$
\begin{gather}
\begin{aligned}
    X&= \frac{A}{A+B} \\
    Y&= \frac{B}{A+B} = 1- X
\end{aligned}
\end{gather}
$$

求导得

$$
\begin{gather}
\begin{aligned}
    \big(\frac{A}{A + B}\big)' &= \frac{(A + B) A' - A(A + B)'}{(A + B)^2} \\
    &= \frac{AA' + B A' - AA' - AB'}{(A + B)^2}
\end{aligned}
\end{gather}
$$

将式（1）代入（3），有

$$
\begin{gather}
X' = \frac{r_A AB - r_B BA}{(A + B)^2}
\end{gather}
$$

又由式（2），得

$$
X' = (r_A - r_B) X(1 - X)
$$

### 1.3. 收益

- 竞争要付出很大的代价。假设竞争失败的代价为 3，则它的收益是 -3，而获得的资源价值是 +2。

- 所有的骗子都有同样的竞争力，故骗子种内竞争获胜的概率是 50%。因此，当一个骗子遇到另一个骗子时，它的预期回报是 50% 的机会，即 +2，50% 的机会是 -3，故总的期望值是 0.5×(+2) + 0.5×(-3) = -0.5。
- 好人几乎不存在种内竞争。当一个好人遇到另一个好人时，既不需要付出代价也不会得到收益。
- 当一个好人遇到一个骗子时，骗子和好人平分资源。因此，骗子的收益是 +1，而好人的收益是 -1。

|   收益    | 好人（A） |  骗子（B）   |
| :-------: | :-------: | :----------: |
| 好人（A） |  (0, 0)   |   (-1, +1)   |
| 骗子（B） | (+1, -1)  | (-0.5, -0.5) |

将每个基因型的人均增长率定义为其与相同基因型和其他基因型成员相互作用的结果之和。例如，对$A$，有

$$
\begin{gather}
r_A = 0 * X + (-1) * (1 - X) = X - 1
\end{gather}
$$

类似地，则有

$$
\begin{gather}
r_B = 1 * X + (-0.5) * (1 - X) = 1.5X - 0.5
\end{gather}
$$

将式（6）和（7）代入，复制子方程（5），则有

$$
\begin{aligned}
    X' = \dfrac{dX}{dt}
    &= (r_A - r_B)X(1 - X) \\
    &= [(X - 1)-(1.5X - 0.5)]X(1 - X) \\
    &= 0.5*(X + 1)X(X - 1)
\end{aligned}
$$

### 1.4. 稳定性分析

## 2. 演化

$$
Δ = B + (R̄ - D) × N
$$

- $Δ:$ expected change
- $B:$ spontaneous birth rate
- $R̄$: adjusted replication chance per creature
- $D:$ death chance per creature
- $N:$ current creature total

$$
R̄ = R × (1 - M)
$$

- $M$: mutation chance
- $R$: replication chance per creature
