# Markdown - Latex

## 1. Multiple lines

Reduce the use of `begin{array}...end{array}`

- equations in centering: `begin{gathered}...end{gathered}`

$$
\begin{gathered}
  x_1 = \bigg(1 + \dfrac{3}{100} \bigg) ×10, 000 \\
  x_2 = \bigg(1 + \dfrac{3}{100} \bigg) × x_1 = \bigg(1 + \dfrac{3}{100} \bigg)^2×10, 000 \\
  …
\end{gathered}
$$

```latex
$$
\begin{gathered}
  x_1 = \bigg(1 + \dfrac{3}{100} \bigg) ×10, 000 \\
  x_2 = \bigg(1 + \dfrac{3}{100} \bigg) × x_1 = \bigg(1 + \dfrac{3}{100} \bigg)^2×10, 000 \\
  …
\end{gathered}
$$
```

- equations in numbered centering: `begin{gather}...end{gather}`

$$
\begin{gather}
3x_1^2 + 2x_1x_2 + x_2^2 \\
x_1^2 - 2x_2^2
\end{gather}
$$

```latex
$$
\begin{gather}
3x_1^2 + 2x_1x_2 + x_2^2 \\
x_1^2 - 2x_2^2
\end{gather}
$$
```

- equations aligned by symbols: `begin{aligned}...end{aligned}`

$$
\begin{aligned}
y_1 &= x^2 + 2*x \\
y_2 &= x^3 + x
\end{aligned}
$$

```latex
$$
\begin{aligned}
y_1 &= x^2 + 2*x \\
y_2 &= x^3 + x
\end{aligned}
$$
```

- equations with conditions: `begin{cases}...end{cases}`

$$
\begin{cases}
y = x^2 + 2*x & x > 0 \\
y = x^3 + x & x ⩽ 0
\end{cases}
$$

```latex
$$
\begin{cases}
y = x^2 + 2*x & x > 0 \\
y = x^3 + x & x ⩽ 0
\end{cases}
$$
```

- determinant: `begin{vmatrix}...end{vmatrix}`

$$
\begin{vmatrix}
  a + a' & b + b' \\
  c & d
\end{vmatrix} =
\begin{vmatrix}
  a & b \\
  c & d
\end{vmatrix} +
\begin{vmatrix}
  a' & b' \\
  c & d
\end{vmatrix}
$$

```latex
$$
\begin{vmatrix}
  a + a' & b + b' \\
  c & d
\end{vmatrix} =
\begin{vmatrix}
  a & b \\
  c & d
\end{vmatrix} +
\begin{vmatrix}
  a' & b' \\
  c & d
\end{vmatrix}
$$
```

- matrix: `begin{bmatrix}...end{bmatrix}`

$$
\begin{bmatrix}
  a_{11} & a_{12} & ⋯ & a_{1n} \\
  a_{21} & a_{22} & ⋯ & a_{2n} \\
  ⋮ & ⋮ & ⋱ & ⋮ \\
  a_{m1} & a_{m2} & ⋯ & a_{mn}
\end{bmatrix}
$$

```latex
$$
\begin{bmatrix}
  a_{11} & a_{12} & ⋯ & a_{1n} \\
  a_{21} & a_{22} & ⋯ & a_{2n} \\
  ⋮ & ⋮ & ⋱ & ⋮ \\
  a_{m1} & a_{m2} & ⋯ & a_{mn}
\end{bmatrix}
$$
```

## 2. Brackets

- Prefer `\bigg...\bigg` to `\left...\right`

$$
A\bigg[\frac{1}{2}\ \frac{1}{3}\ ⋯\ \frac{1}{99}\bigg]
$$

```latex
$$
A\bigg[\frac{1}{2}\ \frac{1}{3}\ ⋯\ \frac{1}{99}\bigg]
$$
```

- Prefer `\underset{}{}` to `\underset{}`

## 3. Expressions

- Prefer `^{\top}` to `^T` for transpose

$$
A^{⊤}
$$

```latex
$$
A^{\top}
$$
```

- Prefer `\to` to `\rightarrow` for limit

$$
\lim_{n → ∞}
$$

```latex
$$
\lim_{n\to \infty}
$$
```

- Prefer `underset{}{}` to `\limits_`

$$
\underset{w}{\mathrm{argmin}}(wx + b)
$$

```latex
$$
\underset{w}{\mathrm{argmin}}(wx + b)
$$
```

## 4. Fonts

- Prefer `mathrm{}` to `{\rm }` or `\mathop{}` or `\operatorname{}`

$$
θ_\mathrm{MLE} = \underset{θ}{\mathrm{argmax}}∑_{i=1}^{N}\log p(x_i ∣ θ)
$$

```latex
$$
θ_\mathrm{MLE} = \underset{θ}{\mathrm{argmax}}∑_{i=1}^{N}\log p(x_i ∣ θ)
$$
```

- Prefer `\mathbf{}` to `{\bf }`
- Prefer `\mathit{}` to `{\it }`
