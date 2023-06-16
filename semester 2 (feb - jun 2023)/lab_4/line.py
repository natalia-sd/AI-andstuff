"""
Line setting module.
"""
from typing import Tuple
import numpy as np

class Line():
    def __init__(self, x: np.ndarray, y: np.ndarray) -> None:
        self.k = None
        self.b = None
        self.x = x
        self.y = y

    def estimate_params(self) -> None:
        points_num = len(self.x)
        if points_num < 2:
            raise ValueError(f"Not enough points. Must be at least 2, but got {points_num}.")
        else:
            A = np.vstack([self.x, np.ones(len(self.x))]).T
            self.k, self.b = np.linalg.lstsq(A, self.y, rcond=None)[0]

    def get_params(self) -> Tuple[float, float]:
        return (self.k, self.b)

    def set_params(self, k: float, b: float) -> None:
        self.k = k
        self.b = b

    def devide_points(self, x: np.ndarray, y: np.ndarray, eps: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        inliers_x = []
        inliers_y = []
        outliers_x = []
        outliers_y = []
        for k_x, k_y in zip(x, y):
            if abs(k_y - k_x*self.k - self.b) < eps:
                inliers_x.append(k_x)
                inliers_y.append(k_y)
            else:
                outliers_x.append(k_x)
                outliers_y.append(k_y)
        return (inliers_x, inliers_y, outliers_x, outliers_y)