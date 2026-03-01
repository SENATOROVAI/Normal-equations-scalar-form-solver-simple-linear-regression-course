# stepik: https://stepik.org/a/239757

# Normal Equations Solver for Simple Linear Regression

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

Research-oriented implementation of the **Normal Equations method** for solving **Simple Linear Regression** in closed form.

---

## Overview

This repository provides a mathematically transparent implementation of the closed-form solution to the ordinary least squares (OLS) problem for simple linear regression.

We consider the model:

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i
$$

where:

- $x_i$ — scalar input  
- $y_i$ — scalar target  
- $\beta_0$ — intercept  
- $\beta_1$ — slope  
- $\varepsilon_i$ — noise term  

---

## Least Squares Formulation

The objective is to minimize the residual sum of squares:

$$
\min_{\beta_0, \beta_1}
\sum_{i=1}^{n}
\left(
y_i - (\beta_0 + \beta_1 x_i)
\right)^2
$$

---

## Matrix Form

Define the design matrix:

$$
X =
\begin{bmatrix}
1 & x_1 \\
1 & x_2 \\
\vdots & \vdots \\
1 & x_n
\end{bmatrix}
$$

Parameter vector:

$$
\beta =
\begin{bmatrix}
\beta_0 \\
\beta_1
\end{bmatrix}
$$

Target vector:

$$
y =
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix}
$$

Then the least squares problem becomes:

$$
\min_{\beta} \|X\beta - y\|_2^2
$$

---

## Closed-Form Solution (Scalar Version)

For simple linear regression, the coefficients can also be written explicitly:

$$
\beta_1 =
\frac
{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}
{\sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

$$
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$

where:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

$$
\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i
$$

---

## Numerical Considerations

The matrix $X^T X$ must be non-singular.  
If multicollinearity or degeneracy occurs, numerical instability may arise.

For improved stability in high-dimensional settings, QR decomposition or SVD-based solvers are preferred.

---

## Implementation

The solver is implemented using NumPy and performs:

1. Construction of $X$
2. Computation of $X^T X$
3. Matrix inversion
4. Coefficient estimation

---

## Example Usage

```python
from solver import normal_equation

beta_0, beta_1 = normal_equation(x, y)
