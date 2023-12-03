def read_file():
    filename = "input_part_2.txt"
    lines = []

    with open(filename, "r") as f:
        s = f.readline()
        while s:
            lines.append(s)
            s = f.readline()

    return lines


def calculate_calibration_value(string: str) -> int:
    """
    Calibration value is the combination of the first digit and the last digit of the string
    :param string:
    :return:
    """

    string_to_numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    # Mon idée est de replace "one" par "1one"
    for key, value in string_to_numbers.items():
        string = string.replace(key, f"{key}{value}{key}")

    first_digit = None
    last_digit = None
    for c in string:
        if c.isnumeric():
            last_digit = c
            if first_digit is None:
                first_digit = c

    print(f"{first_digit} / {last_digit} / {int(first_digit + last_digit)}")

    return int(first_digit + last_digit)


def main():
    lines = read_file()
    sum = 0

    for line in lines:
        sum += calculate_calibration_value(line)

    print(sum)


if __name__ == "__main__":
    main()
