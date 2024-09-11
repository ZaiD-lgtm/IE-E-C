size = int(input("Enter the size of matrix: "))
'''
[
[a11, a12, a13],
[a21,a22,a23],
[a31,a32,a33]
]
'''

matrix = []
n = 1
while size >= n:

    row = []
    for i in range (1, size +1):
        x = int(input(f"a{n}{i}: "))
        row.append(x)

    matrix.append(row)
    n += 1
for i in matrix:
    print(i)

def transpose(matrix):
        return list(zip(*matrix))

transposed= transpose(matrix)
print(transposed)