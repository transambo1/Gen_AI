import pandas as pd

def get_top_video_optimized(path):
    cumulative_sum = None
    cumulative_count = None

    chunksize = 1000

    for chunk in pd.read_csv(path, chunksize=chunksize):
        chunk_sum = chunk.sum(skipna=True)
        chunk_count = chunk.count()

        if cumulative_sum is None:
            cumulative_sum = chunk_sum
            cumulative_count = chunk_count
        else:
            cumulative_sum += chunk_sum
            cumulative_count += chunk_count

    return (cumulative_sum / cumulative_count).idxmax()




