import sqlite3
import zlib
import pandas as pd

db_path = 'ancient.fossil'  # Update this path to the correct location
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
hex_data_query = "SELECT content FROM blob"
cursor.execute(hex_data_query)
hex_data_rows = cursor.fetchall()

# Process each hex-encoded row, starting the decompression from index 4 in the binary data
decompressed_data_list = []
for row in hex_data_rows:
    blob_data = row[0]  # Assuming the 'content' data is in the first column
    
    if blob_data:
        try:
            binary_data = blob_data[4:]
            decompressed_data = zlib.decompress(binary_data)
            decompressed_data_list.append(decompressed_data.decode('utf-8'))  # Decode from bytes to string
        except (zlib.error, ValueError) as e:
            decompressed_data_list.append(f"Error processing data: {e}")

for i, data in enumerate(decompressed_data_list):
    print(f"Decompressed Data {i+1}: {data}")

conn.close()