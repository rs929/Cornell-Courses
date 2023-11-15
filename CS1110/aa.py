def pad_square(ragged):
    countcol = len(ragged)
    for k in ragged:
        countrow = 0
        for y in k:
            countrow += 1
    if countcol > countrow:
        for row in range(len(ragged)):
            numzeros = [0]
            row.append(numzeros) * (countrow - countcol)

    if countrow > countcol:
        newcollist = [0] * (countcol-countrow)
        ragged.append(newcollist)