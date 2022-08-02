print("Hollow Square Star Pattern")
def Hollow_Pattern(a):
    i = 0
    while(i < a):
        j = 0
        while(j < a):
            if(i == 0 or i == a - 1 or j == 0 or j == a - 1):
                print('*', end = '  ')
            else:
                print(' ', end = '  ')
            j = j + 1
        i = i + 1
        print()
lenght = int(input("Please Enter The Length of a Square  : "))
Hollow_Pattern(lenght)

