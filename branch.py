import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1.Generate random data with NUMPY
np.random.seed(0)
student_ids = np.arange(1,21)
entc_scores = np.random.randint(50,100,size=20)
cse_scores = np.random.randint(50,100,size=20)
mech_scores = np.random.randint(50,100,size=20)

#2.Create a DataFrame with pandas 
df = pd.DataFrame({
    'StudentID': student_ids,
    'entc': entc_scores,
    'cse' : cse_scores,
    'mech' : mech_scores 
})

print("First 5 rows of the DataFrame:")
print(df.head())

#3.Basic analysis with pandas
print("\nAverage scores:")
print(df[['entc','cse','mech']].mean())

print("\nStudent with highest entc score:")
print(df.loc[df['entc'].idxmax()])

#4.Visualization with Matplotlib
plt.figure(figsize=(8,5))
plt.plot(df['StudentID'],df['entc'],marker='o',label='entc')
plt.plot(df['StudentID'],df['cse'],marker='s',label='cse')
plt.plot(df['StudentID'],df['mech'],marker='^',label='mech')
plt.xlabel('Student ID')
plt.ylabel('Score')
plt.title('Student Scores by Subject')
plt.legend()
plt.show()

#5.Visualization with Seaborn
plt.figure(figsize=(8,5))
sns.boxplot(data=df[['entc','cse','mech']])
plt.title('Score Distribution by Subject')
plt.ylabel('Score')
plt.show()