import numpy as np
import pandas as pd

def get_manhattan_distance(
        df1: pd.DataFrame,
        df2: pd.DataFrame,
) -> np.float64:
    element_wise_dist: pd.DataFrame = (df1 - df2).abs()
    dist: float = element_wise_dist.sum().sum().astype(float)
    return dist
if __name__ == "__main__":
    df1 = pd.DataFrame({
        'A': [1.0, 2, 3.5, 4, 5.1],
        'B': [6, 7.2, 8, 9.1, 10],
        'C': [11.3, 12, 13.4, 14, 15]
    })
    df2 = pd.DataFrame({
        'A': [1.5, 2.5, 3, 4.5, 5],
        'B': [6.5, 7, 8.5, 9, 10.2],
        'C': [11, 12.5, 13, 14.5, 15.2]
    })
    distance = get_manhattan_distance(df1, df2)
    print(f"Khoảng cách Manhattan là: {distance}")