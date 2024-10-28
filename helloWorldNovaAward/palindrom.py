word = str(input('Please enter a lowercase word with no spaces:'))

#Creates a loop that will iterate through every character of the word
w=''
for i in word:
    w = i + w
    
if (word==w):
    print("Yes your word is a Palindrome")
else:
    print("No your word is not a Palindrome")

'''
#Function that will see if the word is a palindrome
def palindrome(str):
    #Run's the loop starting at 0 and goes until it takes the length of the word/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

word = str(input('Please Enter a Word?'))
ans = palindrome(word)

if (ans):
    print("Yes, your word is a palindrome")
else:
    print("No your word is not a palindrome")

'''


