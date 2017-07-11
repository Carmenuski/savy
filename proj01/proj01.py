# Name:
# Date:
# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.
# If you complete extensions, describe your extensions here!
name = raw_input("Enter your name: ")

print name

a = raw_input("Enter your age: ")
a=int(a)
print a
y=2017-a
w=y+100

birthday = raw_input("Has your birthday happened yet: ")

if birthday == "no":
    a=int(a)
    y=2017-a
    w = y + 99
    print name, "will turn 100 in the year",w

if birthday == "yes":
    a=int(a)
    y = 2017 - a
    w = y + 100
    print name, "will turn 100 in the year",w








