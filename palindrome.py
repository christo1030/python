#palindrome.py

print(' Returns True if s is a palindrome, False otherwise')
input = raw_input('Enter a word: ')
def is_palindrome(input):
    if input == '':
        return True
    else:
        if (ord(input[0]) - ord(input[len(input)-1])) == 0:
            return is_palindrome(input[1:len(input)-1])
        else:
            return False

if is_palindrome(input):
    print "Palindrome"
else:
    print "NOT Palindrome"
