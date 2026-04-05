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
        freq_table = VigenereHacker._get_frequency_table(language)
        n = len(column_text)
        
        counts = [0] * 26
        for char in column_text:
            counts[ord(char) - ord('A')] += 1
        
        best_char = 'A'
        min_error = float('inf')
        
        # Testando os 26 deslocamentos possíveis (0 = A, 1 = B) em cada local da chave
        for shift in range(26):
            current_error = 0.0
            
            for p in range(26):
                c = (p + shift) % 26
                
                # Qual porcentagem apareceu no texto cifrado?
                observed_porcentage = (counts[c] / n) * 100               
                
                # Qual porcentagem deveria ter no idioma original?
                original_char = chr(p + ord('A'))                   
                expected_pct = freq_table[original_char]
                
                current_error += abs(observed_porcentage - expected_pct)
                
            if current_error < min_error:
                min_error = current_error
                best_char = chr(shift + ord('A'))
                 
        return best_char, min_error
    
    @staticmethod
    def _calculate_ic(text: str) -> float:
        """
        Calcula o Índice de Coicidência (IC) de uma string.
        O IC mede a probabilidade de duas letras sorteadas aleatoriamente serem iguais 
        """
        
        n = len(text)
        if n <= 1:
            return 0.0
        
        freqs = [0] * 26
        for char in text:
            freqs[ord(char) - ord('A')] += 1
        
        # Essa é basicamente a fórmula do IC: Somatório de f * (f - 1) / (n * (n - 1))
        sum_frequence = sum(f * (f - 1) for f in freqs)
        ic = sum_frequence / (n * (n - 1))
        
        return ic
    
    @staticmethod
    def _guess_key_length(cyphertext: str, max_length: int = 20) -> int:
        """
        Tenta adivinhar o tamanho da chave testando de 1 até max_length.
        O tamanho correto agrupa letras que sofreram o mesmo deslocamento,
        fazendo o IC saltar de ~0.038 (aleatório) para ~0.07 (idioma real).
        """
        
        safe_limit = min(max_length, len(cyphertext) // 20)
        safe_limit = max(safe_limit, 3)
        
        best_length = 1
        greater_average_ic = 0.0
        
        lenght_candidates = set([1])
        
        for k_len in range(1, safe_limit + 1):
            sum_ic_column = 0.0
            
            for i in range(k_len):
                column = cyphertext[i::k_len]
                sum_ic_column += VigenereHacker._calculate_ic(column)
            
            average_ic = sum_ic_column / k_len
            
            if average_ic > greater_average_ic:     
                greater_average_ic = average_ic
                best_length = k_len
                lenght_candidates.add(best_length)
                    
        return best_length, list(lenght_candidates)
        
    @staticmethod
    def hack(cyphertext: str, language: str = 'PT') -> dict:
        """
        Método principal do ataque.
        Retorna um dicionário com a chave encontrada e o texto decifrado.
        """
        text_only = "".join(char for char in cyphertext.upper() if char.isalpha())
        
        lenght_key, _ = VigenereHacker._guess_key_length(text_only)
        discovery_key = ""
        
        # Dividir a senha em várias Cifras de César (dividir pra conquistar)
        for i in range(lenght_key):
            column = text_only[i::lenght_key]
            
            key_char, _ = VigenereHacker._break_single_column(column, language)
            discovery_key += key_char 
            
        # Agora que temos a key, só decifrar novamente a mensagem cifrada
        decrypted_message = VigenereCipher.decrypt(cyphertext, discovery_key)
        
        return {
            "key": discovery_key,
            "text": decrypted_message,
            "length": lenght_key
        }
        
