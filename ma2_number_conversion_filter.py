#Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.   

def negative_to_positive(input_list):
    output_list = []
    output_list = list(filter(lambda item: item if(item > 0) else None,map(lambda el: el*-1 , input_list)))
    return output_list


print(negative_to_positive([-1000, 500, -600, 700, 5000, -90000, -17500]))