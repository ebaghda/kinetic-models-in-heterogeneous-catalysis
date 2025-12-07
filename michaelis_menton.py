#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def michaelis_menton_model(C_A, V_max, K_M):
    return V_max * C_A / (K_M + C_A)

def main():
    colormap = matplotlib.colormaps['inferno']  #'viridis', 'plasma', 'inferno', 'coolwarm')
    n_curves = 50
    n_points = 150
    V_max = np.ones(n_points)*10 # maximum reaction rate
    for K_M in np.linspace(0.05, 8, n_curves): #loop over equilibrium constant for species A
        C_A = np.linspace(0, 5, n_points) # concentration of A is the x-axis
        plt.plot(C_A, michaelis_menton_model(C_A, V_max, K_M=K_M), 
            linewidth=1.75, color = colormap(K_M / n_curves*5))

    # format the plot with bold Arial font
    font = {'weight': 'bold', 'fontsize':16}
    plt.xlabel("Concentration of Species A (M)", fontdict=font)
    plt.ylabel("Rate (mol/s)", fontdict=font)
    plt.title("Michaelis-Menton Model", fontdict=font)
    plt.xticks(fontname=None, fontweight='bold', fontsize=12)
    plt.yticks(fontname=None, fontweight='bold', fontsize=12)
    # annotate the plots
    plt.gca().axhline(y=10, color='k', linestyle='--', linewidth=1, label='Target Line', xmax=3)
    plt.annotate(
        'Increasing ${K_M}$',
        xy=(0.25, michaelis_menton_model(2.5, 10, K_M=0.1)),
        xytext=(2, michaelis_menton_model(2.5, 10, K_M=100)),
        arrowprops=dict(facecolor='black', arrowstyle='<-', linewidth=1.5),
        fontsize=16,
        fontweight='normal'
    )
    plt.text(
        0.85, 0.1,
        r"$\mathrm{Rate} = \dfrac{V_{max} [A]}{K_M + [A]}$",
        fontsize=13,
        fontweight='bold',
        ha='center',
        va='center',
        transform=plt.gca().transAxes,
        bbox=dict(boxstyle="round,pad=0.4", fc="w", ec="black", lw=0, alpha=0)
    )
    plt.tight_layout()
    figure_name = "michaelis_menton.png"
    plt.savefig(figure_name)
    print("Saved figure to " + figure_name)

if __name__ == "__main__":
    main()