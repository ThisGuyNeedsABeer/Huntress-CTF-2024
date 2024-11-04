import base64

def decode_until_flag(input_file):
    with open(input_file, 'r') as f:
        encoded_data = f.read().strip()

    while True:
        try:
            # Decode the base64 encoded data
            decoded_data = base64.b64decode(encoded_data).decode('utf-8', errors='ignore')
            print(decoded_data)  # Print the decoded output
            
            # Check for the word "flag" in the decoded data
            if "flag" in decoded_data:
                print("Found flag:", decoded_data)
                break

            # Prepare for the next iteration with the new decoded data
            encoded_data = decoded_data.strip()

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    input_file = 'base64by32'  # Challenge Filename
    decode_until_flag(input_file)
