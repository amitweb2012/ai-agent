import numpy as np


def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    """Calculate cosine similarity between two numeric vectors."""
    v1 = np.asarray(vector1, dtype=float)
    v2 = np.asarray(vector2, dtype=float)
    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)
    if denominator == 0:
        return 0.0
    return float(np.dot(v1, v2) / denominator)
