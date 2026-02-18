# Q3: KNN without libraries

import csv
import math

# Create CSV
data = [
    ["Feature1", "Feature2", "Spam"],
    [1, 1, "Spam"],
    [1, 0, "Spam"],
    [0, 1, "Spam"],
    [0, 0, "NotSpam"],
    [0, 1, "NotSpam"],
    [1, 0, "NotSpam"]
]

with open("knn.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV Created!")

# Read data
dataset = []
with open("knn.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        dataset.append([int(row[0]), int(row[1]), row[2]])

# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Test sample
test = [1, 1]
k = 3

distances = []

for data in dataset:
    dist = distance(test, data)
    distances.append((dist, data[2]))

distances.sort()

neighbors = distances[:k]

spam_count = 0
notspam_count = 0

for neighbor in neighbors:
    if neighbor[1] == "Spam":
        spam_count += 1
    else:
        notspam_count += 1

if spam_count > notspam_count:
    print("Prediction: Spam")
else:
    print("Prediction: NotSpam")
