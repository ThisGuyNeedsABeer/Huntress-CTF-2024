import re

# Read data from chunk.txt file
with open("chunk.txt", "r") as file:
    data = file.read().strip()

# Break data into chunks of 40 characters
chunk_size = 40
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Function to get a unique character from each chunk
def get_unique_character(chunk):
    # Use a set to find unique characters in the chunk
    unique_chars = set(chunk)
    # Return the first unique character found
    return unique_chars.pop()

# Extract one unique character from each chunk
flag = ''.join(get_unique_character(chunk) for chunk in chunks)


print("Extracted Flag:", flag)
