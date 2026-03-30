from memory_profiler import profile
import pandas as pd

@profile
def get_top_video(path):
    interactions = pd.read_csv(path)

    avg_ratio = interactions.mean(axis=0, skipna=True)

    return avg_ratio.idxmax()

if __name__ == "__main__":
    get_top_video('interactions_10_000.csv')





