import pyperclip

# the string to be encrypt/decrypted
message = input("Enter a message: ")

# the encryption/decription key
key = int(input("Enter a key value(1 <-> 26): "))

# whether the program decrypts or encrypts
mode = input("Enter 'e' or 'd': ").lower()

# all possible symbols that can be encrypted
Symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# store translated string
translated = ""

for symbol in message:
    # note: only the symbols in Symbols can be encrypted/decrypted
    if symbol in Symbols:
        symbol_index = Symbols.find(symbol)

        # perform encryption/decryption
        if mode == "e":
            translated_index = symbol_index + key
        elif mode == "d":
            translated_index = symbol_index - key

        # handle wraparound, if needed
        if translated_index >= len(Symbols):
            translated_index = translated_index - len(Symbols)
        elif translated_index < 0:
            translated_index = translated_index + len(Symbols)

        translated = translated + Symbols[translated_index]
    else:
        # append the symbol without encrypting/decrypting
        translated = translated + symbol

# output the translated string
print(translated)
pyperclip.copy(translated)
