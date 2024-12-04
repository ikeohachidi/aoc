with open("./input.txt", "r") as f:
    content = f.read()
    count = 0
    for index in range(len(content)):
        if count == -1:
            print(index)

        if content[index] == "(":
            count += 1
        else:
            count -= 1