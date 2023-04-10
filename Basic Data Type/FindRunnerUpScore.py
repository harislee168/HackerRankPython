if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_arr = sorted(list(arr))
    array_index = n-1
    max_value = list_arr[array_index]
    
    while array_index >= 0:
        if list_arr[array_index] < max_value:
            print(list_arr[array_index])
            break
        array_index -=1