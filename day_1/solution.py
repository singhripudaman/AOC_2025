def solve_part_one(input_text):
    counter = 0
    position = 50
    for line in input_text:
        direction, amount = line[0], int(line[1:])
        position = (
            (position + amount) % 100 if direction == "R" else (position - amount) % 100
        )
        if position == 0:
            counter += 1
    return counter


def solve_part_two(input_text):
    counter = 0
    position = 50
    at_zero = False
    for line in input_text:
        direction, amount = line[0], int(line[1:])
        full_rotations, partial_rotations = amount // 100, amount % 100
        counter += full_rotations

        print(counter, position)
        position = (
            position + partial_rotations
            if direction == "R"
            else position - partial_rotations
        )
        # edge case
        if not at_zero:
            if position > 99:
                counter += 1
            if position <= 0:
                counter += 1
        position = position % 100
        at_zero = True if position == 0 else False
    return counter


def main():
    with open("day_1.txt", "r") as f:
        lines = f.readlines()
        print(f"Solution of part one is {solve_part_one(lines)}")
        print(f"Solution of part two is {solve_part_two(lines)}")


if __name__ == "__main__":
    main()
