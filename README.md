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

├── Bíblia_Sagrada(port-br).txt # Arquivo de entrada
├── huffman_compress.py # Script de compressão
├── huffman_decompress.py # Script de descompressão
├── Bíblia_Sagrada(port-br)_compressed.bin # Arquivo comprimido gerado
├── Bíblia_Sagrada(port-br)_codes.pkl # Tabela de códigos para descompressão

## Scripts

### 1. Huffman Compress

**Arquivo:** `huffman_compress.py`  

**O que faz**:
- Lê o arquivo TXT.
- Aplica pré-processamento:
  - Remove caracteres especiais
  - Converte todas as letras para maiúsculas
  - Limita a 30 letras e 10 números
  - Substitui `;` por `.`
- Gera a árvore de Huffman e os códigos binários.
- Cria o arquivo binário comprimido: Bíblia_Sagrada(port-br)_compressed.bin
- - Salva a tabela de códigos para descompressão: Bíblia_Sagrada(port-br)_codes.pkl

**Como executar**:

```bash
python3 huffman_compress.py

