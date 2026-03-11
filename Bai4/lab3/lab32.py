import math
from typing import Iterable


def geometric_mean(numbers: Iterable[float]) -> float:
    """Compute the geometric mean of a sequence of positive numbers.

    The geometric mean is defined as the n-th root of the product of the
    values. If any number is non-positive, a ValueError is raised because the
    geometric mean is only defined for positive values (zero yields 0).

    Args:
        numbers: An iterable of numbers (ints or floats).

    Returns:
        The geometric mean as a float.

    Raises:
        ValueError: If the iterable is empty or contains non-positive values.
    """

    numbers_list = list(numbers)
    if not numbers_list:
        raise ValueError("geometric_mean requires at least one number")

    # use logarithms to avoid overflow when multiplying many numbers
    log_sum = 0.0
    count = 0
    for x in numbers_list:
        if x <= 0:
            raise ValueError("all numbers must be positive")
        log_sum += math.log(x)
        count += 1

    return math.exp(log_sum / count)


if __name__ == "__main__":
    # simple demonstration
    sample = [1, 4, 9, 16]
    print("Geometric mean of", sample, "=", geometric_mean(sample))
