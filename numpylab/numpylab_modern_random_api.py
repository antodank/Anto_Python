import numpy as np

"""
Modern NumPy Random API guide (simple version).

Goals:
- Show why Generator is preferred over global state
- Show reproducibility and independent streams
- Show how to pick a BitGenerator when needed
"""


def bootstrap_mean(x: np.ndarray, n_boot: int, rng: np.random.Generator) -> np.ndarray:
    """Return bootstrap means using an explicit RNG."""
    n = x.shape[0]
    means = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        means[i] = x[idx].mean()
    return means


def main() -> None:
    print("Modern NumPy random API (short guide)")

    # 1) Reproducibility with Generator
    rng_a = np.random.default_rng(123)
    rng_b = np.random.default_rng(123)
    same = np.allclose(rng_a.normal(size=5), rng_b.normal(size=5))
    print("1) Same seed -> same result:", same)

    # 2) Independent streams for different app parts
    rng_train = np.random.default_rng(7)
    rng_eval = np.random.default_rng(999)
    print("2) Independent train stream:", np.round(rng_train.normal(size=3), 3))
    print("   Independent eval stream :", np.round(rng_eval.normal(size=3), 3))

    # 3) Pass RNG into functions instead of using global state
    values = np.array([10.0, 12.0, 14.0, 16.0, 18.0])
    boot = bootstrap_mean(values, n_boot=4, rng=np.random.default_rng(2026))
    print("3) Bootstrap means:", np.round(boot, 3))

    # 4) BitGenerator examples (engine under Generator)
    bit_generators = {
        "PCG64": np.random.PCG64(12345),
        "Philox": np.random.Philox(12345),
        "SFC64": np.random.SFC64(12345),
        "MT19937": np.random.MT19937(12345),
    }
    sample_by_engine = {
        name: np.round(np.random.Generator(bitgen).random(2), 3).tolist()
        for name, bitgen in bit_generators.items()
    }
    print("4) BitGenerator samples:", sample_by_engine)

    # 5) Legacy to modern migration summary
    print("5) Use rng.random, rng.integers, rng.normal, rng.choice instead of np.random.*")


if __name__ == "__main__":
    main()
