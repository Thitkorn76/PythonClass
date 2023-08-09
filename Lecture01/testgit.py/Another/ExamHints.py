inputmsg = input(" In put srtring you want it swap words:")
print(inputmsg.split())
separatewords = inputmsg.split()

print("separate words")
for i in separatewords:
    print(i)

print("Modify each words")
for j in range(len(separatewords)):
    separatewords[j] = 'G' + separatewords[j]
    print(separatewords[j])

print(separatewords)
print(" ".join(separatewords),)