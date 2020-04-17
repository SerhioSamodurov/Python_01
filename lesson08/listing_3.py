class OrganicCell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return OrganicCell(other.cells + self.cells)

    def __mul__(self, other):
        return OrganicCell(other.cells * self.cells)

    def __floordiv__(self, other):
        return OrganicCell(other.cells // self.cells)

    def __sub__(self, other):
        return OrganicCell(self.cells - other.cells if self.cells - other.cells > 0 else 'Не положительно')

    def make_order(self, symbol, count):
        my_list = []
        for i in range(int(self.cells / count)):
            my_list.append(symbol * count + '\\n')
        my_list.append(symbol * (self.cells % count))
        return ''.join(my_list)


cell_7 = OrganicCell(12)
c = cell_7.make_order('*', 5)

cell_1 = OrganicCell(4)
cell_2 = OrganicCell(10)

cell_3 = cell_1 + cell_2
print(cell_3.cells)

cell_4 = cell_1 * cell_2
print(cell_4.cells)

cell_5 = cell_1 // cell_2
print(cell_5.cells)

cell_6 = cell_1 - cell_2
print(cell_6.cells)
