# Q4: Accuracy Calculation Example

# Assume predictions and actual values
actual = ["Spam", "Spam", "NotSpam", "Spam", "NotSpam"]
predicted_nb = ["Spam", "Spam", "NotSpam", "Spam", "NotSpam"]
predicted_lr = ["Spam", "NotSpam", "NotSpam", "Spam", "NotSpam"]
predicted_knn = ["Spam", "Spam", "Spam", "Spam", "NotSpam"]

def accuracy(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return (correct / len(actual)) * 100

print("Naive Bayes Accuracy:", accuracy(actual, predicted_nb), "%")
print("Logistic Regression Accuracy:", accuracy(actual, predicted_lr), "%")
print("KNN Accuracy:", accuracy(actual, predicted_knn), "%")
