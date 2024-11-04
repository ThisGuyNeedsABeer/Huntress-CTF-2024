import game_state_pb2  # Import the generated protobuf classes
import sys

# Load the binary .pb file
def decode_protobuf_file(file_path):
    # Create a Grid object from the generated game_state_pb2 class
    grid = game_state_pb2.Grid()
    
    # Open the file in binary mode and read its contents
    with open(file_path, "rb") as f:
        try:
            grid.ParseFromString(f.read())  # Parse the contents into the Grid object
        except Exception as e:
            print(f"Failed to parse file: {e}")
            sys.exit(1)
    
    return grid

# Display the contents of the grid
def display_grid(grid):
    print(f"Width: {grid.width}")
    print(f"Height: {grid.height}")
    print("Grid rows and cells:")
    
    for row_idx, row in enumerate(grid.rows):
        for cell_idx, cell in enumerate(row.cells):
            print(f"Row {row_idx}, Cell {cell_idx} - Alive: {cell.alive}, Color: {cell.color}")

if __name__ == "__main__":
    # Path to your .pb file
    pb_file = "game_state.pb"

    # Decode the file
    decoded_grid = decode_protobuf_file(pb_file)
    
    # Display the decoded grid
    display_grid(decoded_grid)