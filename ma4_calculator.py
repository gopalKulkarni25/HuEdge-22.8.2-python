#interactive calculator with error handling
import operator
ops = { "+": operator.add, "-": operator.sub }

class FormulaError(Exception):
    pass

print("Enter value as a expression . Eg. 1+1")


def interactive_calc(expr):
    expr_split = [*expr]
    # print(expr_split)
    try:
        if(len(expr_split) != 3):
            raise FormulaError
        elif(expr_split[1] != "+" and expr_split[1] != "-"):
            raise FormulaError
    except FormulaError:
        print("Please enter valid expression")
    if(expr_split[1] == "+"):
        print(ops["+"](int(expr_split[0]),int(expr_split[2])))
    elif(expr_split[1] == "-"):
        print(ops["-"](int(expr_split[0]),int(expr_split[2])))
    
while True:
  user_input = input('> > ')
  if user_input == 'quit':
    break
  interactive_calc((user_input))
