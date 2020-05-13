friends = ["kevin","karen","jim", "john","alex"]
lucky_numbers = [4, 6, 8, 9, 34, 57, 67]
print(friends)
friends.append("shane")  #appends additional element to the list
#friends.extend(lucky_numbers) #concatenate two lists
friends.insert(3, "shalem")  #inserts element at a particular number
print(friends)
#popped_friends= friends.pop() #prints or pops out last element in the list
#print(popped_friends)
friends.remove("karen") #removes mentioned element from the list
print(friends)
#friends.clear() #clears or removes everything in the list
print(friends)
print(friends.index("kevin")) #it will gives us the index of the element, if the element in not present it will end in error,
#like this we can chek if the element is present in the list or not.
print(friends.count("jim"))  #it will give count of the elements ( how many times it appeared)
friends.sort() #sorts the list
lucky_numbers.sort() #sorts the list in ascending order
print(friends)
print(lucky_numbers)
friends2 = friends.copy() #copies friends to friends2
print(friends2)

#creating list using list comprehension (using for loop)
"""
it assigns numbers range from 0 to 9 to i, 
"""
listofnum = [i for i in range(0,10)]  # range mean (0,n) prints 0 to n-1
print(listofnum)
simplelist = list(range(0,10,3))   #  range mean (0,n,x) prints 0 to n-1 leaving x-1 items in between each numbers
print(simplelist)
#creating ;ist from comma seperated string

createlistfromsep = "hello,this,is,my,name"
listfromsep = createlistfromsep.split(',')
print(listfromsep)

listfromstring = "hello"
charlist = list(listfromstring)
print(charlist)
#samething with integers

integer = 12345
intolist = [int(i) for i in str(integer)]
print(intolist)

#converting dictioonary to list
dict = {'a':1,'b':2}
a = list(dict.keys())
print(a)
b = list(dict.keys())
print(b)

#popular functions in list
#difference between append() and extend()
#insert item at a particular position, here added not_Add after bolo
l2 = ["goat", "cat", "hello", "bolo", "not"]
boloindex = l2.index('bolo')
l2.insert(boloindex+1, 'new_Add')
print(l2)

l3 = ["goat", "cat", "hello", "bolo", "not"]
l3.remove('not')
print(l3)
l4 = ["goat", "cat", "hello", "bolo", "not"]
xpoppedx = l4.pop(0) #by default pop will pop out lat, you can pop based on ind4ex also like below
print(xpoppedx)

l5 = [3,4,6,2,4,5,]
l5.sort()
print(l5)
l5.sort(reverse=1)
print(l5)
l6 = [3,4,6,2,4,5,]
l6.reverse()
print(l6)
lenl6 = len(l6)
print(lenl6)
minl6 = min(l6)
print(minl6)
maxl6 = max(l6)
print(maxl6)
cnt = l6.count(4)
print(cnt)
l6.clear()