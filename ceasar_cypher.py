def cypher(word, num):
    ''' will shift the characters depending on the key

    args:
        word: will be the word inserted, string value
        num: will determine what the new character will be, integer value

    return: word after being encrypted, string value
    '''
    answer = []
    remainder = 0

    for i in word:
            remainder = 0
            if (ord(i) + num) < 97:
                remainder = (ord(i) + num) - 97
                answer.append(chr(123 + remainder))
            elif (ord(i) + num) > 122:
                remainder = (ord(i) + num) - 122
                answer.append(chr(96 + remainder))
            else:
                 answer.append(chr(ord(i) + num))
    
    final = "".join(map(str, answer))
    return(final)

test_str = input("")
test_num = int(input(""))


print(cypher(test_str, test_num))
                