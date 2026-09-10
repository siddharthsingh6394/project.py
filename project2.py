import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [

# Semester 1
["Semester 1", "Engineering Chemistry", 81],
["Semester 1", "Engineering Mathematics-I", 64],
["Semester 1", "Fundamentals of Electrical Engineering", 81],
["Semester 1", "Programming for Problem Solving", 64],
["Semester 1", "Environment and Ecology", 78],
["Semester 1", "Engineering Chemistry Lab", 96],
["Semester 1", "Basic Electrical Engineering Lab", 95],
["Semester 1", "Programming for Problem Solving Lab", 96],
["Semester 1", "Engineering Graphics & Design Lab", 95],

# Semester 2
["Semester 2", "Engineering Physics", 64],
["Semester 2", "Engineering Mathematics-II", 60],
["Semester 2", "Fundamentals of Electronics Engineering", 72],
["Semester 2", "Fundamentals of Mechanical Engineering", 72],
["Semester 2", "Soft Skills", 73],
["Semester 2", "Engineering Physics Lab", 96],
["Semester 2", "Basic Electronics Engineering Lab", 95],
["Semester 2", "English Language Lab", 97],
["Semester 2", "Workshop Practice Lab", 97],

# Semester 3
["Semester 3", "Material Science", 55],
["Semester 3", "Technical Communication", 79],
["Semester 3", "Data Structure", 78],
["Semester 3", "Computer Organization and Architecture", 68],
["Semester 3", "Discrete Structures & Theory of Logic", 63],
["Semester 3", "Cyber Security", 60],
["Semester 3", "Data Structure Lab", 98],
["Semester 3", "Computer Organization and Architecture Lab", 98],
["Semester 3", "Web Designing Workshop", 98],
["Semester 3", "Internship Assessment / Mini Project", 51],

# Semester 4
["Semester 4", "Mathematics-IV", 70],
["Semester 4", "Universal Human Value and Professional Ethics", 69],
["Semester 4", "Operating System", 73],
["Semester 4", "Theory of Automata and Formal Languages", 53],
["Semester 4", "Object Oriented Programming with Java", 76],
["Semester 4", "Python Programming", 69],
["Semester 4", "Operating System Lab", 94],
["Semester 4", "Object Oriented Programming with Java Lab", 96],
["Semester 4", "Cyber Security Workshop", 94],
["Semester 4", "Sports and Yoga-II", 94],

# Semester 5
["Semester 5", "Database Management System", 68],
["Semester 5", "Web Technology", 67],
["Semester 5", "Design and Analysis of Algorithm", 49],
["Semester 5", "Object Oriented System Design with C++", 75],
["Semester 5", "Application of Soft Computing", 60],
["Semester 5", "Database Management System Lab", 95],
["Semester 5", "Web Technology Lab", 94],
["Semester 5", "Design and Analysis of Algorithm Lab", 95],
["Semester 5", "Mini Project / Internship Assessment", 92],

# Semester 6
["Semester 6", "Software Engineering", 55],
["Semester 6", "Data Analytics", 64],
["Semester 6", "Computer Networks", 62],
["Semester 6", "Blockchain Architecture Design", 77],
["Semester 6", "Idea to Business Model", 73],
["Semester 6", "Software Engineering Lab", 95],
["Semester 6", "Data Analytics Lab", 96],
["Semester 6", "Computer Networks Lab", 96]
]

df = pd.DataFrame(data, columns=["Semester", "Subject", "Marks"])

print(df)

# Number of semesters
print("Total Semesters:", df["Semester"].nunique())

# Total subjects
print("Total Subjects:", len(df))

# Highest marks
print("Highest Marks:", df["Marks"].max())

# Lowest marks
print("Lowest Marks:", df["Marks"].min())

# Semester total
print("\nSemester Total:")
print(df.groupby("Semester")["Marks"].sum())

# Semester average
print("\nSemester Average:")
print(df.groupby("Semester")["Marks"].mean())

# Highest performing subject
print("\nHighest Subject:")
print(df.loc[df["Marks"].idxmax()])

# Lowest performing subject
print("\nLowest Subject:")
print(df.loc[df["Marks"].idxmin()])

# NumPy
marks = np.array(df["Marks"])

print("\nMean:", np.mean(marks))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard Deviation:", np.std(marks))

# Graph
avg = df.groupby("Semester")["Marks"].mean()

plt.plot(avg.index, avg.values, marker="o")
plt.axhline(75, linestyle="--")
plt.title("Semester-wise Average Marks")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.show()