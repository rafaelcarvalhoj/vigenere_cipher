from vigenere_cipher import VigenereCipher
from vigenere_hacker import VigenereHacker

def test_hack_complete_portuguese():
    original_text = """
    A Criptografia de Chave Simétrica utiliza a mesma chave tanto para codificar 
    quanto para decodificar a mensagem. O método de Vigenère foi considerado 
    inquebrável por séculos, mas a análise de frequências e o índice de 
    coincidência permitem que hackers descubram a chave original.
    """
    key = "UNB"
    ciphertext = VigenereCipher.encrypt(original_text, key)
    
    result = VigenereHacker.hack(ciphertext, language='PT')
    
    assert result["key"] == "UNB"
    assert "CRIPTOGRAFIA" in result["text"].upper()

def test_hack_wrong_language():
    # Tentar quebrar um texto em Inglês usando a tabela de frequência do PT
    en_text = "The quick brown fox jumps over the lazy dog many times to test frequency."
    key = "KEY"
    ciphertext = VigenereCipher.encrypt(en_text, key)
    
    result = VigenereHacker.hack(ciphertext, language='PT')

def test_hack_language_mismatch():
    # Texto em inglês clássico
    en_text = "The Vigenere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword."
    key = "KEY"
    ciphertext = VigenereCipher.encrypt(en_text, key)
    
    # Tentando hackear forçando Português
    result = VigenereHacker.hack(ciphertext, language='PT')
    
    # Aqui o assert é interessante: ou a chave vem errada, ou o score de erro é alto
    # Isso demonstra que a 'digital' do idioma não bateu.
    assert result["key"] != "KEY"