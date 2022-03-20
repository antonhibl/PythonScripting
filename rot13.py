import codecs

text = input("Enter some text: ")

text = codecs.encode(text, "rot13")

print(text)
