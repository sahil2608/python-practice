# Python Program to Remove Punctuation from a String

punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''

sent = input("Enter the String: ")
no_pun = "" # another string to store string without punctuation
for i in sent:
    if i not in punctuation:
        no_pun = no_pun + i

print(no_pun)