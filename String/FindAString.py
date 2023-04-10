def count_substring(string, sub_string):
    count = 0
    stringLength = len(string)
    i = 0
    iSubLength = i + len(sub_string)
    
    while iSubLength <= stringLength:
        if sub_string == string[i:iSubLength]:
            count += 1
        i+=1
        iSubLength+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)