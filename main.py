from vigenere_cipher import VigenereCipher
from vigenere_hacker import VigenereHacker

def show_menu() -> None:
    print("\n=== Vigenere Cipher ===")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Test key lenght")
    print("4. Exit")


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
            text = input("Enter the text to encrypt: ")
            key = read_key()
            encrypted_text = VigenereCipher.encrypt(text, key)
            best_len, possibles_len = VigenereHacker._guess_key_length(text)
            print(f"Best key lenght: {best_len}")
            print(f"All best cases: {possibles_len}")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
