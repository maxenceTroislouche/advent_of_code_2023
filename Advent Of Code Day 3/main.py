from typing import List

TEST_FILE = "test.txt"
INPUT_FILE = "input.txt"

TEST_EXPECTED_RESULT_PART_ONE = 4361
TEST_EXPECTED_RESULT_PART_TWO = 467835


class Symbol:
    row_idx: int
    col_idx: int
    symbol: str

    def __init__(self, symbol: str, row_idx: int, col_idx: int):
        self.symbol = symbol
        self.row_idx = row_idx
        self.col_idx = col_idx

    def __str__(self):
        return f"{self.symbol}: {self.row_idx}/{self.col_idx}"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_character_a_symbol(c: str) -> bool:
        """
        Checks that a character corresponds to a symbol
        """
        if c.isdigit():
            return False

        if c == ".":
            return False

        return True


class Gear(Symbol):
    part_numbers: List
    is_valid = False

    def __init__(self, row_idx: int, col_idx: int):
        super().__init__("*", row_idx, col_idx)
        self.part_numbers = []
        self.is_valid = False

    def check_for_part_numbers(self, numbers):
        for number in numbers:
            if number.check_validity(self):
                self.part_numbers.append(number)

        if len(self.part_numbers) == 2:
            self.is_valid = True


class Number:
    num: int
    row_idx: int
    col_idx: int
    is_valid: bool
    length: int  # Length of the string representation of the number

    def __init__(self, num: int, row_idx: int, col_idx: int):
        self.num = num
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.is_valid = False

        self.length = len(str(self.num))

    def __str__(self) -> str:
        return f"{self.num}: {self.row_idx}/{self.col_idx} - {self.is_valid} - {self.length}"

    def __repr__(self):
        return self.__str__()

    def check_validity(self, symbol: Symbol) -> bool:
        # Checks if the symbol is adjacent to the number
        min_valid_col_idx = self.col_idx - 1
        max_valid_col_idx = self.col_idx + self.length

        min_valid_row_idx = self.row_idx - 1
        max_valid_row_idx = self.row_idx + 1

        return (min_valid_row_idx <= symbol.row_idx <= max_valid_row_idx and
                min_valid_col_idx <= symbol.col_idx <= max_valid_col_idx)

    def check_validity_with_list_of_symbols(self, symbols: List):
        # Checks that at least one symbol is adjacent to the number
        for symbol in symbols:
            if self.check_validity(symbol):
                self.is_valid = True
                return


def extract_numbers_from_string(file_lines: List):
    # Returns a list of numbers
    list_of_numbers = []

    for row_idx, line in enumerate(file_lines):
        buf = ""
        for col_idx, c in enumerate(line):
            if c.isdigit():
                buf += c
            else:
                if buf:
                    list_of_numbers.append(Number(int(buf), row_idx, col_idx - len(buf)))
                    buf = ""

        if buf:
            list_of_numbers.append(Number(int(buf), row_idx, col_idx - len(buf)))

    return list_of_numbers


def extract_symbols_from_string(file_lines: List):
    # Returns a list of symbols
    list_of_symbols = []
    for row_idx, line in enumerate(file_lines):
        for col_idx, c in enumerate(line):
            if Symbol.is_character_a_symbol(c):
                if c == '*':
                    symbol = Gear(row_idx, col_idx)
                else:
                    symbol = Symbol(c, row_idx, col_idx)

                list_of_symbols.append(symbol)

    return list_of_symbols


def read_file(filename):
    lines = []

    with open(filename, "r") as f:
        s = f.readline()
        while s:
            s = s.replace("\n", "")  # Remove trailing \n

            lines.append(s)
            s = f.readline()

    return lines


def calculate_sum_from_list_of_numbers_and_symbols(numbers, symbols):
    sum_of_numbers = 0

    for number in numbers:
        number.check_validity_with_list_of_symbols(symbols)
        if number.is_valid:
            sum_of_numbers += number.num

    return sum_of_numbers


def calculate_sum_of_gears_ratio(numbers, gears):
    sum_of_gears = 0
    for gear in gears:
        gear.check_for_part_numbers(numbers)
        if gear.is_valid:
            sum_of_gears += gear.part_numbers[0].num * gear.part_numbers[1].num

    return sum_of_gears


def test_part_one():
    print("Test part One")

    lines = read_file(TEST_FILE)
    print(lines)

    numbers_extracted = extract_numbers_from_string(lines)
    print("Numbers extracted")
    print(numbers_extracted)

    symbols_extracted = extract_symbols_from_string(lines)
    print("Symbols extracted")
    print(symbols_extracted)

    sum_of_numbers = calculate_sum_from_list_of_numbers_and_symbols(numbers_extracted, symbols_extracted)

    print(f"sum: {sum_of_numbers}")
    print(f"Expected sum: {TEST_EXPECTED_RESULT_PART_ONE}")

    print([num for num in numbers_extracted if not num.is_valid])
    print(set([symbol.symbol for symbol in symbols_extracted]))

    if sum_of_numbers != TEST_EXPECTED_RESULT_PART_ONE:
        print("TEST FAILED !")
    else:
        print("TEST SUCCEEDED !")


def solve_part_one():
    print("Solve part One")

    lines = read_file(INPUT_FILE)
    print(lines)

    numbers_extracted = extract_numbers_from_string(lines)
    print("Numbers extracted")
    print(numbers_extracted)

    symbols_extracted = extract_symbols_from_string(lines)
    print("Symbols extracted")
    print(symbols_extracted)

    sum_of_numbers = calculate_sum_from_list_of_numbers_and_symbols(numbers_extracted, symbols_extracted)

    print([num for num in numbers_extracted if not num.is_valid])
    print(set([symbol.symbol for symbol in symbols_extracted]))

    print(f"sum: {sum_of_numbers}")


def test_part_two():
    print("Test part Two")

    lines = read_file(TEST_FILE)
    numbers_extracted = extract_numbers_from_string(lines)
    symbols_extracted = extract_symbols_from_string(lines)

    gears_extracted = [symbol for symbol in symbols_extracted if isinstance(symbol, Gear)]
    print(gears_extracted)

    sum_of_gears_ratio = calculate_sum_of_gears_ratio(numbers_extracted, gears_extracted)
    print(sum_of_gears_ratio)
    print(TEST_EXPECTED_RESULT_PART_TWO)

    if sum_of_gears_ratio == TEST_EXPECTED_RESULT_PART_TWO:
        print("TEST SUCCEEDED !")
    else:
        print("TEST FAILED !")


def solve_part_two():
    print("Solve part Two")

    lines = read_file(INPUT_FILE)
    numbers_extracted = extract_numbers_from_string(lines)
    symbols_extracted = extract_symbols_from_string(lines)

    gears_extracted = [symbol for symbol in symbols_extracted if isinstance(symbol, Gear)]
    print(gears_extracted)

    sum_of_gears_ratio = calculate_sum_of_gears_ratio(numbers_extracted, gears_extracted)
    print(sum_of_gears_ratio)


if __name__ == '__main__':
    # test_part_one()
    # solve_part_one()
    test_part_two()
    solve_part_two() 
