import random
from copy import deepcopy

class Generator:
    """
        class Generator
        Generates a sudoku field: result contains the result list, field contains the solution to the sudoku
        Init:
            Sets field size and difficulty (difficulty number shows how many numbers will be removed from the solution)
        Usage:
            generate_field() - generates a field and returns a solvable sudoku
            get_solution() - returns the sudoku's solution
    """
    def __init__(self, n=4, difficulty=50):
        self.n = n
        self.field = [[((i * n + i // n + j) % (n * n)) for j in range(n * n)] for i in range(n * n)]
        self.result = []
        self.difficulty = difficulty

    def transpose(self):
        self.field = list(map(list, zip(*self.field)))

    def swap_columns(self, col_1, col_2):
        for i in range(len(self.field)):
            self.field[i][col_1], self.field[i][col_2] = self.field[i][col_2], self.field[i][col_1]

    def swap_rows(self, row_1, row_2):
        self.field[row_1], self.field[row_2] = self.field[row_2], self.field[row_1]
    
    def swap_vertical_area(self, col_1, col_2):
        for k in range(len(self.field)):
            for i in range(self.n):
                  self.field[k][(col_1 * self.n) + i], self.field[k][(col_2 * self.n) + i] = self.field[k][(col_2 * self.n) + i], self.field[k][(col_1 * self.n) + i]

    def swap_horizontal_area(self, row_1, row_2):
        for i in range(self.n):
            self.field[(row_1 * self.n) + i], self.field[(row_2 * self.n) + i] = self.field[(row_2 * self.n) + i], self.field[(row_1 * self.n) + i]

    def generate_field(self):
        iterations = random.randint(1000, 1100)
        for i in range(iterations):
            operation = random.randint(0, 4)
            if operation == 0: 
                self.transpose()
            elif operation == 1:
                cell = random.randint(0, self.n - 1)
                first = random.randint(0, self.n - 1)
                second = random.randint(0, self.n - 1)
                self.swap_columns(cell * self.n + first, cell * self.n + second)
            elif operation == 2:
                cell = random.randint(0, self.n - 1)
                first = random.randint(0, self.n - 1)
                second = random.randint(0, self.n - 1)
                self.swap_rows(cell * self.n + first, cell * self.n + second)
            elif operation == 3:
                first = random.randint(0, self.n - 1)
                second = random.randint(0, self.n - 1)
                self.swap_horizontal_area(first, second)
            elif operation == 4:
                first = random.randint(0, self.n - 1)
                second = random.randint(0, self.n - 1)
                self.swap_vertical_area(first, second)
        
        self.result = deepcopy(self.field)
        for i in range(self.difficulty):
            x = random.randint(0, self.n * self.n - 1)
            y = random.randint(0, self.n * self.n - 1)
            self.result[x][y] = -1
        return self.result

    def get_solution(self):
        return self.field


# Example
# inits a generator with 16x16 field, 60 cells removed
generator = Generator(n=4, difficulty=60)
# generates a field and returns a generated field
field = generator.generate_field()
# prints a generated field, then prints a solution to that field
print(*field, sep="\n", end="\n\n")
print(*generator.get_solution(), sep="\n")
