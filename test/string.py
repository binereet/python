'''
Created on Oct 31, 2023

@author: Lenovo
'''
s = 'binereet'
print(s[2:6])
print(s.count("e"))


name = "HarryIsGood"
e = name[0::3]
d = name[:0:-1]
print(d)
print(e)
print(name[0:4])



story = "Harry is good.\nHe\tis ve\'ry good"
print(story)


print(" hello\n My name is Biney\'s Iphone\t i am 8 years old")



letter = '''Dear name,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: date
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("name", name)
letter = letter.replace("date", date)
print(letter)