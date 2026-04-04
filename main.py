from vigenere_cipher import VigenereCipher


def show_menu() -> None:
    print("\n=== Vigenere Cipher ===")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Exit")


def read_key() -> str:
    while True:
        key = input("Enter the key: ").strip()
        if key:
            return key

        print("The key cannot be empty.")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            key = read_key()
            encrypted_text = VigenereCipher.encrypt(text, key)
            print(f"Encrypted text: {encrypted_text}")
        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            key = read_key()
            decrypted_text = VigenereCipher.decrypt(text, key)
            print(f"Decrypted text: {decrypted_text}")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
