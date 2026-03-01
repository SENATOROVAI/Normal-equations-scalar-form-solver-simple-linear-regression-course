# stepik: https://stepik.org/a/239757

# Normal Equations Solver for Simple Linear Regression

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/YOUR_DOI_HERE.svg)](https://doi.org/YOUR_DOI_HERE)

A research-oriented implementation of the **Normal Equations method** for solving the Simple Linear Regression problem in closed form.

---

## Overview

This repository provides a mathematically transparent implementation of the Normal Equations approach:

\[
\hat{\beta} = (X^T X)^{-1} X^T y
\]

for solving the least squares problem:

\[
\min_{\beta} \|X\beta - y\|_2^2
\]

The project is designed for:

- Educational purposes
- Numerical analysis studies
- Research reproducibility
- Linear algebra demonstrations

---

## Mathematical Background

Given:

- Design matrix \( X \in \mathbb{R}^{n \times p} \)
- Target vector \( y \in \mathbb{R}^n \)

The closed-form solution is:

\[
\beta^* = (X^T X)^{-1} X^T y
\]

Provided that \( X^T X \) is invertible.

---

## Features

- Clean NumPy implementation
- Explicit matrix operations
- Reproducible results
- Minimal dependencies
- Research-friendly structure

---

## Installation

```bash
git clone https://github.com/USERNAME/Normal-equations-solver-simple-linear-regression.git
cd Normal-equations-solver-simple-linear-regression
pip install -r requirements.txt
