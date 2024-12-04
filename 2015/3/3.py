up = "^"
down = "v"
left = "<"
right = ">"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    # def __eq__(self, value: object) -> bool:
    #     return value.x == self.x and value.y == self.y

with (open("./input.txt", "r") as file):
    content = file.read()
    coord = Point(0, 0)
    uniqueCoord = set()

    for char in content:
        if char == up:
            coord.y += 1
        elif char == down:
            coord.y -= 1
        elif char == left:
            coord.x -= 1
        elif char == right:
            coord.x += 1
        
        # uniqueCoord.add((coord.x, coord.y))
        uniqueCoord.add(coord)

print(len(uniqueCoord))