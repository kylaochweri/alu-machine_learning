#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

#data
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

#plot
plt.figure(figsize=(10, 6))
bins = range(0, 101, 10)
plt.hist(student_grades, bins=bins, color='blue', edgecolor='black')       
plt.yscale('linear')
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')
plt.show()
