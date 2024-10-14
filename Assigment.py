# KAMWIKARA SARAH KIARA
# M24B65/009
# B28776


# 1.10.Programming Exercises

#Number  1 
print("Hello, world!")
print("Hello", "world!")
print(3)
print(3.0)
print(2 + 3)
print(2.0 + 3.0)
print("2" + "3")
print("2 + 3 =", 2 + 3)
print(2 * 3)
print(2 ** 3)
print(2 / 3)

'''Output
a) Hello, world!
b) Hello world!
c) 3
d) 3.0
e) 5
f) 5.0
g) 23
h) 2 + 3 = 5
i) 6
j) 8
k) 0.6666666666666666'''

#Number 2
# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1- x)
        print(x)
main()
#Yes the chaos program functions as described in the chapter
'''Tried with inputs of 0.2 and 0.3
--0.2--                 --0.3--
0.6240000000000001  0.8907134336100001 
0.9150335999999998  0.3796377499070677
0.30321373239705673 0.3796377499070677
0.8239731430433209  0.9185004221350089
0.5656614700878645  0.29194384702399534
0.9581854282490118  0.8061792851144187
0.1562578420270518  0.6093915569306115
0.5141811824451928  0.9283306003619574
0.9742156868513789  0.2594782974949042
0.09796598114189214 0.7493823114337959
'''

#Number 3
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1- x)
        print(x)
main()
#Short paragraph describing differences I noticed in the behaviour of the two versions
'''
The original program with the 3.9 multiplier shows chaotic behavior, where small changes in input lead to unpredictable and fluctuating values over time.
In contrast, 
the modified version with the 2.0 multiplier quickly stabilizes,
with the output converging to 0.5 after just a few iterations,
regardless of the starting value.
This demonstrates that a smaller multiplier results in a more stable and predictable system,
while a higher multiplier leads to chaos.'''

#Number 4

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):  # Changed the loop to run 20 iterations
        x = 3.9 * x * (1 - x)
        print(x)

main()

#Number 5

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))  # Get the number of values to print from the user
    for i in range(n):  # Use n to control the number of iterations
        x = 3.9 * x * (1 - x)
        print(x)

main()

#Number 6
#program a
# (a)
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):  # Run 100 iterations
        x = 3.9 * x * (1 - x)  # Original formula
        print(x)

main()

# (b)
#program b
#This is the algebraically equivalent version.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):  # Run 100 iterations
        x = 3.9 * (x - x * x)  # Modified formula
        print(x)

main()

# (c)
#program c
#Another algebraically equivalent version.
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):  # Run 100 iterations
        x = 3.9 * x - 3.9 * x * x  # Modified formula
        print(x)

main()

#Explanation of Results:
"""
All three versions of the program perform the same calculation but express it differently.
Since these expressions are algebraically equivalent, they should theoretically produce identical results for each iteration.
However, when run over a large number of iterations (e.g., 100), you may notice very slight differences in the values due to the way floating-point arithmetic works on computers.
In practice, computers store floating-point numbers with limited precision, and small rounding errors can accumulate over time, especially in chaotic systems where small differences can grow quickly.
These differences in precision might cause the outputs to diverge slightly after many iterations. Despite this, the overall chaotic behavior remains the same across all three versions.

In summary:

All three programs will produce almost identical results, but over 100 iterations, tiny discrepancies may appear due to floating-point rounding errors, a characteristic of chaotic systems.
These small differences do not change the overall chaotic nature of the logistic function in each version."""

#Number 7

def main():
    print("This program illustrates a chaotic function with two inputs")
    
    
    x1 = eval(input("Enter the first number between 0 and 1: "))
    x2 = eval(input("Enter the second number between 0 and 1: "))
    
    # Print table header
    print(f"{'input':<10}{x1:<10}{x2:<10}")
    print("-" * 30)
    
    
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print(f"{x1:<10.6f}{x2:<10.6f}")

main()
