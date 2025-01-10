# Mohammad Abu Shams 1200549.
# Joud Hijaz 1200342.

# Import necessary libraries.
import collections
import math
import heapq
from tabulate import tabulate
import docx2txt

# Define a class to represent a node in the Huffman tree.
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Function to calculate the frequency of each character in the text.
def calculate_frequencies(text):
    text = text.replace("\n", "").lower()
    freq = collections.Counter(text)
    return freq


# Function to calculate the probability of each character in the text.
def calculate_probabilities(freq, total_chars):
    probabilities = {char: count / total_chars for char, count in freq.items()}
    return probabilities


# Function to calculate the entropy of the text.
def calculate_entropy(probabilities):
    entropy = -sum(p * math.log2(p) for p in probabilities.values() if p > 0)
    return entropy


# Function to build the Huffman tree.
def build_huffman_tree(freq):
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the tree


# Function to generate the Huffman codes.
def generate_huffman_codes(root, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if root:
        if root.char is not None:  # Leaf node
            codebook[root.char] = prefix
        generate_huffman_codes(root.left, prefix + "0", codebook)
        generate_huffman_codes(root.right, prefix + "1", codebook)

    return codebook


# Function to calculate the length of the Huffman encoding.
def calculate_huffman_encoding_length(freq, codebook):
    return sum(len(codebook[char]) * freq[char] for char in freq)


# Function to calculate the compression percentage.
def calculate_compression_percentage(n_ascii, n_huffman):
    return (1 - (n_huffman / n_ascii)) * 100


# Function to read the .docx file.
def readText():
    text = docx2txt.process("To+Build+A+Fire+by+Jack+London.docx")
    return text


# MAIN.
if __name__ == "__main__":
    # Read the text file.
    story = readText()

    # Calculate frequencies.
    freq = calculate_frequencies(story)
    total_chars = sum(freq.values())

    # Calculate probabilities.
    probabilities = calculate_probabilities(freq, total_chars)

    # Calculate entropy.
    entropy = calculate_entropy(probabilities)

    # Build Huffman tree.
    huffman_tree_root = build_huffman_tree(freq)

    # Generate Huffman codes.
    huffman_codes = generate_huffman_codes(huffman_tree_root)

    # Calculate ASCII and Huffman encoding lengths.
    n_ascii = total_chars * 8  # ASCII uses 8 bits per character
    n_huffman = calculate_huffman_encoding_length(freq, huffman_codes)

    # Calculate average bits per character and compression.
    avg_bits_per_char = n_huffman / total_chars
    compression_percentage = calculate_compression_percentage(n_ascii, n_huffman)

    # Print summary results.
    print("\n**************************** Final Result **********************************")
    print(f"\nTotal characters: {total_chars}")
    print(f"Entropy of the alphabet: {entropy:.4f} bits/character")
    print(f"ASCII encoding length (NASCII): {n_ascii} bits")
    print(f"Average bits per character with Huffman: {avg_bits_per_char:.4f} bits/character")
    print(f"Compression ratio (Entropy to Huffman bits): {(entropy / avg_bits_per_char)*100:.4f}%")
    print(f"Huffman encoding length (Nhuffman): {n_huffman} bits")
    print(f"Compression Percentage: {compression_percentage:.4f}%")


 # Display selected symbols in a detailed table.
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'z', ' ', '.']
    symbol_table = [
        [symbol if symbol != " " else "space",f"{freq.get(symbol, 0)}" ,f"{probabilities.get(symbol, 0):.6f}", huffman_codes.get(symbol, ""), len(huffman_codes.get(symbol, ""))]
        for symbol in symbols
    ]
    print("\nDetailed Huffman Codes for Selected Symbols:")
    print(tabulate(symbol_table, headers=["Character", "Frequency","Probability", "Huffman Code", "Code Length"], tablefmt="pretty"))
