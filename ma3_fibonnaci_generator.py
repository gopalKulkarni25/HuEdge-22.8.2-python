"""Create a generator to return the fibonnaci sequence starting from the first element   

up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,  89, . . .   """


def fib_generator(n):
    n1, n2 = 0, 1
    for i in range(n):
        yield n1
        n1, n2=n2 , n1+n2
        


g = list(fib_generator(10))

print(g)
