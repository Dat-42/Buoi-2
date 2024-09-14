import numpy as np
import tkinter as tk
from tkinter import messagebox


def calculate_gpa():
    try:
        # Lấy dữ liệu từ ô nhập liệu
        data_str = entry_data.get("1.0", "end-1c")
        if not data_str.strip():
            raise ValueError("Input cannot be empty.")

        # Phân tách dữ liệu theo dòng, mỗi dòng là một môn học
        rows = data_str.strip().split('\n')
        grades = []
        credits = []

        for row in rows:
            if ',' in row:
                grade_str, credit_str = row.split(',')
                grade = float(grade_str.strip())
                credit = float(credit_str.strip())
                grades.append(grade)
                credits.append(credit)
            else:
                raise ValueError("Each line must contain a grade and credit separated by a comma.")

        # Chuyển đổi danh sách thành mảng NumPy
        grades = np.array(grades)
        credits = np.array(credits)

        if len(grades) == 0 or len(credits) == 0:
            raise ValueError("No valid data provided.")

        # Tính toán GPA
        total_credits = np.sum(credits)
        weighted_sum = np.sum(grades * credits)
        gpa = weighted_sum / total_credits

        # Hiển thị kết quả
        result_text = f"GPA: {gpa:.2f}"
        result_label.config(text=result_text)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Error: {e}")


# Tạo giao diện chính
root = tk.Tk()
root.title("GPA Calculator")

tk.Label(root, text="Enter grades and credits (grade,credit) for each subject, one per line:").pack(pady=5)
entry_data = tk.Text(root, height=10, width=50)
entry_data.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=5)

root.mainloop()