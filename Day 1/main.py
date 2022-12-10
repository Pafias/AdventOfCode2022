content = []

with open('input.txt', 'r') as file:
    content = file.readlines()
    file.close()

for i in range(len(content)):
    s = content[i]
    content[i] = s.replace('\n', '')

calories = {}
elf = 1
for line in content:
    if line == '':
        elf += 1
        continue
    calorie = int(line)
    if elf in calories.keys():
        calories[elf] += calorie
    else:
        calories[elf] = calorie

winner = max(calories, key=calories.get)
winnerCal = calories[winner]
calories.pop(winner)
second = max(calories, key=calories.get)
secondCal = calories[second]
calories.pop(second)
third = max(calories, key=calories.get)
thirdCal = calories[third]

print(f"Elf {winner} is carrying {winnerCal} calories.")

print(
    f"Top 3: Elf {winner} with {winnerCal} calories, elf {second} with {secondCal} calories, and elf {third} with {thirdCal} calories. That gives a total of {winnerCal + secondCal + thirdCal} calories.")
