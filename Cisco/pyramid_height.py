#pyramid height

blocks = int(input("Enter the number of blocks: "))
height = 0
total = 0

for b in range(1, blocks +1 ):
     total += b
     if total>blocks:
        break
     height+=1

    
print("The height of the pyramid:", height)

