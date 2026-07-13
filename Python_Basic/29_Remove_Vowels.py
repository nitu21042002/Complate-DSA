#Write a program to remove vowels from a string.

st=input("Enter your string : ")
srt=""
for s in st:
    if s not in "aeiouAEIOU":
        srt+=s
print(srt)
