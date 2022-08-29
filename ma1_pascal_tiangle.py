# Loops Assignment 

# Write a program to input an integer N from user and print pascal triangle up to N rows. 

def display_pascal_triangle(input_value):
    output_display = [[] for i in range(input_value)]
    for i in range(0,input_value):
        for j in range(0,input_value):
            if(j<i):
                if(j==0):
                    output_display[i].append(1)
                else:
                    output_display[i].append(output_display[i-1][j] + output_display[i-1][j-1])
            elif(j==i):
                    output_display[i].append(1)
            else:
                output_display[i].append(0)
    
    return output_display

print(display_pascal_triangle(int(input("enter a number"))))