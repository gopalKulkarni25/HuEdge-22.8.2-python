# program to print the center star pattern

def print_star_pattern(x):

        for i in range(x):
            print(' '*(x-i)+'*'*(i*2+1))
        for j in range(x-2,-1,-1):
            print(' '*(x-j)+'*'*(j*2+1))

x=5

print(print_star_pattern(x))
