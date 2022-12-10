content = []

with open('input.txt', 'r') as file:
    content = file.readlines()
    file.close()

for i in range(len(content)):
    s = content[i]
    content[i] = s.replace('\n', '')


def get_points(letter):
    if letter == 'A' or letter == 'X':
        return 1
    elif letter == 'B' or letter == 'Y':
        return 2
    elif letter == 'C' or letter == 'Z':
        return 3


def get_outcome_points(play1, play2):
    win = 6
    tie = 3
    loss = 0
    if play1 == 'A':  # Rock
        if play2 == 'X':  # Rock
            return tie
        elif play2 == 'Y':  # Paper
            return win
        elif play2 == 'Z':  # Scissors
            return loss
    elif play1 == 'B':  # Paper
        if play2 == 'X':  # Rock
            return loss
        elif play2 == 'Y':  # Paper
            return tie
        elif play2 == 'Z':  # Scissors
            return win
    elif play1 == 'C':  # Scissors
        if play2 == 'X':  # Rock
            return win
        elif play2 == 'Y':  # Paper
            return loss
        elif play2 == 'Z':  # Scissors
            return tie


def get_to_play(play1, desired_outcome):
    if play1 == 'A':  # Rock
        if desired_outcome == 'X':  # Lose
            return 'Z'
        elif desired_outcome == 'Y':  # Tie
            return 'X'
        elif desired_outcome == 'Z':  # Win
            return 'Y'
    elif play1 == 'B':  # Paper
        if desired_outcome == 'X':  # Lose
            return 'X'
        elif desired_outcome == 'Y':  # Tie
            return 'Y'
        elif desired_outcome == 'Z':  # Win
            return 'Z'
    elif play1 == 'C':  # Scissors
        if desired_outcome == 'X':  # Lose
            return 'Y'
        elif desired_outcome == 'Y':  # Tie
            return 'Z'
        elif desired_outcome == 'Z':  # Win
            return 'X'


total_score = 0

for round in content:
    play1 = round.split(' ')[0]
    desired_outcome = round.split(' ')[1]
    to_play = get_to_play(play1, desired_outcome)
    outcome_points = get_outcome_points(play1, to_play)
    round_points = get_points(to_play) + outcome_points
    total_score += round_points

print(f"Total score of {total_score}")
