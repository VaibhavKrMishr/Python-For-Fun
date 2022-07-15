num = input("Enter a No.: ")
n = len(num)
sum_ = 0
num1 = int(num)
while num1 > 0:
    for j in num:
        k = int(j)
        sum_ += k**n
    if num1 == sum_:
        print(num1,"is an Armstrong number")
    else:
        print(num1,"is not an Armstrong number")
    break
