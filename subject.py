import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1.Generate random data with NUMPY
np.random.seed(0)
student_ids = np.arange(1,21)
math_scores = np.random.randint(50,100,size=20)
english_scores = np.random.randint(50,100,size=20)
science_scores = np.random.randint(50,100,size=20)

#2.Create a DataFrame with pandas 
df = pd.DataFrame({
    'StudentID': student_ids,
    'Math': math_scores,
    'English' : english_scores,
    'Science' : science_scores 
})

print("First 5 rows of the DataFrame:")
print(df.head())

#3.Basic analysis with pandas
print("\nAverage scores:")
print(df[['Math','English','Science']].mean())

print("\nStudent with highest Math score:")
print(df.loc[df['Math'].idxmax()])

#4.Visualization with Matplotlib
plt.figure(figsize=(8,5))
plt.plot(df['StudentID'],df['Math'],marker='o',label='Math')
plt.plot(df['StudentID'],df['English'],marker='s',label='English')
plt.plot(df['StudentID'],df['Science'],marker='^',label='Science')
plt.xlabel('Student ID')
plt.ylabel('Score')
plt.title('Student Scores by Subject')
plt.legend()
plt.show()

#5.Visualization with Seaborn
plt.figure(figsize=(8,5))
sns.boxplot(data=df[['Math','English','Science']])
plt.title('Score Distribution by Subject')
plt.ylabel('Score')
plt.show()