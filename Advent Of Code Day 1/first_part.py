def read_file():
    filename = "input_part_1.txt"
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
