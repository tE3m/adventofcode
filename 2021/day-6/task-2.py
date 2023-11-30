def main(days: int):
    fishes = [int(number) for number in open("input.txt").readline().strip().split(",")]
    fish_dict = {index: 0 for index in range(0, 9)}
    for fish in fishes:
        fish_dict[fish] += 1
    for _ in range(days):
        reproducing = fish_dict[0]
        for age in range(0, 8):
            fish_dict[age] = fish_dict[age+1]
        fish_dict[6] += reproducing
        fish_dict[8] = reproducing
    print(str(sum(fish_dict[age] for age in range(0, 9))))


if __name__ == '__main__':
    main(256)
