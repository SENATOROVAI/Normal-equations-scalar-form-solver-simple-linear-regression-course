# Troubleshooting Guide

This document helps resolve common issues, errors, and problems encountered when using or developing this project.

---

## 🧪 1. Installation Errors

### ❗ `ModuleNotFoundError` or `ImportError`

**Symptoms:**
```

ModuleNotFoundError: No module named 'Normal equations'

````

**Solution:**
- Make sure dependencies are installed:

```bash
pip install -r requirements.txt
````

* If using a virtual environment, activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

---

## 🛠 2. Running Examples

### ❗ Error when running solver

```
TypeError: grad() missing required positional argument
```

**Solution:**

* Ensure gradient and function signatures match:

```python
def f(x):
    return (x**2).sum()

def grad(x):
    return 2*x
```

---

## 📉 3. Convergence Issues

### ❗ Solver diverges or stagnates

**Possible Causes:**

* Step sizes too large
* Improper line search
* Gradient not computed correctly
* Initial guess far from optimum

**Tips:**

* Try a different starting point
* Use smaller Wolfe line search parameters
* Check gradient implementation with numerical differentiation

---

## 📦 4. Unsupported Python Version

**Warning:**

```
SyntaxError: invalid syntax
```

**Solution:**

* Ensure Python ≥ 3.10 is used
* Check version:

```bash
python --version
```

---

## 🚨 5. Memory or Performance Errors

### ❗ Out of Memory (OOM)

**Cause:**

* Very large dimension (`n`)
* Storing all curvature pairs

**Solution:**

* Reduce memory parameter `m`
* Use sparse or mini-batch implementation

---

## 🧩 6. Jupyter Notebook Issues

### ❗ Notebook not running interactive plots

**Fix:**

* Ensure required extensions are installed:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

---

## 🔍 7. Tests Failing

### ❗ `AssertionError` in tests

**Check:**

* Are you using latest code?
* Did you update algorithm logic without updating test thresholds?

---

## 💡 8. Error Messages & Solutions

Below are common exceptions and how to address them:

| Error                            | Cause                 | Fix                              |
| -------------------------------- | --------------------- | -------------------------------- |
| `ValueError: shapes not aligned` | Wrong array shape     | Ensure correct vector dimensions |
| `TypeError: '<' not supported`   | Invalid comparison    | Cast types properly              |
| `IndexError`                     | Out-of-range          | Check indices and loops          |
| `FloatingPointError`             | Numerical instability | Use smaller step size            |

---

## 🚨 If Issue Persists

If none of the above solves your problem:

1. Search existing Issues in the repository
2. Open a new Issue with:

   * Clear description
   * Minimal reproducible code
   * Screenshots or logs if possible

We will respond as soon as possible.

---

## 📬 Reporting a Bug

Please include:

* Operating System
* Python version
* Exact error traceback
* Input data that caused the error

Example:

```
OS: Ubuntu 22.04
Python: 3.11.2
Error Traceback:
  ...
Function definition:
  ...
```

---

Thank you for using the project! 🚀

