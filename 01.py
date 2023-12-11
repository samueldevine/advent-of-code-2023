import os
os.remove("01_modified.txt")

file = open("01.txt", "r")
calibration_values = []

def find_calibration_values(file) -> None:
    for line in file.readlines():
        for char in line:
            if char.isnumeric():
                val1 = char
                break

        for char in line[::-1]:
            if char.isnumeric():
                val2 = char
                break

        calibration_values.append(int(val1 + val2))

find_calibration_values(file)
print(sum(calibration_values))
file.close()

# Part 2
calibration_values = []
number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six":6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

original_file = open("01.txt", "r")
modified_file = open("01_modified.txt", "x")

for line in original_file.readlines():
    new_line = line
    for k, v in number_map.items():
        if k in line:
            new_line = new_line.replace(k, f"{k[0]}{str(v)}{k[-1]}")
    modified_file.write(new_line)

original_file.close()
modified_file.close()
modified_file = open("01_modified.txt", "r")

find_calibration_values(modified_file)
print(sum(calibration_values))

