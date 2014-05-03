inputWord = raw_input("Enter a word: ")
v = int(raw_input("Enter number of shift: "))

def wrap(v, a, z):
    if v > z:
        v -= 26
    elif v < a:
        v += 26
    return v

def rotate_word(word, amt):
    encry = ''
    for ch in word: #ch is the character
        if not ch.isalpha():
            encry+= ch 
        elif ch.isupper():
            encry += chr(wrap(ord(ch) + amt, 65, 90))
        else:
            encry += chr(wrap(ord(ch) + amt, 97, 122))
    return encry
    
print rotate_word(inputWord, v)

