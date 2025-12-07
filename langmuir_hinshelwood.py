#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def langmuir_hinshelwood_model(p_A, p_B, k_1, K_A, K_B):
    return k_1 * K_A * p_A * K_B * p_B / (1 + K_A * p_A + K_B * p_B)**2

def main():
    colormap = matplotlib.colormaps['inferno']  #'viridis', 'plasma', 'inferno', 'coolwarm')
    n_curves = 50
    n_points = 150
    p_A = np.ones(n_points)*10
    K_A = np.ones(n_points)*0.6
    K_As = {}
    rates = []
    rate_strings = []
    for K_A in np.linspace(0.01, 10, n_curves): #loop over equilibrium constant for species A
        p_B = np.linspace(0, 200, n_points) # pressure of B is the x-axis
        plt.plot(p_B, langmuir_hinshelwood_model(p_A, p_B, k_1=0.05, K_A=K_A, K_B=0.6), 
            linewidth=1.75, color = colormap(K_A / n_curves*5))
        rates.append(langmuir_hinshelwood_model(p_A, p_B, k_1=0.05, K_A=K_A, K_B=0.6))
    print(rates[0][0:5:-1])
    print(rate_strings[0:4])

    # format the plot with bold Arial font
    font = {'weight': 'bold', 'fontsize':16}
    plt.xlabel("Pressure of B (kPa)", fontdict=font)
    plt.ylabel("Rate (mol/s)", fontdict=font)
    plt.title("Langmuir-Hinshelwood Model", fontdict=font)
    plt.xticks(fontname=None, fontweight='bold', fontsize=12)
    plt.yticks(fontname=None, fontweight='bold', fontsize=12)
    plt.annotate(
        'Increasing ${K_A}$',
        xy=(0.25, 0.1),
        xytext=(2, 0.1),
        arrowprops=dict(facecolor='black', arrowstyle='<-', linewidth=1.5),
        fontsize=16,
        fontweight='normal'
    )
    plt.text(
        0.75, 0.1,
        r"$\mathrm{Rate} = \dfrac{k_1 K_A p_A K_B p_B}{\left(1 + K_A p_A + K_B p_B\right)^2}$",
        fontsize=13,
        fontweight='bold',
        ha='center',
        va='center',
        transform=plt.gca().transAxes,
        bbox=dict(boxstyle="round,pad=0.1", fc="w", ec="black", lw=0, alpha=0.8)
    )
    plt.tight_layout()
    figure_name = "langmuir-hinshelwood.png"
    plt.savefig(figure_name)
    print("Saved figure to " + figure_name)

if __name__ == "__main__":
    main()