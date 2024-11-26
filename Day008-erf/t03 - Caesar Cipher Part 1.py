alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1
def encrypt(original_text, shift_amount):
  encrypt_message = ''
  for x in original_text:
    real_index = alphabet.index(x)
    encrypt_index = real_index + shift_amount
    encrypt_letter = alphabet[encrypt_index]
    encrypt_message += encrypt_letter
  return encrypt_message

print(encrypt('hello', 1))
