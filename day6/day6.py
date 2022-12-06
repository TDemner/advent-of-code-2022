with open('C:/Users/ssstub/OneDrive - Scania CV/Advent of code/advent-of-code-2022/day6/day6.txt') as file:
    input = file.readlines()[0].strip()
buff = ''
count = 0
for char in input:
    if len(buff) == 14:
        buff = buff[1:]
    buff += char
    if len(list(set(buff))) == len(buff) and len(buff) >= 14:
        break
    count += 1
print(count + 1)