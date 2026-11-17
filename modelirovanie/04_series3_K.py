import numpy as np
import matplotlib.pyplot as plt


def logistic_model(a, K, N0, T):
    """Дискретная логистическая модель из задания."""
    N = np.zeros(T + 1, dtype=float)
    N[0] = N0

    for t in range(T):
        N[t + 1] = N[t] + a * N[t] * (1.0 - N[t] / K)

    return N
# Серия 3 по методичке: меняется только K.
# a = 0.6, N0 = 5000.
K_values = [60_000, 150_000]
a = 0.6
N0 = 5_000.0
T = 24

plt.figure(figsize=(10, 6))

for K in K_values:
    N = logistic_model(a, K, N0, T)
    t = np.arange(T + 1)
    plt.plot(t, N, linewidth=1.5, label=f"K = {K:,.0f}".replace(",", " "))

plt.axhline(N0, linestyle=":", linewidth=1.0, label="N₀ = 5 000")
plt.xlabel("Месяц t")
plt.ylabel("Число пользователей N(t)")
plt.title("Серия 3 — влияние ёмкости рынка K")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("series3_K.png", dpi=200, bbox_inches="tight")
plt.show()
