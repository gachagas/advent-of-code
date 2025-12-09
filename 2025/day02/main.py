import sys
import traceback
from pathlib import Path


def exception_handler(type, value, exc_traceback):
    print("=" * 50)
    print("Exception occured:")
    traceback.print_exception(type, value, exc_traceback)
    print("=" * 50)


sys.excepthook = exception_handler


def part_one(filename: str):
    valid_ids = []

    with open(Path(__file__).resolve().parent / filename) as file:
        for line in file:  # loop only once since its only one line
            long_str = line
            ranges = long_str.split(",")

            for num_range in ranges:
                start, end = num_range.split("-")

                for number in range(int(start), int(end) + 1):
                    len_half = int(len(str(number)) / 2)
                    if len(str(number)) % 2 != 0:
                        continue

                    first_half = str(number)[:len_half]
                    second_half = str(number)[len_half:]

                    if int(first_half) == int(second_half):
                        valid_ids.append(int(first_half + second_half))
    print(sum(valid_ids))


def part_two(filename: str):
    valid_ids = []

    with open(Path(__file__).resolve().parent / filename) as file:
        for line in file:  # loop only once since its only one line
            long_str = line
            ranges = long_str.split(",")

            for num_range in ranges:
                start, end = num_range.split("-")

                for number in range(int(start), int(end) + 1):
                    str_number = str(number)
                    len_half = int(len(str_number) / 2)
                    # print(f"processing number {number} in range {num_range}")
                    temp_arr = []

                    found = False
                    for window_size in range(1, len_half + 1):
                        if found:
                            break

                        if (len(str(number))) % window_size != 0:
                            continue
                        temp_arr = []

                        for i in range(0, len(str_number), window_size):
                            temp_arr.append(str_number[i : i + window_size])
                            # print(f"{temp_arr=} {window_size=} {number=}")

                        if len(set(temp_arr)) == 1 and len(temp_arr) != 1:
                            # print(f"appending {temp_arr}")
                            valid_ids.append(int("".join(temp_arr)))
                            found = True
                            break
                print(
                    f"{''.join(temp_arr)} is an invalid id for range {num_range}, counted at number {number} {window_size}"
                )

    print(sum(valid_ids))


if __name__ == "__main__":
    filename = sys.argv[1]
    part_two(filename=filename)
