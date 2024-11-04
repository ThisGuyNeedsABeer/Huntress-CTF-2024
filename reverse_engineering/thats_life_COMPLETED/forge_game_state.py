import game_state_pb2

# Initialize the grid with width = 400 and height = 49 rows
grid = game_state_pb2.Grid()
grid.width = 400  # Set the width of the grid
grid.height = 49  # Set the height of the grid (number of rows)

# List of winning condition cells (Row, Cell Index, Color, Alive=True)
winning_cells = [
    (10, 15, 31),  # X=10, Y=15, Color=31 -> Alive=True
    (20, 25, 32),  # X=20, Y=25, Color=32 -> Alive=True
    (30, 35, 33),  # X=30, Y=35, Color=33 -> Alive=True
    (40, 45, 34),  # X=40, Y=45, Color=34 -> Alive=True
    (25, 50, 35),  # X=25, Y=50, Color=35 -> Alive=True
    (5, 55, 36),   # X=5,  Y=55, Color=36 -> Alive=True
    (15, 60, 37),  # X=15, Y=60, Color=37 -> Alive=True
    (35, 65, 31),  # X=35, Y=65, Color=31 -> Alive=True
    (45, 70, 32),  # X=45, Y=70, Color=32 -> Alive=True
    (0, 75, 33),   # X=0,  Y=75, Color=33 -> Alive=True
    (1, 80, 34),   # X=1,  Y=80, Color=34 -> Alive=True
    (2, 85, 35),   # X=2,  Y=85, Color=35 -> Alive=True
]

# Create a dictionary for quick lookup of winning cells
winning_cells_dict = {(x, y): color for x, y, color in winning_cells}

# Populate the grid with 49 rows, and each row has 400 cells
for y in range(grid.height):
    row = grid.rows.add()  # Add a new row to the grid
    for x in range(grid.width):
        cell = row.cells.add()  # Add a new cell to the row
        
        # Check if the current cell matches a winning condition cell
        if (y, x) in winning_cells_dict:
            cell.alive = True   # Cell is alive if it has a color
            cell.color = winning_cells_dict[(y, x)]  # Set color from the winning condition
        else:
            cell.alive = False  # Default for non-winning cells
            cell.color = 0      # Default color for non-winning cells

# Serialize the grid to a file (game_state.pb)
with open('game_state.pb', 'wb') as f:
    f.write(grid.SerializeToString())

print("Game state protobuf generated successfully!")