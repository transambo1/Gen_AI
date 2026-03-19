def calculate_distance(data, dist_type):
    results = []
    for i in range(len(data)):
        row_results = []
        for j in range(len(data)):
            if dist_type == "manhattan":
                d = 0
                for k in range(len(data[i])):
                    d += abs(data[i][k] - data[j][k])
                row_results.append(d)
            elif dist_type == "euclidean":
                d = 0
                for k in range(len(data[i])):
                    d += (data[i][k] - data[j][k])**2
                row_results.append(d**0.5)
        results.append(row_results)
    return results



