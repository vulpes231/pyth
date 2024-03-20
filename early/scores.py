scores = []

for i in range(3):
    score = int(input("Enter score: "))
    scores.append(score)

average = sum(scores) / len(scores)
print(average)
