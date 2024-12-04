up = "^"
down = "v"
left = "<"
right = ">"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))  # Use a tuple of attributes for 

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def update_coords(self, direction):
        if direction == up:
            return Point(self.x, self.y + 1)
        elif direction == down:
            return Point(self.x, self.y - 1)
        elif direction == left:
            return Point(self.x - 1, self.y)
        elif direction == right:
            return Point(self.x + 1, self.y)

class Solution():
    def __init__(self, filepath):
        with open(filepath, "r") as file:
            self.content = file.read()
    def part1(self):
        coord = Point(0, 0)
        uniqueCoord = set()

        for char in self.content:
            coord.update_coords(char)
            uniqueCoord.add(coord)

        print(len(uniqueCoord))

    def part2(self):
        santaCoords = Point(0, 0)
        roboCoords = Point(0, 0)

        homes = set()
        homes.add(Point(0, 0))

        for index in range(len(self.content)):
            # santa
            if index % 2 == 0:
                santaCoords = santaCoords.update_coords(self.content[index])
                homes.add(santaCoords)
            else:
                roboCoords = roboCoords.update_coords(self.content[index])
                homes.add(roboCoords)
        
        print(len(homes))

s = Solution("input.txt")
s.part2()