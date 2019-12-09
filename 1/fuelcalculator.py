import math

def calculate_fuel(mass):
    return (math.floor(mass / 3)) - 2

def calculate_total_fuel_from_file(filename):
    total_fuel = 0
    f = open(filename)
    line = f.readline()
    while line:
        total_fuel += calculate_fuel(int(line))
        line = f.readline()
    f.close()
    return total_fuel

if __name__ == '__main__':
    print(calculate_total_fuel_from_file("masses.txt"))