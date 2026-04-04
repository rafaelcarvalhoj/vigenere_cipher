# Cifra de Vigenere

Este projeto implementa a cifra de Vigenere em Python, com foco nas operações de cifrar e decifrar mensagens usando uma chave textual.

A ideia central da implementação é tratar cada letra como um número de `0` a `25` e aplicar operações de módulo `26`, fazendo o alfabeto "girar" durante o processo de cifragem e decifragem.

Caracteres que não são letras, como espaços, números e pontuação, são preservados no resultado para manter o texto legível.

## Objetivo

Este trabalho explora a cifra de Vigenere em duas frentes:

1. Cifrador e decifrador de mensagens.
2. Base para futuros experimentos com recuperação de chave por análise de frequência.

## Como funciona

Na cifragem, cada letra da mensagem é deslocada de acordo com a letra correspondente da chave.

Na decifragem, o processo inverso é aplicado, subtraindo o deslocamento definido pela chave para recuperar o texto original.

O projeto normaliza os textos antes do processamento:

- Converte tudo para letras maiúsculas.
- Remove acentos e sinais diacríticos.
- Mantém caracteres não alfabéticos no texto final.

Exemplos de normalização:

- `ç` vira `C`
- `ã` vira `A`
- `é` vira `E`

## Como executar

Para rodar o programa no terminal:

```bash
python3 main.py
```

## Observações

- A implementação considera o alfabeto latino básico de 26 letras.
- Letras acentuadas são normalizadas para sua forma ASCII equivalente antes da cifragem.
- O projeto foi organizado de forma simples para facilitar estudo, testes e evolução futura.
