


#KAMWIKARA SARAH KIARA
#M24B65/009
#B28776

#TEST 2 SOLUTIONS
#a
def find_even(numbers):
    return [num for num in numbers if num%2==0]

numbers= [9,11,13,4,2]
even_numbers_found = find_even(numbers)
print(even_numbers_found)

#b

def multi_table(n):
    for i in range(1,13):
        print(f"{n} x {i} = {n * i}")
#Implementation example

multi_table(6)


#c

def find_largest(numbers):
    largest= numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

#Implementation Example
numbers =[22,33,45,56,97]
largest = find_largest(numbers)
print(largest)


#d

def is_palindrome(string):
    return string==string[::-1]

string = 'kashara'
print(is_palindrome(string))
