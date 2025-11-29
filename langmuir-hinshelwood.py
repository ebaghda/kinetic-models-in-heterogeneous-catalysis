#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def langmuir_hinshelwood_model(p_A, p_B, k_1, K_A, K_B):
    return k_1 * K_A *p_A * K_B *p_B / (1 + K_A * p_A + K_B * p_B)**2

def main():
    
    p_A = np.ones(100)*20
    K_As = {}
    rates = []
    rate_strings = []
    for K_A in np.linspace(0.001, 100, 100):
        p_B = np.linspace(0, 10, 100)
        plt.plot(p_B, langmuir_hinshelwood_model(p_A, p_B, 0.01, K_A=K_A, K_B=0.6))
        K_As[K_A] = langmuir_hinshelwood_model(p_A, p_B, 0.01, K_A=K_A, K_B=0.6)
        rates.append(langmuir_hinshelwood_model(p_A, p_B, 0.01, K_A=K_A, K_B=0.6))


    # format the plot
    plt.xlabel("Pressure of B (kPa)")
    plt.ylabel("Rate (mol/s) \n (k_1 = 0.01 mol/s·kPa²) \n (p_A = 20 kPa) \n (K_B = 0.6) \n (K_A = 0.05 - 200)")
    plt.title("Langmuir-Hinshelwood Model")
    # plt.legend(title="K_A", loc="upper left")
    # plt.legend(K_As, title="K_A")
    plt.tight_layout()
    plt.savefig("langmuir-hinshelwood.png")
    print("Saved figure to langmuir-hinshelwood.png")

if __name__ == "__main__":
    main()