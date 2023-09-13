import os

def main_decryption():
    with open("encryption.txt", "r") as f:
        content = f.read().split("\n---\n")
        encryption_alphabet, encrypted_message = content[0], content[1]

    standard_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

    decrypted_message_list = []
    for char in encrypted_message:
        char_lower = char.lower()
        if char_lower in encryption_alphabet:
            index = encryption_alphabet.index(char_lower)
            decrypted_char = standard_alphabet[index]
            decrypted_message_list.append(decrypted_char.upper() if char.isupper() else decrypted_char)
        else:
            decrypted_message_list.append(char)

    decrypted_message = ''.join(decrypted_message_list)

    print(f"Decrypted message: {decrypted_message}")

    # Delete the encryption.txt file
    os.remove("encryption.txt")

    return decrypted_message

# test comm standalone decrypt
#print(main_decryption())
