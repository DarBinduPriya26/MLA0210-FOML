# Q1: Naive Bayes for Spam Detection (No external libraries)

import csv

# Step 1: Create CSV file
data = [
    ["Free", "Win", "Offer", "Spam"],
    ["Yes", "Yes", "Yes", "Spam"],
    ["Yes", "No", "Yes", "Spam"],
    ["No", "Yes", "Yes", "Spam"],
    ["No", "No", "Yes", "NotSpam"],
    ["No", "Yes", "No", "NotSpam"],
    ["Yes", "No", "No", "NotSpam"],
    ["No", "No", "No", "NotSpam"]
]

with open("spam.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data[0])
    writer.writerows(data[1:])

print("CSV File Created Successfully!")

# Step 2: Read CSV
with open("spam.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
rows = rows[1:]

spam_count = 0
notspam_count = 0

for row in rows:
    if row[3] == "Spam":
        spam_count += 1
    else:
        notspam_count += 1

total = len(rows)

p_spam = spam_count / total
p_notspam = notspam_count / total

print("Prior Probability Spam:", p_spam)
print("Prior Probability NotSpam:", p_notspam)

# Predict for new email
new_mail = ["Yes", "Yes", "Yes"]

def likelihood(index, value, label):
    count = 0
    total_label = 0
    for row in rows:
        if row[3] == label:
            total_label += 1
            if row[index] == value:
                count += 1
    return count / total_label

prob_spam = p_spam
prob_notspam = p_notspam

for i in range(3):
    prob_spam *= likelihood(i, new_mail[i], "Spam")
    prob_notspam *= likelihood(i, new_mail[i], "NotSpam")

if prob_spam > prob_notspam:
    print("Prediction: Spam")
else:
    print("Prediction: NotSpam")
