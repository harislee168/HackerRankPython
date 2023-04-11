def minion_game(string):
    # your code goes here
    vowel ='AEIOU'
    start_index = 0
    consonant_stuart_list = list()
    vowel_kevin_list = list()

    for character in string:
        if (character not in vowel):
            processStringList(character, string, start_index, consonant_stuart_list)
        else:
            processStringList(character, string, start_index, vowel_kevin_list)
        start_index+=1
    
    if len(consonant_stuart_list) > len(vowel_kevin_list):
        print('Stuart', len(consonant_stuart_list))
    else:
        print('Kevin', len(vowel_kevin_list))    
    
def processStringList(character, string, start_index, myList):
    str_len = len(string)
    end_index = start_index + 1
    while end_index <= str_len:
        myList.append(string[start_index:end_index])
        end_index+=1
    
    
        
if __name__ == '__main__':