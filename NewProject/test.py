



for i in range(8):
    for j in range(8):
        if i == 1 or i == 7:
            if j == 1 or j == 7:
                print("#", end='')
            else:
                print(" ", end='')
        if i == 2 or i == 6:
            if j == 2 or j == 6:
                print("#", end='')
            else:
                print(" ", end='')
        if i == 3 or i == 5:
            if j == 3 or j == 5:
                print("#", end='')
            else:
                print(" ", end='')
        if i == 4:
            if j == 4:
                print("#", end='')
            else:
                print(" ", end='')
    print('')