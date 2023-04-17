if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
new_list = [[myx, myy, myz] for myx in range (x+1) for myy in range (y+1) for myz in range (z+1) if myx+myy+myz != n]

print(new_list)