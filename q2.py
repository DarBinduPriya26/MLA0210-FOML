# Q2: Logistic Regression without libraries

import csv
import math

# Create CSV
data = [
    ["Feature1", "Feature2", "Spam"],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0]
]

with open("logistic.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV Created!")

# Read data
X = []
Y = []

with open("logistic.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        X.append([1, int(row[0]), int(row[1])])  # bias term
        Y.append(int(row[2]))

# Initialize weights
weights = [0, 0, 0]
learning_rate = 0.1

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Training
for epoch in range(1000):
    for i in range(len(X)):
        z = sum(X[i][j] * weights[j] for j in range(3))
        pred = sigmoid(z)
        error = Y[i] - pred
        for j in range(3):
            weights[j] += learning_rate * error * X[i][j]

print("Trained Weights:", weights)

# Prediction
test = [1, 1, 1]
z = sum(test[j] * weights[j] for j in range(3))
prediction = sigmoid(z)

print("Predicted Probability:", prediction)

if prediction >= 0.5:
    print("Prediction: Spam")
else:
    print("Prediction: Not Spam")
