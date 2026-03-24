# program to find the sum of even numbers
numbers = [1,2,3,4,5,6,7,8,9,10,12,16,23,34]

total = 0

for n in numbers:
    if n % 2 == 0:
        total = total+n

print("The sum of Even numbers is: ",total)        