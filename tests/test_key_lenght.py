import pytest

from vigenere_hacker import VigenereHacker
from vigenere_cipher import VigenereCipher


@pytest.mark.parametrize(
    "plaintext,key",
    [
        #("HELLO WORLD", "ABC", 3),
        #("HELLO WORLD, THIS IS A TEST", "XYZA", 4),
        #("BOM DIA", "CHAVE", 5),
        #("SECURITY TEST 123!", "BANANA", 6),
        #("HELLO WORLD", "A", 1)
        ("THIS IS A LONGER PLAINTEXT TO TEST THE KEY LENGTH GUESSING FUNCTION", "KEY"),
        ("ANOTHER EXAMPLE WITH DIFFERENT KEY LENGTHestudar e anotar possiveis referencias na planilha disponibilizada emS", "LONGKEYLONGKEYLONG"),
        ("Under this scenario, Dave would beat Kristen (S>P), Richard would beat Michael (R>S), and then Dave and Richard would play (Richard wins since R>S); similarly, Allen would beat Omer, Richard X would beat David E., and Allen and Richard X. would play (Allen wins since S>P); and finally Richard would beat Allen since R>S, that is, continue until there is only a single winner.", "VERYLONGKEY")
    ],
)
def test_get_key_lenght_specific_cases(plaintext, key):
    clear_plaintext = "".join(char for char in VigenereCipher._normalize(plaintext) if char.isalpha())
    cyphertext = VigenereCipher.encrypt(clear_plaintext, key)
    best, candidates = VigenereHacker._guess_key_length(cyphertext)
    assert len(key) in candidates
