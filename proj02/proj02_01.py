# Name:
# Date:
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
# The sum of your number is 21
sum = 0
loop_control = True
while loop_control==True:
    number1 = int(raw_input("Enter a number to add, or 0 to show that you are finished: "))
    #sum = number1
    if int(number1)!=0:

        sum = sum + number1
        number1=("Enter a number to add, or 0 to show that you are finished: ")
    else:
        loop_control = False

print sum, "is the sum of your numbers"