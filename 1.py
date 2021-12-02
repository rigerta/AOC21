
def part1(fileName):  

    counter = 0 
    prev_number = 999999999 

    with open(f'data/{fileName}') as f:

        lines = f.read().splitlines()
        lines = [int(x) for x in lines]

        for number in lines:
            if number > prev_number:
                counter +=1
            prev_number = number
    f.close()
    return counter

def part2(fileName):
    
    counter = 0 
    prev_sum = 9999999

    with open(f'data/{fileName}') as f:
        lines = f.read().splitlines()
        lines = [int(x) for x in lines]

        # we only iterate until the 3rd last element, not until the very end
        for i in range(len(lines)-2):
            sum = lines[i] + lines[i+1] + lines[i+2]
            if sum > prev_sum:
                counter += 1
            prev_sum = sum
    f.close()
    return counter

print(f'Solution Day 1 Part 1: {part1("1.txt")}')
print(f'Solution Day 1 Part 2: {part2("1.txt")}')