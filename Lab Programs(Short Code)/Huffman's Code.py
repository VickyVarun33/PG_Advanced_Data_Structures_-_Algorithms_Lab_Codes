import heapq
from collections import defaultdict

def huffman(data):
    freq = defaultdict(int)
    for char in data: freq[char] += 1
    
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo, hi = heapq.heappop(heap), heapq.heappop(heap)
        for pair in lo[1:]: pair[1] = '0' + pair[1]
        for pair in hi[1:]: pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    encoding = heap[0][1:]
    
    compressed = ''.join([char[1] for char in encoding for _ in data if char[0] == _])
    decoded_data = ''.join([char for char in compressed] + ['0' for _ in range((8 - len(compressed) % 8) % 8)])  # Padded with zeros to handle incomplete byte
    
    reverse_encoding = {code: char for char, code in encoding}
    current_code, decoded_data = '', ''
    
    for bit in decoded_data:
        current_code += bit
        if current_code in reverse_encoding:
            decoded_data += reverse_encoding[current_code]
            current_code = ''
    
    return encoding, compressed, decoded_data

# Example Usage:
data = "hello world"
encoding, compressed_data, decoded_data = huffman(data)

print(f"Original Data: {data}")
print(f"Encoded Data: {encoding}")
print(f"Compressed Data: {compressed_data}")
print(f"Decoded Data: {decoded_data}")
