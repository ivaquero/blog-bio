# Python

## 1. Basics

### 1.1. Iteration

- `enumerate()` is prefered to `range(len())`

```python
xs = range(3)

# good
for ind, x in enumerate(xs):
  print(f'{ind}: {x}')

# bad
for i in range(len(xs)):
  print(f'{i}: {xs[i]}')
```

## 2. Matplotlib

### 2.1. Subplots

- `Axes` object is prefered to `Figure` object
- use `constrained_layout=True` when draw subplots

```python
# good
_, axes = plt.subplots(1, 2, constrained_layout=True)
axes[0].plot(x1, y1)
axes[1].hist(x2, y2)

# bad
plt.subplot(121)
plt.plot(x1, y1)
plt.subplot(122)
plt.hist(x2, y2)
```

- `axes.flatten()` is prefered to `plt.subplot()` in cases where subplots' data is iterable
- `zip()` or `enumerate()` is prefered to `range()` for iterable objects

```python
# good
_, ax = plt.subplots(2, 2, figsize=[12,8], constrained_layout=True)

for ax, x, y in zip(axes.flatten(), xs, ys):
  ax.plot(x, y)

# bad
for i in range(4):
  ax = plt.subplot(2, 2, i+1)
  ax.plot(x[i], y[i])
```

### 2.2. Decoration

- `set()` method is prefered to `set_*()` method

```python

# good
ax.set(xlabel='x', ylabel='y')

# bad
ax.set_xlabel('x')
ax.set_ylabel('y')
```

- `ax.spines[*].set_visible()` with list is prefered to line-by-line `ax.spines[*].set_visible()`

```python
# good
ax.spines["top", "bottom"].set_visible(False)

# bad
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
```
