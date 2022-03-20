message = input("Enter a message: ")
Symbols = u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through all possible keys
for key in range(len(Symbols)):
    translated = u''

    # loop through each symbol in message
    for symbol in message:
        if symbol in Symbols:
            symbol_index = Symbols.find(symbol)
            translated_index = symbol_index - key

            # handle the wrap-around
            if translated_index < 0:
                translated_index = translated_index + len(Symbols)

            # append the decrypted symbol
            translated = translated + Symbols[translated_index]

        else:
            # append the symbol without encrypting/decrypting
            translated = translated + symbol

    # display every possible decryption
    print(u'Key #{}s: {}'.format(key, translated))

