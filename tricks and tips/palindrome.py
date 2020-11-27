#to check given word is palindrome or not
word=input("")
palindrome=bool(word.find(word[::-1])+1)
print(palindrome)