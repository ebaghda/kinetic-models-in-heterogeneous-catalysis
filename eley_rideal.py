#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def eley_rideal_model(p_A, p_B, k_1, K_A):
    return k_1 * K_A * p_A * p_B / (1 + K_A * p_A)

def main():
    colormap = matplotlib.colormaps['inferno']  #'viridis', 'plasma', 'inferno', 'coolwarm')
    n_curves = 100
    n_points = 150
    p_B = np.ones(n_points)*10
    K_As = {}
    rates = []
    rate_strings = []
    for K_A in np.linspace(0.0001, 1, n_curves): #loop over equilibrium constant for species A
        p_A = np.linspace(0, 10, n_points) # pressure of A is the x-axis
        plt.plot(p_A, eley_rideal_model(p_A, p_B, k_1=0.05, K_A=K_A), 
            linewidth=1.75, color = colormap(K_A / n_curves*95))
        rates.append(eley_rideal_model(p_A, p_B, k_1=0.05, K_A=K_A))

    # format the plot with bold Arial font
    font = {'weight': 'bold', 'fontsize':16}
    plt.xlabel("Pressure of Species A (kPa)", fontdict=font)
    plt.ylabel("Rate (mol/s)", fontdict=font)
    plt.title("Eley-Rideal Model", fontdict=font)
    plt.xticks(fontname=None, fontweight='bold', fontsize=12)
    plt.yticks(fontname=None, fontweight='bold', fontsize=12)
    # annotate the plots
    plt.annotate(
        'Increasing ${lambda_A}$',
        xy=(0.25, 0.4), xytext=(6, 0.1),
        arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=2.0),
        fontsize=16,
        fontweight='normal'
    )
    # Annotate the plot with the Eley-Rideal model equation
    plt.text(
        0.16, 0.92,
        r"$\mathrm{Rate} = \dfrac{k_1 K_A p_A p_B}{1 + K_A p_A}$",
        fontsize=12,
        fontweight='bold',
        ha='center',
        va='center',
        transform=plt.gca().transAxes,
        bbox=dict(boxstyle="round,pad=0.4", fc="w", ec="black", lw=0, alpha=0)
    )
    plt.tight_layout()
    figure_name = "eley_rideal.png"
    plt.savefig(figure_name)
    print("Saved figure to " + figure_name)


if __name__ == "__main__":
    main()