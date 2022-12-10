content = []

with open('input.txt', 'r') as file:
    content = file.readlines()
    file.close()

for i in range(len(content)):
    s = content[i]
    content[i] = s.replace('\n', '')

sum = 0

for pair in content:
    p1 = pair.split(',')[0]
    p2 = pair.split(',')[1]
    p1min = int(p1.split('-')[0])
    p1max = int(p1.split('-')[1])
    lst1 = []
    for i in range(p1min, p1max + 1):
        lst1.append(i)
    p2min = int(p2.split('-')[0])
    p2max = int(p2.split('-')[1])
    lst2 = []
    for i in range(p2min, p2max + 1):
        lst2.append(i)
    overlapping = len(set(lst1).intersection(set(lst2))) > 0
    if overlapping:
        sum += 1

print(f"{sum} pairs contain overlapping assignments")
