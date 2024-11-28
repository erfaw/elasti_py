from clear_sc import clear_screen
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
clear_screen()
print(logo)
input('press "Enter" to continue')

def main():
    clear_screen()


    # def caesar(direction, original_text, shift_amount):
    #     def encrypt():
    #         encrypt_message = ''
    #         for x in original_text:
    #             encrypt_index = alphabet.index(x) + shift_amount
    #             encrypt_index %= len(alphabet)
    #             encrypt_message += alphabet[encrypt_index]
    #         print(encrypt_message)


    #     def decrypt():
    #         decrypt_message = ''
    #         for x in original_text:
    #             decrypt_index = alphabet.index(x) - shift_amount
    #             decrypt_index %= len(alphabet)
    #             decrypt_message += alphabet[decrypt_index]
    #         print(decrypt_message)


    #     if direction == 'encode':
    #         encrypt()
    #     elif direction == 'decode':
    #         decrypt()
    #     else:
    #         input('pick again , wrong choice')
    #     # encrypt(text, shift) # erfan -2-> gthcp
    #     # decrypt(text, shift)
    # caesar() from course:
    def caesar(direction, original_text, shift_amount):
        if direction == 'decode':
            shift_amount *= -1   

        encrypt_message = ''
        for x in original_text:

            if x in alphabet:
                encrypt_index = alphabet.index(x) + shift_amount
                encrypt_index %= len(alphabet)
                encrypt_message += alphabet[encrypt_index]
            else: 
                encrypt_message += x
            

        print(encrypt_message)


    direction = input("Type 'encode' to encrypt,\nType 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number(any shift number is accepted):\n"))
    caesar(direction, text, shift)

while True:
    main()
    if input("continue?(y/n)").lower() !='y':
        break
