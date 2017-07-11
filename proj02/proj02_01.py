# Name: Nunya buisness
# Date: Dunno
# proj02: sum
# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.
#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21
("addition")
number1 = raw_input("Enter a number: ")
print number1
number2 = raw_input("Enter a number: ")
print number2
number3 = raw_input("Enter a number: ")
print number3
number4 = raw_input("Enter a number: ")
print number4
A = int(number1)
B = int(number2)
C = int(number3)
D = int(number4)
E = A+B+C+D
print E, "is the answer."
