#2d lists and nested loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][2]) #first [] refers to row and second [] refers to column. here [0][2] gives 3

#Nested Loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in number_grid:
    print(i)

for i in number_grid:  #i will get the value of each row
    for j in i:       #j will get each value of i
        print (j)
