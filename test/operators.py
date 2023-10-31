'''
Created on Oct 31, 2023

@author: Lenovo
'''
a = 3
b = 4

# Arithmetic Operators
print("The value of 3+4 is ", 3+4)
print("The value of 3-4 is ", 3-4)
print("The value of 3*4 is ", 3*4)
print("The value of 3/4 is ", 3/4)

a = 458
b = 15

print("The remainder when a is divided by b is", a%b)

# Assignment Operators
a = 34
a -= 12
a *= 12
#a /= 12
print(a)

# Comparison Operators
# b = (14<=7)
# b = (14>=7)
# b = (14<7)
# b = (14>7)
# b = (14==7)
b = (14!=7)
print(b)

# Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))

#typecasting 

o = 10
print(type(o))
o = str(o)
print(type(o))


a = 30
b = 15
print("The sum of a and b is", a + b)



a=int(input( "enter value of a "))
b= int(input("enter value of b"))
print("c=",a+b)


#square
p = 10
print(pow(10,2))
