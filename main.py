from vigenere_cipher import VigenereCipher
from vigenere_hacker import VigenereHacker

def show_menu() -> None:
    print("\n=== Vigenere Cipher ===")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Test key lenght (Debug)")
    print("4. Hack cypher")
    print("5. Exit")


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
            print(f"\nEncrypted text: {encrypted_text}")
            
            encrypted_text = "".join(char for char in encrypted_text.upper() if char.isalpha())
            
            best_len, possibles_len = VigenereHacker._guess_key_length(encrypted_text)
            
            print(f"Real key length: {len(key)}")
            print(f"Best key lenght: {best_len}")
            print(f"All best cases: {possibles_len}")
        
        elif choice == "4":
            text = input ("Enter the encrypted text to hack: ")
            lang = input ("Enter language (PT/EN) [Default: PT]: ").strip().upper()
            
            if lang not in ["PT", "EN"]:
                lang = "PT"
            
            print("\n[+] Analyzing frequency and breaking the cipher...")
            result = VigenereHacker.hack(text, lang)
            
            print("="*40)
            print(" ATAQUE CONCLUÍDO!")
            print("="*40)
            print(f"Tamanho da Chave : {result['length']}")
            print(f"Chave Encontrada : {result['key']}")
            print("-" * 40)
            print(f"Mensagem Decifrada:\n{result['text']}")
            print("="*40)
            
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
