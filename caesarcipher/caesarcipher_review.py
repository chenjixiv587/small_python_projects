SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
maxKey = len(SYMBOLS) - 1  # 0 - 25
while True:
    print("Do you want to encrypt or decrypt, e means encrypt d means decrypt")
    response = input().lower().strip()
    if response == 'e':
        mode = 'encrypt'
        break
    elif response == 'd':
        mode = 'decrypt'
        break
    print("You should enter e or d")


while True:
    print(f"What key do you want to enter, key is 0 - {maxKey}")
    response = input().lower().strip()
    if not response.isdecimal():
        continue
    elif 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print("What message do you want to encrypt/decrypt")
message = input().upper().strip()
translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num += key
        elif mode == "decrypt":
            num -= key

        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        translated += SYMBOLS[num]
print(translated)
