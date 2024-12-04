# Part 1
# Each list asecnding order
# Find the distance between each index
# Sum the distances

# Split the two columns from text file into 2 lists
with open("input.txt", "r") as file:
    col1 = []
    col2 = []
    for line in file:
        p = line.split()
        col1.append(int(p[0]))
        col2.append(int(p[1]))

col1.sort()
col2.sort()

dist = 0
for i in range(len(col1)):
    dist += abs(col1[i] - col2[i])

print(dist)


# Part 2
# Similarity Score
score = 0
col1_set = set(col1)
for num in col1_set:
    right_count = col2.count(num)
    score += (num * right_count)

print(score)
