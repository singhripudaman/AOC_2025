def solve_part_one(input_text):
    nums = []
    for line in input_text:
        int_list = [int(num) for num in line.strip()]
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
            # if last number, don't bother checking for a new one
            if biggest_index == len(int_list) - 1:
                # swap for convenience
                biggest, second_biggest = second_biggest, biggest
            else:
                second_biggest = 0
                for num in int_list[biggest_index + 1 : len(int_list)]:
                    if num > second_biggest:
                        second_biggest = num
        nums.append(int(str(biggest) + str(second_biggest)))

    return sum(nums)


def solve_part_two(input_text):
    nums = []
    for line in input_text:
        digits_required = 12
        int_list = [int(num) for num in line.strip()]
        # for i in range(digits_required, -1, -1):

        #     print(i)

        shortened = int_list[: len(int_list) + 1 - digits_required]
        starting_value = shortened.index(max(shortened))

        required_nums = sorted(int_list[starting_value:], reverse=True)[
            :digits_required
        ]
        number_components = []
        for num in int_list[starting_value:][::-1]:
            if num in required_nums:
                required_nums.remove(num)
                number_components.append(num)
        nums.append(int("".join(str(x) for x in number_components[::-1])))
    return nums


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(f"Solution of part one is {solve_part_one(lines)}")
        print(f"Solution of part two is {solve_part_two(lines)}")


if __name__ == "__main__":
    main()
