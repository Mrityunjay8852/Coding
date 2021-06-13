#print pattern
i=1
while i<=6:
    b=1
    while b<=6-i:
        print(' ',end='')
        b=b+1
    j=1
    while j<=i:
        print('#',end='')
        j=j+1
    print()
    i=i+1