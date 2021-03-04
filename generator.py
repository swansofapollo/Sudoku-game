import random


class Grid:
    def __init__(self, n=4):
        """Generation of the base table"""
        self.n = n
        self.table = [[((i * n + i // n + j) % (n * n)) for j in range(n * n)] for i in range(n * n)]

    def __del__(self):
        pass

    def show(self):
        for i in range(self.n * self.n):
            print(self.table[i])

    def transposing(self):
        """ Transposing the whole grid """
        self.table = map(list, zip(*self.table))

    def swap_rows_small(self):
        """ Swap the two rows """
        area = random.randrange(0, self.n, 1)
        line1 = random.randrange(0, self.n, 1)
        # получение случайного района и случайной строки
        N1 = area * self.n + line1
        # номер 1 строки для обмена

        line2 = random.randrange(0, self.n, 1)
        while (line1 == line2):
            line2 = random.randrange(0, self.n, 1)

        N2 = area * self.n + line2
        # номер 2 строки для обмена

        self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_small(self):
        self.transposing()
        self.swap_rows_small()
        self.transposing()


    def swap_rows_area(self):
        """ Swap the two area horizon """
        area1 = random.randrange(0, self.n, 1)
        # получение случайного района

        area2 = random.randrange(0, self.n, 1)
        while (area1 == area2):
            area2 = random.randrange(0, self.n, 1)

        for i in range(0, self.n):
            N1, N2 = area1 * self.n + i, area2 * self.n + i
            self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def mix(self, amt=10):
        mix_func = ['self.transposing()',
                    'self.swap_rows_small()',
                    'self.swap_colums_small()',
                    'self.swap_rows_area()']
        for i in range(1, amt):
            id_func = random.randrange(0, len(mix_func), 1)
            eval(mix_func[id_func])



a = Grid()
a.mix()
a.show()