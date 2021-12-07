def main():
    positions: list[int] = [int(position) for position in open("input.txt").readline().split(",")]
    fuelCosts = {possiblePosition: sum(fuelConsumption for position in positions for fuelConsumption in range(abs(position-possiblePosition)+1)) for possiblePosition in range(min(positions), max(positions)+1)}
    print(min(fuelCosts.values()))


if __name__ == '__main__':
    main()
