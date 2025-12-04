from fetcher.fetcher import day_input

class Grid:
    def __init__(self):
        self.internal_grid = []
        self.max_rolls = 4
        self.pickup_list = []

    def add_row(self, row: str):
        grid_row = []

        for character in row:
            if character == ".":
                grid_row.append(0)
            elif character == "@":
                grid_row.append(1)
        
        self.internal_grid.append(grid_row)
    
    def get_pos(self, x: int, y: int):
        return self.internal_grid[y][x]
    
    def set_pos(self, x: int, y: int, occupied: bool):
        self.internal_grid[y][x] = 1 if occupied else 0
    
    def scan(self, x, y):
        if self.get_pos(x,y) == 0:
            return False
        
        num_of_rolls = 0
        num_of_rolls += self.top_spots(x, y)
        num_of_rolls += self.adjacent_spots(x, y)
        num_of_rolls += self.bottom_spots(x, y)

        if num_of_rolls < self.max_rolls:
            self.pickup_list_append(x, y)
            return True
        return False

    def picked_up(self):
        pickup_status = False
        for x, y in self.pickup_list:
            self.set_pos(x, y, False)
            pickup_status = True
        
        self.pickup_list = []
        return pickup_status

    def top_spots(self, x, y):
        if y == 0:
            return 0
        
        return self.total_x_spots(x, y - 1)
        
    def adjacent_spots(self, x, y):
        return self.total_x_spots(x, y) - 1
    
    def bottom_spots(self, x, y):
        if y == (len(self.internal_grid) - 1):
            return 0

        return self.total_x_spots(x, y + 1)

    def total_x_spots(self, x, y):
        look_spots = []
        if x == 0:
            look_spots += [x, x + 1]
        elif x == (len(self.internal_grid[y]) - 1):
            look_spots += [x - 1, x]
        else:
            look_spots += [x - 1, x, x + 1]
        
        total = 0

        for x_spot in look_spots:
            total += self.get_pos(x_spot, y)

        return total
    
    def get_total_rows(self):
        return len(self.internal_grid)
    
    def get_total_cols(self, at_row: int):
        return len(self.internal_grid[at_row])
    
    def pickup_list_append(self, x, y):
        self.pickup_list.append((x, y))


def main():
    grid = Grid()
    counter = 0
    pickup_status = True

    # populate grid
    for line in day_input.split("\n"):
        grid.add_row(line)

    while pickup_status:
        for y in range(0, grid.get_total_rows()):
            for x in range(0, grid.get_total_cols(y)):
                result = grid.scan(x,y)
                counter += 1 if result else 0
        
        pickup_status = grid.picked_up()

    print(counter, "toilet rolls that can be picked up.")

main()