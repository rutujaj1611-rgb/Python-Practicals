text= input("Enter a string  ")
print("Length :", len(text))
print("Upper case:" , text.upper)
print("Lower case", text.lower)
print("Reversed string: ", text[::-1])
char=input("Enter characters to count")
print("Count:" , text.count(char))

words= text.split()
print(words)

words=["Java", "Python", "c"]
result="".join(words) 
print(result)

sub= input("Enter substring")
if sub in text:
    print("Substring found")
else:
    print("Substring not found")

old=input("Enter a word to replace")
new=input("Enter new word")
print("New string:", text.replace(old,new))

