import zlib
import binascii

# The hex string
hex_string = "78 9c 4b cb 49 4c af 36 4a 4d 31 36 4e 33 36 33 35 33 b3 4c 4d b4 4c 33 34 48 32 4c 34 49 4d 34 01 0a a4 a5 5a 24 d7 72 01 00 f0 a2 0b 96"

# Convert the hex string to a byte array
hex_bytes = binascii.unhexlify(hex_string.replace(" ", ""))

try:
    # Perform zlib decompression (inflate)
    decompressed_data = zlib.decompress(hex_bytes)
    print("Decompressed data:", decompressed_data.decode())
except zlib.error as e:
    print("Zlib decompression failed:", e)