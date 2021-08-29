column = int(input())
row = int(input())


def is_coordinate_by_the_border(coordinate):
    return coordinate < 2 or coordinate > 7


is_column_by_border = is_coordinate_by_the_border(column)
is_row_by_border = is_coordinate_by_the_border(row)

if is_column_by_border and is_row_by_border:
    print("3")
elif is_column_by_border or is_row_by_border:
    print("5")
else:
    print("8")
