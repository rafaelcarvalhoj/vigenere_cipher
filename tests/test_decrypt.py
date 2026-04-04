from vigenere_cipher import VigenereCipher


def test_decrypt_known_english_vector():
    assert VigenereCipher.decrypt("RIJVS", "KEY") == "HELLO"


def test_decrypt_preserves_spaces_and_punctuation():
    assert VigenereCipher.decrypt("RIJVS, UYVJN!", "KEY") == "HELLO, WORLD!"


def test_decrypt_empty_text_returns_empty():
    assert VigenereCipher.decrypt("", "KEY") == ""


def test_decrypt_portuguese_ascii_case():
    assert VigenereCipher.decrypt("DVM YMC", "CHAVE") == "BOM DIA"


def test_decrypt_roundtrip_english():
    text = "SECURITY TEST 123!"
    key = "BANANA"
    encrypted = VigenereCipher.encrypt(text, key)

    assert VigenereCipher.decrypt(encrypted, key) == text


def test_decrypt_roundtrip_portuguese_ascii():
    text = "MENSAGEM DE TESTE"
    key = "CHAVE"
    encrypted = VigenereCipher.encrypt(text, key)

    assert VigenereCipher.decrypt(encrypted, key) == text


def test_decrypt_handles_accented_input_as_ascii():
    encrypted = VigenereCipher.encrypt("maçã", "chave")

    assert VigenereCipher.decrypt(encrypted, "chave") == "MACA"
