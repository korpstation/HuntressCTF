encoded = [
    0x342d31373a30, 0x6334, 0x306764336060636f,
    0x6e6063336363, 0x3266, 0x34343265306f6e63,
    0x30663533, 0x2b6e
]

# Convertir en bytes
encoded_bytes = b''.join(x.to_bytes((x.bit_length() + 7) // 8, 'little') for x in encoded)

# Décoder avec XOR 0x56
decoded = bytes(b ^ 0x56 for b in encoded_bytes)

print(decoded.decode('ascii'))

#flag{bb59566e21f55e5680d589f3dbbec0f8}
