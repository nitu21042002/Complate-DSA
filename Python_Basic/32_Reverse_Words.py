#Write a program to reverse the words in a sentence.
st = "Hello My Self Nitu Yadav"
for srt in st.split():
    rev = ""
    for w in srt:
        rev = w + rev
    print(rev, end=" ")




#Write a program to reverse a sentence.
st="Hello My Self Nitu Yadav."
s=""
for i in st:
    s=i+s
print(s)