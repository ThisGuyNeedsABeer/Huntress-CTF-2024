import sqlite3
import zlib
import pandas as pd

# Path to the Fossil SCM database file
db_path = 'ancient.fossil'  # Update this path to the correct location

# Reconnect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch the 'content' column from the 'blob' table
hex_data_query = "SELECT content FROM blob"
cursor.execute(hex_data_query)

# Fetch all rows of hex-encoded data (in 'blob' format)
hex_data_rows = cursor.fetchall()

# Process each hex-encoded row, starting the decompression from index 4 in the binary data
flag_data_list = []
for row in hex_data_rows:
    blob_data = row[0]  # Assuming the 'content' data is in the first column
    
    if blob_data:
        try:
            # Skip the first 4 bytes of the binary data
            binary_data = blob_data[4:]
            
            # Decompress using zlib
            decompressed_data = zlib.decompress(binary_data)

            # Check if the decompressed data contains the flag
            if b'flag{' in decompressed_data:
                flag_data_list.append(decompressed_data.decode('utf-8'))  # Decode from bytes to string
        except (zlib.error, ValueError) as e:
            flag_data_list.append(f"Error processing data: {e}")

# Display the decompressed flag data
if flag_data_list:
    for i, data in enumerate(flag_data_list):
        print(f"Flag {i+1}: {data}")
else:
    print("No flag data found")

# Close the connection
conn.close()