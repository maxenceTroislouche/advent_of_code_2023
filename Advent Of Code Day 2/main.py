colors_and_numbers = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def read_file():
    filename = "input.txt"
    lines = []

    with open(filename, "r") as f:
        s = f.readline()
        while s:
            lines.append(s)
            s = f.readline()

    return lines


def get_game_id_from_line(line: str):
    """
    Gets the game id from the line
    """
    first_part = line.split(":")[0]
    game_id = first_part.split(" ")[1]

    return int(game_id)


def split_line_to_number_and_colors(line: str):
    """
    Returns an array containing a tuple with number and color
    """
    second_part_of_line = line.split(":")[1]
    different_plays = second_part_of_line.split(";")

    list_numbers_and_colors = []

    for different_play in different_plays:
        # Extract the color and the number
        different_play = different_play.replace("\n", "").replace(",", "")
        str_split = different_play.split(" ")[1:]
        it = iter(str_split)
        for number, color in zip(it, it):
            list_numbers_and_colors.append((number, color))

    return list_numbers_and_colors


def check_list_numbers_and_colors(list_numbers_and_colors):
    for values in list_numbers_and_colors:
        if int(values[0]) > colors_and_numbers.get(values[1]):
            return False

    return True


def get_minimum_amount_of_each_color(list_numbers_and_colors):
    minimums = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for values in list_numbers_and_colors:
        if int(values[0]) > minimums.get(values[1]):
            minimums[values[1]] = int(values[0])

    return minimums


def calculate_power_from_minimums(minimums):
    return minimums.get("red") * minimums.get("blue") * minimums.get("green")


def solve_part_1():
    lines = read_file()
    sum_of_ids = 0
    for line in lines:
        list_numbers_and_colors = split_line_to_number_and_colors(line)
        if check_list_numbers_and_colors(list_numbers_and_colors):
            sum_of_ids += get_game_id_from_line(line)

    print(sum_of_ids)


def solve_part_2():
    lines = read_file()
    sum_of_powers = 0
    for line in lines:
        list_numbers_and_colors = split_line_to_number_and_colors(line)
        minimums = get_minimum_amount_of_each_color(list_numbers_and_colors)
        sum_of_powers += calculate_power_from_minimums(minimums)

    print(sum_of_powers)


if __name__ == '__main__':
    solve_part_2()
