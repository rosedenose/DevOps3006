import re


def add_score(difficulty, name):
    updated = []
    newfile = 0
    scores = []
    try:
        scores = open("scores.txt")
    except:
        newfile = 1
    score_found = 0
    if newfile == 0:
        for line in scores.readlines():
            if name in str(line):
                score = re.sub(name, "", line)
                score = int(score.strip()) + difficulty * 3 + 5
                updated.append(f"{name} {score}\n")
                print(f"{name} has {score} points")
                score_found = 1
            else:
                updated.append(line)
        scores.close()

    if score_found == 0 or newfile == 1:
        updated.append(str(f"{name} {difficulty * 3 + 5}\n"))

    updated = ''.join(map(str, updated))
    update = open("scores.txt", "w+")
    update.write(updated)
