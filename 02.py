file = open("02.txt", "r")

game_id = 1
threshold = {"red": 12, "green": 13, "blue": 14}
sum_of_possible_game_ids = 0
total_power = 0
for line in file.readlines():
    line = line.strip("\n")
    line = line.split(":")[1]
    sets = line.split(";")

    max_count_by_color = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        color_counts = set.split(",")
        for count in color_counts:
            color = count.split(" ")[2]
            amount = int(count.split(" ")[1])
            if amount > max_count_by_color[color]:
                max_count_by_color[color] = amount

    game_is_possible = True
    for item in threshold.items():
        if item[1] < max_count_by_color[item[0]]:
            game_is_possible = False

    game_power = max_count_by_color["red"] * max_count_by_color["green"] * max_count_by_color["blue"]
    total_power += game_power

    if game_is_possible:
        sum_of_possible_game_ids += game_id

    game_id += 1

print("Sum of possible game ids: " + str(sum_of_possible_game_ids))
print("Total power: " + str(total_power))
