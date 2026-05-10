
import random
i=random.randrange(1,15)
n=int(input('enter number:'))
while i!=n:
    if n>i:
        print('input a small no')
        n=int(input('enter number again:'))
    elif n<i:
        print('input a large no')
        n=int(input('enter number again:'))
    else:
     break
    
print("hurray you guessed it correctly")