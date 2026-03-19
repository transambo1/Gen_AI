import numpy as np

def compute_manhattan_distance(matrix):
    """Tính khoảng cách Manhattan bằng Vectorization."""
    return np.abs(matrix[:, None] - matrix).sum(-1)

def compute_euclidean_distance(matrix):
    """Tính khoảng cách Euclidean bằng Vectorization."""
    return np.sqrt(((matrix[:, None] - matrix) ** 2).sum(-1))

def calculate_distance_optimized(data, dist_type="euclidean"):
    matrix = np.array(data)
    if dist_type == "manhattan":
        return compute_manhattan_distance(matrix)
    return compute_euclidean_distance(matrix)