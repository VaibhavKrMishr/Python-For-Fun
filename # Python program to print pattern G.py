# Python program to print pattern G
def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if (row == 0 and (column != 0 and column != n-1)) or (row == n - 1 and (column != 0 and column != n-1)) or ((column == 0 and (row != 0 and row != n-1)) or (column == n-1 and row != n-1 and row >= (n/2)-1)) or (row == (n/2)-1 and ((n/2)-1 <= column < n-1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


a = int(input("Enter size: "))
print_pattern(a)
