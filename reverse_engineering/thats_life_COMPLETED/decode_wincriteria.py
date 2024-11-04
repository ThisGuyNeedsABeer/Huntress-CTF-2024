import struct

# Hex data string provided by the user
hex_data = (
    "0a00000000000000"
    "0f00000000000000"
    "1f00000000000000"
    "0000000000000000"
    "1400000000000000"
    "1900000000000000"
    "2000000000000000"
    "0000000000000000"
    "1e00000000000000"
    "2300000000000000"
    "2100000000000000"
    "0000000000000000"
    "2800000000000000"
    "2d00000000000000"
    "2200000000000000"
    "0000000000000000"
    "1900000000000000"
    "3200000000000000"
    "2300000000000000"
    "0000000000000000"
    "0500000000000000"
    "3700000000000000"
    "2400000000000000"
    "0000000000000000"
    "0f00000000000000"
    "3c00000000000000"
    "2500000000000000"
    "0000000000000000"
    "2300000000000000"
    "4100000000000000"
    "1f00000000000000"
    "0000000000000000"
    "2d00000000000000"
    "4600000000000000"
    "2000000000000000"
    "0000000000000000"
    "0000000000000000"
    "4b00000000000000"
    "2100000000000000"
    "0000000000000000"
    "0100000000000000"
    "5000000000000000"
    "2200000000000000"
    "0000000000000000"
    "0200000000000000"
    "5500000000000000"
    "2300000000000000"
    "0000000000000000"
)

# Convert hex string to bytes
byte_data = bytes.fromhex(hex_data)

# Define the structure format: 3 longlongs ('Q' for unsigned longlong) and 1 bool ('?')
fmt = 'QQQ?' + 'x' * (32 - 25)  # Padding for 32 bytes in total

# Calculate the number of 32-byte entries we have in the data
entry_size = 32
num_entries = len(byte_data) // entry_size

# Process each entry
for i in range(num_entries):
    entry = byte_data[i * entry_size:(i + 1) * entry_size]
    unpacked_data = struct.unpack(fmt, entry)
    
    x, y, color, alive = unpacked_data
    print(f"Entry {i+1}:")
    print(f"  X: {x}")
    print(f"  Y: {y}")
    print(f"  Color: {color}")
    print(f"  Alive: {alive}")
    print()