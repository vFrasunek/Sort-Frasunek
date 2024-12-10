pole = {1,52,96,12,73,65,21,78,99,10}

def Bubble_sort(pole):
 nvm = len(pole)
 for a in range(nvm):
   n = False

   for b in range(0,n-a-1):
     if pole[b] > pole[b+1]:
       pole[b], pole[b+1] = pole[b+1], pole[b]
       n = True

       if not n:
        break

 return pole

print("pole:", Bubble_sort(pole))


def 

