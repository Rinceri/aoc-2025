from fetcher.fetcher import day_input

class RenderedProblem:
    def __init__(self):
        self.op = None
        self.digits = []

    def set_op(self, char: str):
        if char == "*":
            self.op = self.mult
        elif char == "+":
            self.op = self.sum_

    def mult(self):
        prod = 1

        for num in self.digits:
            prod *= num

        return prod
    
    def sum_(self):
        return sum(self.digits)
    
    def solve(self):
        """
        Clears all properties after solving based on op
        """
        solved = self.op()
        self.digits = []
        self.op = None

        return solved



class ProblemSolver:
    def __init__(self, rows: int):
        self.master = [[] for _ in range(rows)]

    def render_row(self, row: str):
        for i, cell in enumerate(row.split()):
            try:
                cell = int(cell)
            except ValueError:
                pass

            self.master[i].append(cell)

    def part_two(self, all_input: str):
        """
        This is completely separate from part 1
        """
        # turn the input into a grid
        tabled = [list(x) for x in all_input.split("\n")]
        row_size = len(tabled[0])
        curr_x = 0
        op = RenderedProblem()
        
        total = 0

        # traverse through every grid column basically
        while curr_x < row_size:
            rendered_num = ""
            # render every character in every row of this column
            for curr_y in tabled:
                if curr_y[curr_x] in ["*", "+"]:
                    op.set_op(curr_y[curr_x])
                elif curr_y[curr_x] != " ":
                    rendered_num += curr_y[curr_x]
            
            # if no character found, then this means it was all whitespaces
            if rendered_num == "":
                total += op.solve()
            else:
                # characters found, add to nums to solve
                op.digits.append(int(rendered_num))
            
            # to next column we go
            curr_x += 1

        # last problem gets left out because of while loop, solve it here
        total += op.solve()

        return total

    
    def calculate_all(self):
        total = 0
        for row in self.master:
            op = self.translate_op(row[-1])
            total += op(row[:-1])

        return total

    def translate_op(self, op: str):
        if op == "*":
            return self.mult
        elif op == "+":
            return sum

    def mult(self, all_nums: list[int]):
        prod = 1

        for num in all_nums:
            prod *= num

        return prod
    
def main():
#     day_input = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """
    ps = ProblemSolver(len(day_input.split("\n")[0].split()))
    for row in day_input.split("\n"):
        ps.render_row(row)
    
    print(f"Part one way of solving it: {ps.calculate_all()}")

    print(f"Part two way of solving it: {ps.part_two(day_input)}")

main()