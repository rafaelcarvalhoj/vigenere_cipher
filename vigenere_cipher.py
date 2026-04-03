# Este trabalho explora a cifra de Vigenère, tendo duas partes: o cifrado/decifrador e o ataque de
# recuperação de senha por análise de frequência

# A lógica central visa tratar as letras como números de 0 a 25, e usar operações de módulo (%26)
# para garantir que o alfabeto "rode"
# Se não for uma letra, simplesmente mantenha os espaços e caracteres especiais dentro do resultado pra frase ficar com a frase legível

# OBS: Nessa primeira versão só trabalhei com o alfabeto clássico de 26 letras, não considerei os acentos ou "Ç", então caso use, vai quebrar o código basicamente
# (Não sei se precisa uma versão pra cobrir os 256 caracteres da tabela ASCII)

class VigenereCipher:
    
    @staticmethod
    def encrypt(text: str, key: str) -> str:
        result = []
        key = key.upper()
        key_index = 0
        
        for char in text.upper():
            if char.isalpha():
                # Transforma letra em 0-25, soma o deslocamento da chave e volta para letra
                p = ord(char) - ord('A')
                k = ord(key[key_index % len(key)]) - ord('A')
                c = (p + k) % 26
                result.append(chr(c + ord('A')))
                
                key_index += 1
            else:
                result.append(char)
            
        return "".join(result)    
    

    @staticmethod
    def decrypt(cyphertext: str, key: str) -> str:
        result = []
        key = key.upper()
        key_index = 0 
        
        for char in cyphertext.upper():
            if char.isalpha():
                # Faz o caminho inverso: subtrai o deslocamento da chave
                c = ord(char) - ord('A')
                k = ord(key[key_index %len(key)]) - ord('A')
                p = (c - k + 26) % 26
                result.append(chr(p + ord('A')))
                
                key_index += 1
            else:
                result.append(char)

        return "".join(result)

# Área para teste
msg = "Finja que isso e uma mensagem gigante, tipo de verdade mesmo, coisa de 1000 linhas mais ou menos, e depois veja a magia acontecer..."
chave = "BANANA"

cifrado = VigenereCipher.encrypt(msg, chave)
decifrado = VigenereCipher.decrypt(cifrado, chave)

print(f"Cifrado: {cifrado}")
print(f"Decifrado: {decifrado}")