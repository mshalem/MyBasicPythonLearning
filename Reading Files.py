bible_file = open("C:\/Users\Janaki\Documents\pyth.txt", "r") #r readonly, w writeonly, a append only, r+ read write and append
#print(bible_file.readable())
#print(bible_file.read())
#print(bible_file.readline())
print_index = bible_file.readlines()
print(print_index[0])
for i in print_index:
    print(i)
bible_file.close()
