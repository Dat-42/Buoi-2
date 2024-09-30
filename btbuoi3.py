import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, scrolledtext

# Đọc file CSV
df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = df.to_numpy()

# Hàm để hiển thị toàn bộ dữ liệu
def show_all_data():
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, df.to_string())

# Hàm để hiển thị tổng số sinh viên đi thi
def show_total_students():
    tongsv = in_data[:, 1]
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, f"Tổng số sinh viên đi thi: {np.sum(tongsv)}")

# Hàm để hiển thị lớp có nhiều điểm nhất
def show_max_scores():
    diemA = in_data[:, 3]
    diemA_plus = in_data[:, 2]
    diemB = in_data[:, 5]
    diemB_plus = in_data[:, 4]
    diemC = in_data[:, 7]
    diemC_plus = in_data[:, 6]
    diemD = in_data[:, 9]
    diemD_plus = in_data[:, 8]
    diemF = in_data[:, 10]

    max_a = df.index[np.argmax(diemA)]
    max_a_plus = df.index[np.argmax(diemA_plus)]
    max_b = df.index[np.argmax(diemB)]
    max_b_plus = df.index[np.argmax(diemB_plus)]
    max_c = df.index[np.argmax(diemC)]
    max_c_plus = df.index[np.argmax(diemC_plus)]
    max_d = df.index[np.argmax(diemD)]
    max_d_plus = df.index[np.argmax(diemD_plus)]
    max_f = df.index[np.argmax(diemF)]

    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, f"Lớp có nhiều điểm A nhất: {max_a}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm A+ nhất: {max_a_plus}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm B nhất: {max_b}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm B+ nhất: {max_b_plus}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm C nhất: {max_c}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm C+ nhất: {max_c_plus}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm D nhất: {max_d}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm D+ nhất: {max_d_plus}\n")
    text_area.insert(tk.END, f"Lớp có nhiều điểm F nhất: {max_f}\n")

# Hàm để hiển thị thống kê điểm
def show_statistics():
    plt.figure()
    diemA = in_data[:, 3]
    diemA_plus = in_data[:, 2]
    diemB = in_data[:, 5]
    diemB_plus = in_data[:, 4]
    diemC = in_data[:, 7]
    diemC_plus = in_data[:, 6]
    diemD = in_data[:, 9]
    diemD_plus = in_data[:, 8]
    diemF = in_data[:, 10]

    plt.plot(range(len(diemA)), diemA, 'r-', label="Điểm A")
    plt.plot(range(len(diemA_plus)), diemA_plus, 'm-', label="Điểm A+")
    plt.plot(range(len(diemB)), diemB, 'b-', label="Điểm B")
    plt.plot(range(len(diemB_plus)), diemB_plus, 'g-', label="Điểm B+")
    plt.plot(range(len(diemC)), diemC, 'y-', label="Điểm C")
    plt.plot(range(len(diemC_plus)), diemC_plus, 'c-', label="Điểm C+")
    plt.plot(range(len(diemD)), diemD, 'k-', label="Điểm D")
    plt.plot(range(len(diemD_plus)), diemD_plus, 'orange', label="Điểm D+")
    plt.plot(range(len(diemF)), diemF, 'purple', label="Điểm F")
    plt.xlabel("Lớp")
    plt.ylabel("Số sinh viên đạt điểm")
    plt.legend(loc='upper right')
    plt.title("Thống kê điểm")
    plt.show()

# Hàm để hiển thị chuẩn đầu ra
def show_output_standard():
    plt.figure()
    l1 = in_data[:, 11]
    l2 = in_data[:, 12]

    plt.plot(range(len(l1)), l1, 'r-', label="L1")
    plt.plot(range(len(l2)), l2, 'g-', label="L2")
    plt.xlabel("Lớp")
    plt.ylabel("Chuẩn đầu ra")
    plt.legend(loc='upper right')
    plt.title("Chuẩn đầu ra")
    plt.show()

# Hàm để hiển thị điểm thường xuyên
def show_regular_scores():
    plt.figure()
    tx1 = in_data[:, 13]
    tx2 = in_data[:, 14]

    plt.plot(range(len(tx1)), tx1, 'r-', label="TX1")
    plt.plot(range(len(tx2)), tx2, 'g-', label="TX2")
    plt.xlabel("Lớp")
    plt.ylabel("Điểm thường xuyên")
    plt.legend(loc='upper right')
    plt.title("Điểm thường xuyên")
    plt.show()

# Hàm để hiển thị điểm cuối kỳ
def show_final_scores():
    plt.figure()
    final_scores = in_data[:, 15]

    plt.plot(range(len(final_scores)), final_scores, 'b-', label="Điểm cuối kỳ")
    plt.xlabel("Lớp")
    plt.ylabel("Điểm cuối kỳ")
    plt.legend(loc='upper right')
    plt.title("Điểm cuối kỳ")
    plt.show()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý điểm")

# Tạo các nút lựa chọn
btn_all_data = ttk.Button(root, text="Hiển thị toàn bộ dữ liệu", command=show_all_data)
btn_total_students = ttk.Button(root, text="Tổng số sinh viên đi thi", command=show_total_students)
btn_max_scores = ttk.Button(root, text="Lớp có nhiều điểm nhất", command=show_max_scores)
btn_statistics = ttk.Button(root, text="Thống kê điểm", command=show_statistics)
btn_output_standard = ttk.Button(root, text="Chuẩn đầu ra", command=show_output_standard)
btn_regular_scores = ttk.Button(root, text="Điểm thường xuyên", command=show_regular_scores)
btn_final_scores = ttk.Button(root, text="Điểm cuối kỳ", command=show_final_scores)

# Đặt các nút lên cửa sổ
btn_all_data.pack(pady=10)
btn_total_students.pack(pady=10)
btn_max_scores.pack(pady=10)
btn_statistics.pack(pady=10)
btn_output_standard.pack(pady=10)
btn_regular_scores.pack(pady=10)
btn_final_scores.pack(pady=10)

# Tạo khu vực hiển thị văn bản
text_area = scrolledtext.ScrolledText(root, width=100, height=20)
text_area.pack(pady=10)

# Chạy ứng dụng
root.mainloop()
