from cProfile import run


def main():
    positions: list[int] = [int(position) for position in open("input.txt").readline().split(",")]
    fuelCosts = (sum(int(abs(position-possiblePosition) * (abs(position-possiblePosition)+1)/2) for position in positions) for possiblePosition in range(min(positions), max(positions)+1))
    print(min(fuelCosts))


if __name__ == '__main__':
    run("main()")
