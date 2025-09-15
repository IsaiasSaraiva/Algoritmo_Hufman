# Compressão e Descompressão de Texto com Huffman

## Descrição

Este repositório contém uma implementação em Python do **algoritmo de Huffman**, utilizado para **compressão e descompressão de arquivos de texto**.  

O algoritmo segue os seguintes passos solicitados pelo exercício:

1. **Pré-processamento do texto**:
   - Remoção de caracteres especiais.
   - Conversão para letras maiúsculas.
   - Limite de 30 letras e 10 números.
   - Substituição de `;` por `.`.
2. **Compressão** do texto pré-processado usando Huffman.
3. **Descompressão** do arquivo gerado, reconstruindo o texto pré-processado.

O arquivo de exemplo utilizado é `Bíblia_Sagrada(port-br).txt`.

---

## Estrutura da pasta

- Bíblia_Sagrada(port-br).txt # Arquivo de entrada
- huffman_compress.py # Script de compressão
- huffman_decompress.py # Script de descompressão
- Bíblia_Sagrada(port-br)_compressed.bin # Arquivo comprimido gerado
- Bíblia_Sagrada(port-br)_codes.pkl # Tabela de códigos para descompressão

## Scripts


**Como executar**:

```bash
python3 huffman_compress.py



```bash
python3 huffman_descompressed.py

