#Write a program to join a list of strings into a sentence.

lst=" ".join(["I","Love","My","Self","."])
print(lst) # space . join join all the elements of list and make it sentance.

words = ["Hello", "World", "My", "Self","Nitu"]
print(" ".join(words))

#using loop
words = ["I", "Am", "Learning", "Python"]
sentence = ""
for word in words:
    sentence += word + " "
print(sentence)