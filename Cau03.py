
import tkinter as tk
from tkinter import ttk

# Hàm để xử lý nút "Enter data"
def submit_data():
    print("Data submitted")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Data Entry Form")
root.geometry("700x300")

# Khung thông tin người dùng
user_info_frame = ttk.LabelFrame(root, text="User Information")
user_info_frame.pack(fill="x", padx=10, pady=5)

# Trường nhập tên
ttk.Label(user_info_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
first_name_entry = ttk.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

# Trường nhập họ
ttk.Label(user_info_frame, text="Last Name").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
last_name_entry = ttk.Entry(user_info_frame)
last_name_entry.grid(row=0, column=3, padx=5, pady=5)

# Trường nhập chức danh
ttk.Label(user_info_frame, text="Title").grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr.", "Prof."])
title_combobox.grid(row=0, column=5, padx=5, pady=5)

# Trường nhập tuổi
ttk.Label(user_info_frame, text="Age").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_spinbox = ttk.Spinbox(user_info_frame, from_=0, to=120)
age_spinbox.grid(row=1, column=1, padx=5, pady=5)

# Trường nhập quốc tịch
ttk.Label(user_info_frame, text="Nationality").grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
nationality_entry = ttk.Entry(user_info_frame)
nationality_entry.grid(row=1, column=3, padx=5, pady=5)

# Khung đăng ký
registration_frame = ttk.LabelFrame(root, text="Registration Status")
registration_frame.pack(fill="x", padx=10, pady=5)

# Hộp kiểm trạng thái đăng ký
registered_check = ttk.Checkbutton(registration_frame, text="Currently Registered")
registered_check.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Hộp quay số số khóa học đã hoàn thành
ttk.Label(registration_frame, text="# Completed Courses").grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
completed_courses_spinbox = ttk.Spinbox(registration_frame, from_=0, to=50)
completed_courses_spinbox.grid(row=0, column=2, padx=5, pady=5)

# Hộp quay số số học kỳ
ttk.Label(registration_frame, text="# Semesters").grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
semesters_spinbox = ttk.Spinbox(registration_frame, from_=0, to=20)
semesters_spinbox.grid(row=0, column=4, padx=5, pady=5)

# Khung Điều khoản và Điều kiện
terms_frame = ttk.LabelFrame(root, text="Terms & Conditions")
terms_frame.pack(fill="x", padx=10, pady=5)

# Hộp kiểm chấp nhận điều khoản
terms_check = ttk.Checkbutton(terms_frame, text="I accept the terms and conditions.")
terms_check.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Nút Gửi dữ liệu
submit_button = ttk.Button(root, text="Enter data", command=submit_data)
submit_button.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
