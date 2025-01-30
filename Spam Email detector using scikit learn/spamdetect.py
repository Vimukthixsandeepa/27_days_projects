import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('spam.csv')
X = data.drop('spam', axis=1)
Y = data['spam']

# Split the data into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

# Train the Logistic Regression model to classify the email
model = LogisticRegression(max_iter=200)  # Increased max_iter to avoid convergence warning
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(Y_test, y_pred)
print('Accuracy:', accuracy)

# Compute the confusion matrix
cm = confusion_matrix(Y_test, y_pred)
print('Confusion Matrix:\n', cm)

# Calculate precision, recall, and F1 score
precision = precision_score(Y_test, y_pred)
print('Precision:', precision)
recall = recall_score(Y_test, y_pred)
print('Recall:', recall)
f1 = f1_score(Y_test, y_pred)
print('F1 Score:', f1)

# Visualize the confusion matrix using seaborn
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()
