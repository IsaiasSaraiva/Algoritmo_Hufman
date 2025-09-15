import heapq
import os
import re
import pickle

"""
Compressão de texto usando Huffman
Pré-processamento:
1. Remove caracteres especiais
2. Converte para maiúsculas
3. Limita a 30 letras e 10 números
4. Substitui ';' por '.'
"""

class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    # ---------- Pré-processamento ----------
    def preprocess_text(self, text):
        text = text.replace(';', '.')
        text = re.sub(r'[^A-Za-z0-9.]', '', text)
        text = text.upper()
        letters = ''.join(re.findall(r'[A-Z]', text))[:30]
        numbers = ''.join(re.findall(r'[0-9]', text))[:10]
        return letters + numbers

    # ---------- Construção da árvore ----------
    def make_frequency_dict(self, text):
        freq = {}
        for c in text:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        return freq

    def make_heap(self, freq):
        for char in freq:
            heapq.heappush(self.heap, self.HeapNode(char, freq[char]))

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if root is None: return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        self.make_codes_helper(root, "")

    # ---------- Codificação ----------
    def get_encoded_text(self, text):
        return ''.join(self.codes[c] for c in text)

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"
        padded_info = "{0:08b}".format(extra_padding)
        return padded_info + encoded_text

    def get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            print("Erro: texto codificado não está devidamente preenchido")
            exit(0)
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b

    # ---------- Compressão ----------
    def compress(self):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + "_compressed.bin"

        with open(self.path, 'r', encoding='latin-1') as file:
            text = file.read().rstrip()
            text = self.preprocess_text(text)
            print("Texto processado:", text)

            freq = self.make_frequency_dict(text)
            self.make_heap(freq)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)
            b = self.get_byte_array(padded_encoded_text)

            with open(output_path, 'wb') as output_file:
                output_file.write(bytes(b))

            # Salvar códigos para descompressão
            with open(filename + "_codes.pkl", 'wb') as code_file:
                pickle.dump(self.reverse_mapping, code_file)

        print("Compressão concluída:", output_path)
        return output_path

# ---------------- Execução ---------------- #
if __name__ == "__main__":
    path = "Bíblia_Sagrada(port-br).txt"  # Arquivo a ser comprimido
    h = HuffmanCoding(path)
    h.compress()
