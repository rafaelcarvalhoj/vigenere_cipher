import unicodedata

# Este trabalho explora a cifra de Vigenère, tendo duas partes: o cifrado/decifrador e o ataque de
# recuperação de senha por análise de frequência

# A lógica central visa tratar as letras como números de 0 a 25, e usar operações de módulo (%26)
# para garantir que o alfabeto "rode"
# Se não for uma letra, simplesmente mantenha os espaços e caracteres especiais dentro do resultado pra frase ficar com a frase legível

# OBS: Nessa primeira versão só trabalhei com o alfabeto clássico de 26 letras, não considerei os acentos ou "Ç", então caso use, vão ser removidos.
# (Não sei se precisa uma versão pra cobrir os 256 caracteres da tabela ASCII)

class VigenereCipher:
    
    @staticmethod
    def _normalize(text: str) -> str:
        decomposed_text = unicodedata.normalize("NFD", text)
        ascii_text = "".join(
            char for char in decomposed_text
            if unicodedata.category(char) != "Mn"
        )
        return ascii_text.upper()
    
    
    @staticmethod
    def _calc_shift_encrypt(char: str, key_char: str) -> str:
        p = ord(char) - ord('A')
        k = ord(key_char) - ord('A')
        c = (p + k) % 26
        return chr(c + ord('A'))
    
    
    @staticmethod
    def _calc_shift_decrypt(char: str, key_char: str) -> str:
        c = ord(char) - ord('A')
        k = ord(key_char) - ord('A')
        p = (c - k + 26) % 26
        return chr(p + ord('A'))
    

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        result = []
        key = VigenereCipher._normalize(key)
        key_index = 0
        
        for char in VigenereCipher._normalize(text):
            if char.isalpha():
                # Transforma letra em 0-25, soma o deslocamento da chave e volta para letra
                result.append(
                    VigenereCipher._calc_shift_encrypt(
                        char, 
                        key[key_index % len(key)]
                        )
                    )
            
                key_index += 1
            else:
                result.append(char)
            
        return "".join(result)    
    

    @staticmethod
    def decrypt(cyphertext: str, key: str) -> str:
        result = []
        key = VigenereCipher._normalize(key)
        key_index = 0 
        
        for char in VigenereCipher._normalize(cyphertext):
            if char.isalpha():
                # Faz o caminho inverso: subtrai o deslocamento da chave
                result.append(
                    VigenereCipher._calc_shift_decrypt(
                        char, 
                        key[key_index %len(key)]
                        )
                    )
                
                key_index += 1
            else:
                result.append(char)

        return "".join(result)
