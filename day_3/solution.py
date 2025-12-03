def solve_part_one(input_text):
    nums = []
    for line in input_text:
        line = line.strip()
        int_list = [int(num) for num in line]
        biggest, biggest_index = 0, -1
        second_biggest, second_biggest_index = 0, -1
        for i, num in enumerate(int_list):
            if num > biggest:
                second_biggest = biggest
                second_biggest_index = biggest_index
                biggest = num
                biggest_index = i
            elif num > second_biggest:
                second_biggest = num
                second_biggest_index = i

        # bigger number appears later, choose another number that appears after
        if biggest_index > second_biggest_index:
            # if last number, don't bother
            if biggest_index != len(int_list) - 1:
                second_biggest = 0
                for num in int_list[biggest_index + 1 : len(int_list)]:
                    if num > second_biggest:
                        second_biggest = num
                nums.append(int(str(biggest) + str(second_biggest)))
            else:
                nums.append(int(str(second_biggest) + str(biggest)))
        else:
            nums.append(int(str(biggest) + str(second_biggest)))

    return sum(nums)


def solve_part_two(input_text):
    return 0


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(f"Solution of part one is {solve_part_one(lines)}")
        print(f"Solution of part two is {solve_part_two(lines)}")


if __name__ == "__main__":
    main()
