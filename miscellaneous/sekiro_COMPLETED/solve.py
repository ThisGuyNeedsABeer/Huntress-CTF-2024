from pwn import *

# Constants for conneciton
HOST = "challenge.ctf.games"
PORT = 30851

# Constants for moves
MOVE_ADVANCE = b"advance"
MOVE_BLOCK = b"block"
MOVE_STRIKE = b"strike"
MOVE_RETREAT = b"retreat"

def get_opponent_move(conn):
    """Receive and return the opponent's move."""
    return conn.recvuntil(b"Your move:")

def process_opponent_move(opponent_move):
    """Determine the response based on the opponent's move."""
    if MOVE_BLOCK in opponent_move:
        return MOVE_ADVANCE
    elif MOVE_STRIKE in opponent_move:
        return MOVE_BLOCK
    elif MOVE_ADVANCE in opponent_move:
        return MOVE_RETREAT
    elif MOVE_RETREAT in opponent_move:
        return MOVE_STRIKE
    else:
        return None

def main():
    # Connect to the remote server
    conn = remote(HOST,PORT)

    # Create a continuous loop to keep the connection alive
    while True:
        try:
            print(conn.recvuntil(b"Opponent move:").decode("utf-8"))
        except Exception as e:
            print(f"Error receiving data: {e}")
            # Switch to an interactive prompt if there are errors
            conn.interactive()

        opponent_move = get_opponent_move(conn)
        print(opponent_move.decode("utf-8"))

        response_move = process_opponent_move(opponent_move)

        if response_move:
            conn.send(response_move)
            print(response_move.decode("utf-8"))
        else:
            print("Unknown opponent move, exiting.")
            exit(1)

if __name__ == "__main__":
    main()