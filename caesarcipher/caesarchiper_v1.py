# the base symbols can be letters and numbers and punctuation
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("the caesar cipher encrypts and decrypts")

# let the user enter if they are encrypting or decrypting
while True:  # keep looping until the user enter e or d
    print("Do you want to (e)ncrypt or (d)ecrypt the letter? ")
    response = input("> ").lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("please enter e or d")

# let the user enter the key to use
while True:  # keep looping until the user enter the valid key
    maxKey = len(SYMBOLS) - 1
    print(f"Please enter the key 0 to {maxKey} to use")
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let the user enter the message to encrypt or decrypt
print(f"enter the message you want to {mode}")
# Caesar cipher only words on upper case
message = input("> ").upper()

# stored the encrypted or decrypted form of the message
translated = ''

# encrypt or decrypt each symbol in the message

for symbol in message:
    if symbol in SYMBOLS:
        # get the decrypt or decrypt number for this symbol
        num = SYMBOLS.find(symbol)  # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # handle the wrap-around if num is larger than the length of SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # add the encrypted or decrypted number's symbol to translated
        translated += SYMBOLS[num]
    else:
        # just add the symbol without encryt or decrypt
        translated += symbol
print(translated)
