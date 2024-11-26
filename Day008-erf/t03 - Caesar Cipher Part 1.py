from clear_sc import clear_screen
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt")


def main():
  clear_screen()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number(1-25):\n"))
  def encrypt(original_text, shift_amount):
    encrypt_message = ''
    for x in original_text:
      real_index = alphabet.index(x)
      encrypt_index = real_index + shift_amount
      encrypt_letter = alphabet[encrypt_index]
      encrypt_message += encrypt_letter
    print(encrypt_message)

  encrypt(text, shift)


while True:
  main()
  if input("continue?(y/n)").lower() !='y':
    break
