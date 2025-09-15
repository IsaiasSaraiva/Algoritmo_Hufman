import pickle
import os

"""
Descompressão de arquivo Huffman
Usa o arquivo _codes.pkl gerado na compressão para decodificar
"""

class HuffmanDecoding:
    def __init__(self, compressed_path, codes_path):
        self.compressed_path = compressed_path
        with open(codes_path, 'rb') as f:
            self.reverse_mapping = pickle.load(f)

    def remove_padding(self, padded_text):
        padded_info = padded_text[:8]
        extra_padding = int(padded_info, 2)
        padded_text = padded_text[8:]
        return padded_text[:-extra_padding]

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""
        return decoded_text

    def decompress(self):
        filename, _ = os.path.splitext(self.compressed_path)
        output_path = filename + "_decompressed.txt"

        bit_string = ""
        with open(self.compressed_path, 'rb') as f:
            byte = f.read(1)
            while len(byte) > 0:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = f.read(1)

        encoded_text = self.remove_padding(bit_string)
        decoded_text = self.decode_text(encoded_text)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(decoded_text)

        print("Descompressão concluída:", output_path)
        return output_path

# ---------------- Execução ---------------- #
if __name__ == "__main__":
    compressed_file = "Bíblia_Sagrada(port-br)_compressed.bin"
    codes_file = "Bíblia_Sagrada(port-br)_codes.pkl"
    h = HuffmanDecoding(compressed_file, codes_file)
    h.decompress()
