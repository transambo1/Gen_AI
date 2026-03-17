from typing import Dict

def get_geometric_mean(net_returns: Dict[str, float]) -> float:
    n = len(net_returns)

    if n == 0:
        return 0.0

    product = 1.0

    for r in net_returns.values():
        product *= (1 + r)

    geometric_mean = product ** (1 / n) - 1

    return geometric_mean


returns = {
    "AAPL": 0.10,
    "MSFT": 0.05,
    "GOOG": -0.02
}

print("Geometric Mean:", get_geometric_mean(returns))
