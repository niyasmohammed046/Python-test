def honeycomb_pattern(rows, cols):
    for i in range(rows):
        print(" " * (i % 2), end="")
        for j in range(cols):
            print("/ \\", end=" ")
        print()
        print(" " * (i % 2), end="")
        for j in range(cols):
            print("\\_/", end=" ")
        print()

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
honeycomb_pattern(rows, cols)