import numpy as np
import matplotlib.pyplot as plt


def logistic_model(a, K, N0, T):
    """Дискретная логистическая модель из задания."""
    N = np.zeros(T + 1, dtype=float)
    N[0] = N0

    for t in range(T):
        N[t + 1] = N[t] + a * N[t] * (1.0 - N[t] / K)

    return N
# Серия 2 по методичке: меняется только N0.
# a = 0.6, K = 100000.
N0_values = [500, 20_000, 90_000, 105_000]
a = 0.6
K = 100_000.0
T = 24

plt.figure(figsize=(10, 6))

for N0 in N0_values:
    N = logistic_model(a, K, N0, T)
    t = np.arange(T + 1)
    plt.plot(t, N, linewidth=1.5, label=f"N₀ = {N0:,.0f}".replace(",", " "))

plt.axhline(K, linestyle="--", linewidth=1.2, label="K = 100 000")
plt.xlabel("Месяц t")
plt.ylabel("Число пользователей N(t)")
plt.title("Серия 2 — влияние начального состояния N₀")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("series2_N0.png", dpi=200, bbox_inches="tight")
plt.show()
