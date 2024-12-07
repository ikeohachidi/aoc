from hashlib import md5


class Solution:
    def __init__(self, filepath):
        with open(filepath) as file:
            self.input = file.read()

    def part1(self):
        count = 0
        while True:
            b_hash = self.input + str(count)
            b_hash = md5(b_hash.encode()).hexdigest()

            if b_hash[:6] == "000000":
                print(f"{count} -- {b_hash}")
                return

            count += 1

s = Solution("input.txt")
s.part1()