if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
myList = list()
for myx in range(x+1):
    for myy in range (y+1):
        for myz in range (z+1):
            if myx+myy+myz != n:
                myList.append([myx,myy,myz])
print(myList)