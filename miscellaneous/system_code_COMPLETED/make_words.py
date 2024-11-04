import itertools

# Characters to generate permutations
chars = 'abcdef'

# Generate all permutations of the given characters
permutations = itertools.permutations(chars)

# Open the wordlist file to write the permutations
with open('wordlist.txt', 'w') as f:
    for perm in permutations:
        # Join the tuple to form a string and write it to the file
        f.write(''.join(perm) + '\n')

print("Wordlist generated and saved to 'wordlist.txt'.")
