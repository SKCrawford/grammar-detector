from functools import reduce
from operator import concat


# Source: https://stackoverflow.com/a/45323085
def flatten(a):
    """Flatten a multi-dimensional List to one-dimensional List."""
    return reduce(concat, a)
