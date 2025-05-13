# Modelling Stress and Inflammation Dynamics

**1> LVmodel.py**

Our stress/inflammation dynamics model consists of two differential equations where variables represent pro-inflammatory/pro-stress response (X) and anti-inflammatory/anti-stress metabolites (Y), inspired by the Lotka-Volterra predator-prey model but applied to inflammatory feedback mechanisms:

dX/dt = AX - BXY ------------------------------ (1)

dY/dt = -CY + DXY	----------------------------- (2)

Where:\
A = basal production rate of pro-inflammatory/pro-stress metabolites\
B = inhibitory effect of anti-inflammatory/anti-stress metabolites\
C = basal removal rate of anti-inflammatory/anti-stress metabolites\
D = activation effect of pro-inflammatory/pro-stress metabolites

The time-independent form is:

Aln(Y) - BY + Cln(X) - DX = 0 ----------------- (3)

We derived constants A, B, C, and D using average abundances of metabolites from Table 2 and optimized with Scikit-learn. 


**2> VDPmodel.py**

When constant values failed to converge, indicating non-periodic oscillations, we applied the Van der Pol model:

x" - μ(1-x²)x' + x = 0 ------------------------ (4)

x' = y	--------------------------------------- (5)

Data was normalized between -1 and 1 to optimize μ, which controls damping. 

Phase portraits were plotted for all conditions using the respective ODE systems and derived constants using the Matplotlib package. 


# Microbiome-Metabolite Correlation

**Correlation.py**

The collected metabolite and microbiome data was loaded into pandas DataFrames, and performed A Spearman Rank Correlation analysis using scipy.stats.spearmanr to assess relationships between metabolites and microbiome taxa, with results stored in a correlation matrix. We filtered correlations with absolute values between 0.8 and 1.0 for further analysis.
