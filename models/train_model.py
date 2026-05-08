import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load Dataset
df = pd.read_csv("../dataset/StudentsPerformance.csv")

# Create Total Score
df['total_score'] = (
    df['math score'] +
    df['reading score'] +
    df['writing score']
)

# Create Performance Category
def performance_label(score):

    if score >= 250:
        return "Good"

    elif score >= 180:
        return "Average"

    else:
        return "Poor"

df['performance'] = df['total_score'].apply(
    performance_label
)

# Features
X = df[
    ['math score',
     'reading score',
     'writing score']
]

# Target
y = df['performance']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL ACCURACY:\n")

print(round(accuracy * 100, 2), "%")

with open("student_model.pkl", "wb") as file:

    pickle.dump(model, file)

print("MODEL SAVED")