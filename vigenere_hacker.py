from vigenere_cipher import VigenereCipher

class VigenereHacker:
    
    # Constantes de frequência (em porcentagem) para cada idioma
    
    FREQ_EN = {
        'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
        'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772,  'L': 4.025,
        'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095,  'R': 5.987,
        'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360,  'X': 0.150,
        'Y': 1.974, 'Z': 0.074
    }

    FREQ_PT = {
        'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57, 'F': 1.02,
        'G': 1.30,  'H': 1.28, 'I': 6.18, 'J': 0.40, 'K': 0.02,  'L': 2.78,
        'M': 4.74,  'N': 5.05, 'O': 10.73,'P': 2.52, 'Q': 1.20,  'R': 6.53,
        'S': 7.81,  'T': 4.34, 'U': 4.63, 'V': 1.67, 'W': 0.01,  'X': 0.21,
        'Y': 0.01,  'Z': 0.47
    }
    
    @staticmethod
    def _get_frequency_table(language: str) -> dict:
        if language.upper() == "EN":
            return VigenereHacker.FREQ_EN
        return VigenereHacker.FREQ_PT
    
    @staticmethod
    def _break_single_column(column_text: str, language: str) -> tuple[str, float]:
        """
        Testa as 26 letras para uma única coluna e retorna a letra da chave 
        que gerou a menor diferença estatística, junto com a pontuação (score).
        """
        pass
    
    @staticmethod
    def _guess_key_length(cyphertext: str) -> int:
        """
        Implementa o Kasiski ou tenta adivinhar o tamanho da chave por força bruta (1 a 20) / ou outro método.
        """
        pass
        
    @staticmethod
    def hack(cyphertext: str, language: str = 'PT') -> dict:
        """
        Método principal do ataque.
        Retorna um dicionário com a chave encontrada e o texto decifrado.
        """
        # 1. Limpar o texto (usando o _normalize)
        # 2. Descobrir o tamanho da chave (_guess_key_length)
        # 3. Fatiar o texto em colunas (como se fosse várias cifras de cesár)
        # 4. Chamar _break_single_column para cada coluna
        # 5. Juntar as letras para formar a chave final
        # 6. Usar VigenereCypher.decrypt para gerar o texto final=
        pass