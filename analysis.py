import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("dataset/StudentsPerformance.csv")

# Display first 5 rows
print("\nFIRST 5 ROWS OF DATASET:\n")

print(df.head())

# Display column names
print("\nCOLUMN NAMES:\n")

print(df.columns)

# Display dataset shape
print("\nDATASET SHAPE:\n")

print(df.shape)

# Display missing values
print("\nMISSING VALUES:\n")

print(df.isnull().sum())

# Average Scores

math_avg = df['math score'].mean()

reading_avg = df['reading score'].mean()

writing_avg = df['writing score'].mean()

print("\nAVERAGE SCORES:\n")

print("Math Average:", round(math_avg, 2))

print("Reading Average:", round(reading_avg, 2))

print("Writing Average:", round(writing_avg, 2))


# Highest Scores

print("\nHIGHEST SCORES:\n")

print("Highest Math Score:",
      df['math score'].max())

print("Highest Reading Score:",
      df['reading score'].max())

print("Highest Writing Score:",
      df['writing score'].max())


# Lowest Scores

print("\nLOWEST SCORES:\n")

print("Lowest Math Score:",
      df['math score'].min())

print("Lowest Reading Score:",
      df['reading score'].min())

print("Lowest Writing Score:",
      df['writing score'].min())

# Visualization

subjects = ['Math', 'Reading', 'Writing']

average_scores = [
    math_avg,
    reading_avg,
    writing_avg
]

plt.figure(figsize=(8,5))

sns.barplot(
    x=subjects,
    y=average_scores
)

plt.title("Average Subject Scores")

plt.ylabel("Average Marks")

plt.show()

# Gender-wise Average Scores

gender_scores = df.groupby('gender')[
    ['math score',
     'reading score',
     'writing score']
].mean()

print("\nGENDER WISE SCORES:\n")

print(gender_scores)

# Gender-wise Visualization

gender_scores.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Gender-wise Average Scores")

plt.ylabel("Average Marks")

plt.xticks(rotation=0)

plt.show()