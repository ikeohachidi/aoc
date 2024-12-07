vowels = "aeiou"
invalid_combination = ("ab", "cd", "pq", "xy")

class Solution:
    def __init__(self, filepath):
        with open(filepath, "r") as file:
            self.input = file.readlines()

    def _contains_vowel_count(self, input):
        count = 0
        for char in input:
            if char in vowels:
                count += 1
        return count >= 3
    
    def _contains_double_pair(self, input):
        for index in range(len(input) - 1):
            if input[index] == input[index + 1]:
                return True
        return False

    def _contains_invalid_pair(self, input):
        for index in range(len(input) - 1):
            if input[index:index + 2] in invalid_combination:
                return True
        return False

    def _contains_overlap(self, input):
        pairs = {}
        for index in range(len(input) - 1):
            pair = input[index:index + 2]

            # Check if pair exists and is non-overlapping
            if pair in pairs and pairs[pair] < index - 1:
                return True

            # Store the first occurrence of the pair
            if pair not in pairs:
                pairs[pair] = index
        return False

    def _contains_repeat(self, input):
        for index in range(len(input) - 2):
            if input[index] == input[index + 2]:
                return True
        return False

    def part1(self):
        count = 0
        for line in self.input:
            line = line.rstrip("\n")
            if self._contains_vowel_count(line) and \
            self._contains_double_pair(line) and not \
            self._contains_invalid_pair(line):
                count += 1
        print(count)

    def part2(self):
        count = 0
        for line in self.input:
            line = line.rstrip("\n")
            if self._contains_overlap(line) and self._contains_repeat(line):
                count += 1
        print(count)

s = Solution("input.txt")
s.part2()
