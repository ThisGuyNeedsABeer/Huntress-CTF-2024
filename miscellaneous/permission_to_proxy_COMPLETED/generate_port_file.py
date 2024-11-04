def generate_ports_file(filename="ports.txt"):
    # Open the file for writing
    with open(filename, 'w') as file:
        # Loop through port numbers 1 to 65535
        for port in range(1, 65536):
            # Write each port number followed by a newline
            file.write(f"{port}\n")
    
    print(f"Ports 1-65535 written to {filename}")

# Call the function to generate the file
if __name__ == "__main__":
    generate_ports_file()