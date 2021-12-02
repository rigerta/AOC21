
def part1(fileName):  

    fwd_tot = 0
    down_tot = 0

    with open(f'data/{fileName}') as f:

        lines = f.read().splitlines()

        for line in lines:

            command = line.split()[0]
            step = int(line.split()[1])

            if command == 'forward':
                fwd_tot += step 
            elif command == 'down':
                down_tot += step 
            elif command == 'up':
                down_tot -= step 
    f.close()
    return fwd_tot * down_tot

def part2(fileName):
    
    fwd_tot = 0
    down_tot = 0
    aim = 0 

    with open(f'data/{fileName}') as f:

        lines = f.read().splitlines()

    for line in lines:

        command = line.split()[0]
        step = int(line.split()[1])

        if command == 'forward':
            fwd_tot += step 
            down_tot += aim * step 
        elif command == 'down':
            aim += step 
        elif command == 'up':
            aim -= step 
    f.close()
    return fwd_tot * down_tot

print(f'Solution Day 2 Part 1: {part1("2.txt")}')
print(f'Solution Day 2 Part 2: {part2("2.txt")}')