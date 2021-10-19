# Ex1
"""
John, 66.3, 170.2
Jane, 54.1, 162.8
Jimmy, 89.5, 179.8
"""

# Ex2
table = [
    ["John", 66.3, 170.2],
    ["Jane", 54.1, 162.8],
    ["Jimmy", 89.5, 179.8]
]

# Ex3
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
data[-1]
data[1]
data[2][0]
data[0][1]

# Ex4
table = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
col0 = [i[0] for i in table]

# Ex5
table = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
new_table = [row for row in table if row[-1]%2==0]