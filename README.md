# Modelling Stress and Inflammation Dynamics

This repository contains the mathematical models, simulations, and correlation analyses used to investigate the dynamic interplay between stress-related and inflammation-related metabolites, along with microbiome-metabolite associations.

## 📁 Contents

- **LVmodel.py** – Implements a Lotka-Volterra-inspired model of stress and inflammation dynamics.
- **VDPmodel.py** – Implements the Van der Pol oscillator model for non-convergent, non-linear dynamics.
- **Correlation.py** – Performs Spearman Rank Correlation analysis between microbiome taxa and metabolite abundances.
  
---

## 📈 1. Lotka-Volterra Model (`LVmodel.py`)

This model consists of two coupled differential equations:

dX/dt = A·X - B·X·Y      \
dY/dt = -C·Y + D·X·Y    

Where:
- `X`: Pro-inflammatory or pro-stress component
- `Y`: Anti-inflammatory or anti-stress component
- `A`: Basal production rate of `X`
- `B`: Inhibitory effect of `Y` on `X`
- `C`: Basal removal rate of `Y`
- `D`: Activation effect of `X` on `Y`

We also solved for the steady-state using the time-independent formulation:

Aln(Y) - BY + Cln(X) - DX = 0

Model constants were derived using average metabolite abundances and optimized using `scikit-learn`.

---

## 🔁 2. Van der Pol Oscillator (`VDPmodel.py`)

In cases where Lotka-Volterra dynamics failed to converge (i.e., non-periodic or damped oscillations), we applied the Van der Pol oscillator:

x'' - μ·(1 - x²)·x' + x = 0     

Where `μ` controls the damping behavior. Variables were normalized between -1 and 1. First-order ODEs were used:

x' = y

Phase portraits were plotted using `matplotlib`.

---

## 🧬 3. Microbiome-Metabolite Correlation (`Correlation.py`)

- Input: DataFrames containing metabolite levels and microbial abundances.
- Method: Spearman Rank Correlation (`scipy.stats.spearmanr`)
- Output: Correlation matrix
- Filter: Correlations with |r| ≥ 0.8 were retained for interpretation.

---

## 🔧 Requirements

Install dependencies using pip:

```bash
pip install numpy pandas matplotlib scikit-learn
