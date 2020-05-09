friends = ["kevin","karen","jim", "john","alex"]
lucky_numbers = [4, 6, 8, 9, 34, 57, 67]
print(friends)
friends.append("shane")  #appends additional element to the list
#friends.extend(lucky_numbers) #concatenate two lists
friends.insert(3, "shalem")  #inserts element at a particular number
print(friends)
popped_friends= friends.pop() #prints or pops out last element in the list
print(popped_friends)
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