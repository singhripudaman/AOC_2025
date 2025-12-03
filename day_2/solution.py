def solve_part_one(input_text):
    ids = []
    for sequence in input_text:
        start, end = sequence.split("-")
        for i in range(int(start), int(end) + 1):
            if len(str(i)) % 2 != 0:
                continue
            string_num = str(i)
            first, last = (
                string_num[: len(string_num) // 2],
                string_num[len(string_num) // 2 :],
            )
            if first == last:
                ids.append(i)
    return sum(ids)


def solve_part_two(input_text):
    unique = set()
    for sequence in input_text:
        start, end = sequence.split("-")
        for num in range(int(start), int(end) + 1):
            string_num = str(num)
            for sequence_length in range(1, len(string_num) // 2 + 1):
                chunks = set(
                    string_num[i : i + sequence_length]
                    for i in range(0, len(string_num), sequence_length)
                )
                if len(chunks) == 1:
                    unique.add(num)
                    break
    return sum(unique)


def main():
    with open("input.txt", "r") as f:
        ranges = f.readline().split(",")
        print(f"Solution of part one is {solve_part_one(ranges)}")
        print(f"Solution of part two is {solve_part_two(ranges)}")


if __name__ == "__main__":
    main()
