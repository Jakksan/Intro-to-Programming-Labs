import pprint

cols = int(input("Cols: "))
rows = int(input("Rows: "))

one_row = cols * [0]
grid = []
for r in range(rows):
    grid.append(one_row+[]) # deep copy

print(grid)
# pprint.pprint(grid)
