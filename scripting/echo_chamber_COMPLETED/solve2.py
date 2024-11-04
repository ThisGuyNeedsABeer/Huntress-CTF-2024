# Read data from chunk.txt file and strip out "4L" from each line
with open("chunk2.txt", "r") as file:
    lines = [line.replace("4L", "").strip() for line in file]

# Extract a character from every other line (starting with the first line)
selected_chars = [line[0] for i, line in enumerate(lines) if i % 2 == 0]

# Join the selected characters to form the message
flag = ''.join(selected_chars)


print("Extracted Flag:", flag)
