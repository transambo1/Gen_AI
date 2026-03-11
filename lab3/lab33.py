from functools import reduce  


def get_geometric_mean_for_three_numbers(a, b, c): 
    return (a*b*c)**(1/3)


def get_geometric_mean(*nums: float) -> float: 
    """ 
    Get the geometric mean of a sequence of numbers  
    """ 

    if not len(nums):  
        raise ValueError("Cannot calculate the geometric mean of an empty sequence") 

    product = reduce(lambda a, b: a * b, nums) 
    if product < 0 and len(nums) % 2 == 0: 
        raise ValueError("Cannot calculate the geometric mean") 

    return pow(product, 1 / len(nums)) 


if __name__ == "__main__":
    print(get_geometric_mean_for_three_numbers(2,4,8))
    print(get_geometric_mean(2,4,8))
    print(get_geometric_mean(1,3,9))