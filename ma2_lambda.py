#Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c

parabola_exp = lambda a,x,b,c: (a*x**2)+b*x+c

print(parabola_exp(1,2,3,4))