# Huffman Coding Project

## Introduction
This project demonstrates the use of Huffman coding, an efficient data compression technique, to analyze and compress the text of the English short story *To Build A Fire by Jack London*. The implementation calculates character frequencies, probabilities, entropy, and Huffman codes while comparing the results with fixed-length ASCII encoding.

## Features
- Calculates character frequencies and probabilities from the given text.
- Computes the entropy of the dataset, representing the theoretical compression limit.
- Implements Huffman coding to generate prefix-free binary codes for the characters.
- Compares the efficiency of Huffman coding with ASCII encoding.
- Provides compression statistics, including compression percentage and average bits per character.

## Results
- **Total characters**: 37705
- **Entropy of the Alphabet**: 4.172 bits per character
- **Average Bits per Character (Huffman)**: 4.2185 bits per character
- **Compression Ratio (Entropy to Huffman)**: 98.8980%
- **Huffman Encoding Length (Nhuffman)**: 159060 bits
- **Compression Percentage**: 47.2683%

### Detailed Huffman Codes for Selected Symbols
| Character | Frequency | Probability | Huffman Code | Code Length |
|-----------|-----------|-------------|--------------|-------------|
| a         | 2264      | 0.060045    | 1001         | 4           |
| b         | 484       | 0.012836    | 100000       | 6           |
| c         | 779       | 0.020660    | 110110       | 6           |
| d         | 1515      | 0.040180    | 11010        | 5           |
| e         | 3887      | 0.103090    | 010          | 3           |
| f         | 794       | 0.021058    | 00000        | 5           |
| m         | 678       | 0.017982    | 101101       | 6           |
| z         | 61        | 0.001618    | 000111101    | 9           |
| space     | 7048      | 0.186925    | 111          | 3           |
| .         | 414       | 0.010980    | 000100       | 6           |

## File Structure
- `project.py`: The main Python script implementing the Huffman coding process.
- `To Build A Fire by Jack London.docx`: The input text file used for analysis and compression.
- `README.md`: Documentation for the project.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/huffman-coding-project.git
   cd huffman-coding-project

## Contributors

- [Mohammad AbuShams](https://github.com/MohammadAbuShams)
- [Joud Hijaz](https://github.com/JoudHijaz)
