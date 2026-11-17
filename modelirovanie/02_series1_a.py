import numpy as np
import matplotlib.pyplot as plt


def logistic_model(a, K, N0, T):
    """Дискретная логистическая модель из задания."""
    N = np.zeros(T + 1, dtype=float)
    N[0] = N0

    for t in range(T):
        N[t + 1] = N[t] + a * N[t] * (1.0 - N[t] / K)

    return N
# Серия 1 по методичке: меняется только a.
# K = 100000, N0 = 5000.
a_values = [0.3, 0.6, 1.2, 1.9, 2.2, 2.55, 2.9]
K = 100_000.0
N0 = 5_000.0
T = 40

plt.figure(figsize=(10, 6))

for a in a_values:
    N = logistic_model(a, K, N0, T)
    t = np.arange(T + 1)
    plt.plot(t, N, linewidth=1.5, label=f"a = {a}")

plt.axhline(K, linestyle="--", linewidth=1.2, label="K = 100 000")
plt.xlabel("Месяц t")
plt.ylabel("Число пользователей N(t)")
plt.title("Серия 1 — влияние коэффициента прироста a")
plt.grid(alpha=0.3)
plt.legend(ncol=2)
plt.tight_layout()

plt.savefig("series1_a.png", dpi=200, bbox_inches="tight")
plt.show()
