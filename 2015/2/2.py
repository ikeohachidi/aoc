with open("./input.txt", "r") as file:
    lines = file.readlines()
    count = 0
    ribbon = 0
    for line in lines:
        l, w, h = line.split("x")
        iL = int(l)
        iW = int(w)
        iH = int(h)

        side1 = iL*iW
        side2 = iW*iH
        side3 = iH*iL

        # part 1
        d = (2*side1) + (2*side2) + (2*side3)
        count += d + min(side1, side2, side3)

        # part 2
        ribbon += 2 * min((iL + iW), (iW + iH), (iL + iH)) + (iL * iW * iH)

    print(count, ribbon)
