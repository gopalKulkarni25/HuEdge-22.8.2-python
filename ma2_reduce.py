# Take the first two values, run the function on them. Then take the result and the next value and have a multiplication between them. etc. When no more values are left, return the last result.

from functools import reduce

def alternate_ops(input_list):
    return reduce(lambda x,y: x+y , input_list)

print(alternate_ops([1,2,3,4]))