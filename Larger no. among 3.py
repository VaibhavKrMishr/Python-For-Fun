i1 = int(input('Enter 1st Number: '))
i2 = int(input('Enter 2nd Number: '))
i3 = int(input('Enter 3rd Number: '))

if i1 > i2 > i3:
    print (f"\nThe Larger No. Among The Three Is:{i1}\n")
elif i1 < i2 > i3:
    print (f"\nThe Larger No. Among The Three Is:{i2}\n")
elif i1 < i2 < i3:
    print (f"\nThe Larger No. Among The Three Is:{i3}\n")
    
elif i1 < i2 == i3:
    print (f"\nThe Larger No. Among The Three Is:{i2}\n")
elif i1 > i2 == i3:
    print (f"\nThe Larger No. Among The Three Is:{i1}\n")
    
elif i1 == i2 < i3:
    print (f"\nThe Larger No. Among The Three Is:{i3}\n")
elif i1 == i2 > i3:
    print (f"\nThe Larger No. Among The Three Is:{i1}\n")
    
elif i1 == i3 < i2:
    print (f"\nThe Larger No. Among The Three Is:{i2}\n")
elif i1 == i3 > i2:
    print (f"\nThe Larger No. Among The Three Is:{i3}\n")

elif i1 == i2 == i3:
    print (f"\nThe Larger No. Among The Three Is:{i1}\n")
input()


