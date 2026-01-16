# 📉 An Order Six Numerical Method for Direct Solution of General Second Order ODEs
**Industrial Mathematics Thesis | Federal University of Technology, Akure (FUTA)**

## 📌 Project Overview
This repository contains the full mathematical derivation and computational implementation of a **Sixth-Order Numerical Method** designed for the direct solution of general second-order Initial Value Problems (IVPs):
$$y'' = f(x, y, y'), \quad y(x_0) = y_0, \quad y'(x_0) = y'_0$$

Developed as a final year project in the Department of Mathematical Sciences, FUTA, this method utilizes a **Power Series (Taylor Series)** basis function to maintain the original second-order structure, avoiding the computational doubling required by reduction to first-order systems.

---

## 🛠️ Technical Stack
* **Computational Engine:** Maple (Matrix inversion, Taylor expansions, Numerical Experiments)
* **Typesetting:** LaTeX (High-precision mathematical documentation)
* **Mathematical Theory:** Collocation & Interpolation, Linear Multistep Methods (LMM).

---

## 🧮 Mathematical Methodology

### 1. The Basis Function
We assume an approximate solution of the form:
$$y(x) = \sum_{j=0}^{7} a_j x^j$$
By collocating at $p=5$ points and interpolating at $q=3$ points, we construct the following matrix system $AX = B$:

$$
\begin{bmatrix}
1 & x_n & x_n^2 & x_n^3 & x_n^4 & x_n^5 & x_n^6 & x_n^7 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
0 & 0 & 2 & 6x_{n+4} & 12x_{n+4}^2 & 20x_{n+4}^3 & 30x_{n+4}^4 & 42x_{n+4}^5
\end{bmatrix}
\begin{bmatrix} a_0 \\ \vdots \\ a_7 \end{bmatrix} = \begin{bmatrix} y_n \\ \vdots \\ f_{n+4} \end{bmatrix}
$$

### 2. The Derived Discrete Scheme
Evaluating the continuous form at $t=4$ yields the main discrete scheme:
$$y_{n+4} - 2y_{n+2} + y_n = \frac{h^2}{15} (f_{n} + 16f_{n+1} + 26f_{n+2} + 16f_{n+3} + f_{n+4})$$

And the derivative $(\text{y}')$ provider:
$$y'_{n+4} = - \frac{149}{42}y_{n+2} + \frac{128}{21}y_{n+1} - \frac{107}{42}y_{n} + \frac{h^{2}}{1260} \left( 325f_{n} + 4048f_{n+1} + 1106f_{n+2} + 1744f_{n+3} + 397f_{n+4} \right)$$

---

## 📊 Analysis of Basic Properties
* **Order ($p$):** 6
* **Error Constant ($C_8$):** $-\frac{2}{945} \approx -0.002116$
* **Consistency:** The method is proven consistent as $p \geq 1$ and it satisfies $\rho(1)=\rho'(1)=0$ and $\rho''(1) = 2\sigma(1)$.
* **Zero-Stability:** The first characteristic polynomial $\rho(z) = z^4 - 2z^2 + 1$ has roots $z=1$ (double) and $z=-1$ (double), satisfying the root condition for second-order ODEs.
* **Stability Interval:** Determined via boundary locus method to be $(0, -0.2742)$.

---

## 🧪 Numerical Results & Benchmarks
The method was implemented in Maple to solve four specific benchmark problems:

| Problem Type | ODE | Exact Solution | Abs Error ($x=1.0$) | Benchmark Source |
| :--- | :--- | :--- | :--- | :--- |
| **Linear** | $y''=y$ | $y=e^x$ | **2.5827e-10** | Olayemi (2015) |
| **Non-Linear** | $y''=x(y')^2$ | $y=1 + \frac{1}{2}\log\left(\frac{2+x}{2-x}\right)$ | **4.4697e-02** | Omole (2023) |
| **Stiff** | $y''=y'$ | $y=1-e^x$ | **4.0000e-10** | Kuboye (2021) |
| **Oscillatory**| $y''+y=2\cos x$ | $y=\cos x + x\sin x$ | **3.6358e-04** | Adesanya (2011) |

---

## 📁 Repository Structure
* `/Documentation`: Contains the LaTeX source code and the final Thesis PDF.
* `/Images`: Plots and graphs generated from numerical experiments.
* `/MapleCodes`: `.txt` and `.mw` files for direct implementation of the solver.

```text
├── Documentation/
│   └── MTS192584_OGUNDARE_THESIS.pdf   # Full Thesis Document (LaTeX)
├── Scripts/
│   └── Maple_Calculations.mw           # Maple Worksheet for Derivations
└── README.md
```
---

## 🎓 Author
**Ogundare, Olamide Emmanuel** *B.Tech Industrial Mathematics, FUTA (2025)* Supervisor: **Dr. F.O. Obarhua**

**LinkedIn:** [emycodes](https://linkedin.com/in/emycodes)