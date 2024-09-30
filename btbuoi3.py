import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('diemPython.csv', index_col=0, header=0)

# Convert the DataFrame to a NumPy array
in_data = df.to_numpy()

# Print the data
print(in_data)

# Calculate the total number of students
tongsv = in_data[:, 1]
print("Tổng số sinh viên đi thi:", np.sum(tongsv))

# Extract scores for Diem A and Diem B+
diemA = in_data[:, 3]
diemBc = in_data[:, 4]

# Print the total number of students
print("Tổng số sinh viên:", np.sum(tongsv))

# Find the class with the highest Diem A
maxa = diemA.max()
i = np.where(diemA == maxa)
print("Lớp có số sinh viên đạt điểm A nhiều nhất:", df.index[i[0][0]])



# Additional analysis for other score categories (A, B, C, etc.)
# Assuming columns for other scores are present in the CSV
diemB = in_data[:, 5]  # Example column for Diem B
diemC = in_data[:, 6]  # Example column for Diem C

# Plot additional scores
plt.plot(range(len(diemA)), diemA, 'r-', label="Điểm A")
plt.plot(range(len(diemBc)), diemBc, 'g-', label="Điểm B+")
plt.plot(range(len(diemB)), diemB, 'b-', label="Điểm B")
plt.plot(range(len(diemC)), diemC, 'y-', label="Điểm C")
plt.xlabel("Lớp")
plt.ylabel("Số sinh viên đạt điểm")
plt.legend(loc='upper right')
plt.show()
