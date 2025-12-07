import argparse
from typing import Optional


class Args(argparse.Namespace):
    filename: Optional[str] = None


def part_one(filename: str):
    dial_pos = 50
    count = 0
    with open(filename) as file:
        for idx, value in enumerate(file):
            cleaned_val = value.strip()

            dir = cleaned_val[0]
            number = int(cleaned_val[1:])

            if dir == "L":
                dial_pos -= number

            if dir == "R":
                dial_pos += number

            if dial_pos % 100 == 0:
                count = count + 1
    return count


def part_two(filename: str):
    """Count how many times dial passes through 0 during rotations."""
    dial_pos = 50
    count = 0

    with open(filename) as file:
        for line in file:
            cleaned_val = line.strip()
            if not cleaned_val:
                continue

            dir = cleaned_val[0]
            number = int(cleaned_val[1:])
            full_rotations, turns = divmod(number, 100)
            count = count + full_rotations

            if dir == "R":
                if (dial_pos + turns) > 100:
                    count = count + 1

                dial_pos = (dial_pos + turns) % 100

            elif dir == "L":
                if (dial_pos - turns) < 0 and dial_pos != 0:
                    count = count + 1

                dial_pos = (dial_pos - turns) % 100

            if dial_pos % 100 == 0:
                count = count + 1

    print(f"Part 2 count: {count}")
    return count


if __name__ == "__main__":
    print("Hi")
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename")
    args = parser.parse_args(namespace=Args())

    ans_one = part_one(filename=args.filename)
    ans_two = part_two(filename=args.filename)

    print(f"{ans_one=} {ans_two=}")
    # 6892
