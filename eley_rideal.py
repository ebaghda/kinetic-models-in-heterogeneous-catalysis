#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def eley_rideal_model(p_A, p_B, k_1, K_A):
    return k_1 * K_A * p_A * p_B / (1 + K_A * p_A)

def main():
    colormap = matplotlib.colormaps['inferno']  #'viridis', 'plasma', 'inferno', 'coolwarm')
    n_curves = 50
    n_points = 150
    p_B = np.ones(n_points)*10
    K_A = np.ones(n_points)*0.01
    K_As = {}
    rates = []
    rate_strings = []
    for K_A in np.linspace(0.05, 10, n_curves): #loop over equilibrium constant for species A
        p_A = np.linspace(0, 5, n_points) # pressure of A is the x-axis
        plt.plot(p_A, eley_rideal_model(p_A, p_B, k_1=0.05, K_A=K_A), 
            linewidth=1.75, color = colormap(K_A / n_curves*5))
        rates.append(eley_rideal_model(p_A, p_B, k_1=0.05, K_A=K_A))
    print(rates[0][0:5:-1])
    print(rate_strings[0:4])

    # format the plot with bold Arial font
    font = {'weight': 'bold', 'fontsize':16}
    plt.xlabel("Pressure of A (kPa)", fontdict=font)
    plt.ylabel("Rate (mol/s)", fontdict=font)
    plt.title("Eley-Rideal Model", fontdict=font)
    plt.xticks(fontname=None, fontweight='bold', fontsize=12)
    plt.yticks(fontname=None, fontweight='bold', fontsize=12)
    # annotate the plots
    plt.annotate(
        'Increasing ${K_A}$',
        xy=(0.25, eley_rideal_model(2.5, 10, k_1=0.05, K_A=8)), # point to annotate (mid x, example K_A)
        xytext=(2, eley_rideal_model(2.5, 10, k_1=0.05, K_A=0.1) + 0.01),   # text location above the point
        arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
        fontsize=16,
        fontweight='normal'
    )
    plt.tight_layout()
    plt.savefig("eley_rideal.png")
    print("Saved figure to eley_rideal.png")

if __name__ == "__main__":
    main()