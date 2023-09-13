import random

alphabet = list("abcdefghijklmnopqrstuvwxyz0123456789")

def generate_pi_digits(n):
    pi = "31415926535897932384626433832795"
    return pi[:n]

def create_encryption_alphabet(pi_digits):

    pi_list = list(map(int, pi_digits))
    random.seed(pi_list[0])
    for i in range(1, len(pi_list)):
        random.seed(pi_list[i])
        random.shuffle(alphabet)
    return ''.join(alphabet)

def main_encryption(message):

    pi_digits = generate_pi_digits(50)

    encryption_alphabet = create_encryption_alphabet(pi_digits)

    standard_alphabet_dict = {key_char: index for index, key_char in enumerate(alphabet)}

    encrypted_message_list = []
    for char in message:
        char_lower = char.lower()
        if char_lower in standard_alphabet_dict:
            index = standard_alphabet_dict[char_lower]
            encrypted_char = encryption_alphabet[index]
            encrypted_message_list.append(encrypted_char.upper() if char.isupper() else encrypted_char)
        else:
            encrypted_message_list.append(char)

    encrypted_message = ''.join(encrypted_message_list)

    # Save both the encryption alphabet and the encrypted message to a file named encryption.txt
    with open("encryption.txt", "w") as f:
        f.write(encryption_alphabet + "\n---\n" + encrypted_message)

    print(f"Encrypted message: {encrypted_message}")
    return encrypted_message

# test comm standalone encrypt
#message = input("Enter the message to encrypt: ")
#main_encryption(message)