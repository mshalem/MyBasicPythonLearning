try:
    #value=10/0
    number= int(input("Enter a Valid number: "))
    print (number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err1:
    print(err1)
except:
    print("generic error")