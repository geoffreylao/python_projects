# 2d lists and nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0]) # prints 1
print(number_grid[2][1]) # prints 8

for row in number_grid: # prints every element individually
    for col in row: 
        print(col)

