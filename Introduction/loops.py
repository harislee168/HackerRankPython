n = int(input())
    
if n >= 1 and n <= 20:
    for i in range(n):
        print(i**2)
else:
    print('n is out of constraints')