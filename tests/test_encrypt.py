from vigenere_cipher import VigenereCipher


def test_encrypt_known_english_vector():
    assert VigenereCipher.encrypt("HELLO", "KEY") == "RIJVS"


def test_encrypt_preserves_spaces_and_punctuation():
    assert VigenereCipher.encrypt("HELLO, WORLD!", "KEY") == "RIJVS, UYVJN!"


def test_encrypt_identity_with_a_key():
    assert VigenereCipher.encrypt("HELLO", "A") == "HELLO"


def test_encrypt_empty_text_returns_empty():
    assert VigenereCipher.encrypt("", "KEY") == ""


def test_encrypt_portuguese_ascii_case():
    assert VigenereCipher.encrypt("BOM DIA", "CHAVE") == "DVM YMC"


def test_encrypt_normalizes_to_uppercase():
    assert VigenereCipher.encrypt("hello", "key") == "RIJVS"


def test_encrypt_removes_accents_during_normalization():
    assert VigenereCipher.encrypt("maçã", "chave") == "OHCV"
