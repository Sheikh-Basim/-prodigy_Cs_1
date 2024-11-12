def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # ASCII base for uppercase or lowercase
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabet characters are added unchanged
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decrypt by shifting in the opposite direction

# Main program to interact with the user
if __name__ == "__main__":
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))

    if choice == "encrypt":
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == "decrypt":
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")

