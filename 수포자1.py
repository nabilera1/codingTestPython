answers = [1,3,2,4,2]
#answers = list(map(int, input().split()))
first = [1, 2, 3, 4, 5] * 2000
second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

result = [0, 0, 0]

for i in range(len(answers)):
    if answers[i] == first[i]:
        result[0] += 1
    if answers[i] == second[i]:
        result[1] += 1
    if answers[i] == third[i]:
        result[2] += 1

print([i + 1 for i in range(len(result)) if max(result) == result[i]])