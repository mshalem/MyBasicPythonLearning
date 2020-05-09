#def is a keyword used to create function


def say_hi():  #definition of the the function
    print("Hello user")
print ("top")
say_hi()  #calling of the function
print("bottom")


#########################################################
#3##333Passing parameter to the function
###

def say_hi(name, age):
    print("hello " + name + "you are " + age)

say_hi("mike", "35")
say_hi("angel", "23")
###########################################################

def say_hi(name, age):
    print("hello " + name + "you are " + str(age))

say_hi("mike", 35)
say_hi("angel", 23)

#Return Statement in Functions

def cube(num):
    print(pow(num,3)) #prints the o/p, print doesnot require another print
    return(pow(num,3)) #retuns the o/p, but return requires print () before the funcction callin to print the returned value
#return is the last statement of any function, anything thats written after return is ignored.


print(cube(2))