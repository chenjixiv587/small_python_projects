SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# ask the user encrypt the message or decrypt the message

while True:
    print("Do you want to (e)ncrypt or (d)ecrypt ?")
    print('e means encrypt d means decrypt')
    response = input("> ").lower()
    if response == "e":
        mode = 'encrypt'
        break
    elif response == 'd':
        mode = 'decrypt'
        break
    else:
        print("You should enter e or d")

# ask the user to enter the key
while True:
    maxKey = len(SYMBOLS) - 1
    print("please enter the key to e or d")
    print(f"the key you can enter is 0 - {maxKey}")
    response = input("> ").upper()
    if not response.isdecimal():
        continue
    elif 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
# store the result of the msesage
translated = ""

# let user enter the message
print("Please enter the message to encrypt or decrypt")
message = input("> ").upper()
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num += key
        elif mode == "decrypt":
            num -= key

        # change num if num > len(SYMBOLS) or num < 0
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

    translated += SYMBOLS[num]

print(translated)
