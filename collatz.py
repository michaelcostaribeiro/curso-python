c0 = int(input("Set a integer number: "))
steps = 0

while c0 != 1:
    if c0%2==0:
        steps += 1
        c0 //= 2
        print(c0)
    else:
        steps += 1
        c0 = 3 * c0 + 1
        print(c0)
        

print("steps =", steps)
