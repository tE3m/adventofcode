def main(days: int):
    fishes = [int(number) for number in open("input.txt").readline().strip().split(",")]
    for day in range(days):
        fishes = [8 if fish == 0 else fish-1 for fish in fishes]
        for _ in filter(lambda fish: fish == 8, fishes):
            fishes.append(6)
    print(len(fishes))


if __name__ == '__main__':
    main(80)
    