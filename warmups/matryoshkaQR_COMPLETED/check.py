import struct

def check_png(file_path):
    with open(file_path, 'rb') as f:
        signature = f.read(8)
        if signature != b'\x89PNG\r\n\x1a\n':
            print("Not a valid PNG file.")
            return

        while True:
            chunk_header = f.read(8)
            if len(chunk_header) < 8:
                break
            
            length, type_ = struct.unpack('>I4s', chunk_header)
            print(f"Chunk Type: {type_.decode()}, Length: {length}")

            # Read the chunk data and CRC
            data = f.read(length)
            crc = f.read(4)

            # Check for IEND to stop processing
            if type_ == b'IEND':
                break

check_png('qrcode.png')
