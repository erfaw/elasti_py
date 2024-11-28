from clear_sc import clear_screen
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def main():
    clear_screen()


    def caesar(direction, original_text, shift_amount):
        def encrypt():
            encrypt_message = ''
            for x in original_text:
                encrypt_index = alphabet.index(x) + shift_amount
                encrypt_message += alphabet[encrypt_index]
            print(encrypt_message)


        def decrypt():
            decrypt_message = ''
            for x in original_text:
                encrypt_index = alphabet.index(x) - shift_amount
                decrypt_message += alphabet[encrypt_index]
            print(decrypt_message)


        if direction == 'encode':
            encrypt()
        elif direction == 'decode':
            decrypt()
        else:
            input('pick again , wrong choice')
        # encrypt(text, shift) # erfan -2-> gthcp
        # decrypt(text, shift)
    
    direction = input("Type 'encode' to encrypt,\nType 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number(1-25):\n"))
    caesar(direction, text, shift)

while True:
    main()
    if input("continue?(y/n)").lower() !='y':
        break
