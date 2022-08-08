a = int(input("Enter the size of the pattern: "))

pattern = [[0 for i in range(a)] for j in range(a)]

num = 1 
i = 0 
j = 0 
m = 0 
n = a - 1 
p = 0 
q = a - 1 

while num <= a * a:
    # fill left to right
    for j in range(p, q + 1):
        pattern[m][j] = num
        num = num + 1
    m = m + 1

    # fill top to bottom
    for i in range(m, n + 1):
        pattern[i][q] = num
        num = num + 1
    q = q - 1

    # fill right to left
    for j in range(q, p - 1, -1):
        pattern[n][j] = num
        num = num + 1
    n = n - 1

    # fill bottom to top
    for i in range(n, m - 1, -1):
        pattern[i][p] = num
        num = num + 1
    p = p + 1

print("");
for i in range(0, a):
    for j in range(0, a):
        print(pattern[i][j], end = "\t")
    print("")