import sys


# Function for Caesar Cipher
def caesar_cipher(message, key):

    output = ""

    # Go through each character in the message
    for ch in message:

        # Handle uppercase letters
        if 'A' <= ch <= 'Z':
            output += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))

        # Handle lowercase letters
        elif 'a' <= ch <= 'z':
            output += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))

        # Keep other characters unchanged
        else:
            output += ch

    return output


# Check if text and key are given through command line
if len(sys.argv) >= 3:

    message = sys.argv[1]

    try:
        key = int(sys.argv[2])

        print("Original Message:", message)
        print("Shift Key:", key)

        # Encrypt the message
        encrypted_message = caesar_cipher(message, key)

        # Decrypt the message
        decrypted_message = caesar_cipher(message, -key)

        print("Encrypted Message:", encrypted_message)
        print("Decrypted Message:", decrypted_message)

    except ValueError:
        print("Invalid key! Please enter a number.")


# Otherwise, take input from the user
else:

    message = input("Enter the message: ")

    # Validate the shift key
    while True:
        key_text = input("Enter the shift key: ")

        if key_text.lstrip('-').isdigit():
            key = int(key_text)
            break
        else:
            print("Please enter a valid integer.")

    # Ask the user for the operation
    operation = input(
        "Enter 1 for Encryption or 2 for Decryption: "
    )

    if operation == "1":

        # Encrypt using positive key
        encrypted_message = caesar_cipher(message, key)
        print("Encrypted Message:", encrypted_message)

    elif operation == "2":

        # Decrypt using negative key
        decrypted_message = caesar_cipher(message, -key)
        print("Decrypted Message:", decrypted_message)

    else:
        print("Invalid operation!")