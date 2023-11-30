def main():
    positions: list[int] = [int(position) for position in open("input.txt").readline().split(",")]
    fuelCosts = {possiblePosition: sum(abs(position-possiblePosition) for position in positions) for possiblePosition in range(min(positions), max(positions)+1)}
    print(min(fuelCosts.values()))


if __name__ == '__main__':
    main()
