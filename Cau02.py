
import tkinter as tk
from tkinter import font

# Tạo cửa sổ chính
root = tk.Tk()
root.title("AtarBals Modern Antivirus")
root.geometry("800x500")

# Khung cho thanh bên
sidebar = tk.Frame(root, bg="#3366cc", width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Thêm các nhãn vào thanh bên
sidebar_items = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
for item in sidebar_items:
    label = tk.Label(sidebar, text=item, bg="#3366cc", fg="white", font=('Arial', 12))
    label.pack(pady=10, padx=10, anchor='w')

# Nút "Scan Now" trong thanh bên
scan_now_button = tk.Button(sidebar, text="Scan Now", bg="lime", fg="black", font=('Arial', 12))
scan_now_button.pack(pady=20, padx=10)

# Khung cho khu vực nội dung chính
main_content = tk.Frame(root, bg="white")
main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Thêm nhãn tiêu đề vào khu vực nội dung chính
title_label = tk.Label(main_content, text="Scan", font=('Arial', 24), bg="white")
title_label.pack(pady=10)

# Thêm nhãn phụ đề vào khu vực nội dung chính
subtitle_label = tk.Label(main_content, text="Premium will be free forever. You just need to click button.", font=('Arial', 12), bg="white")
subtitle_label.pack(pady=5)

# Khung cho các nút chức năng
button_frame = tk.Frame(main_content, bg="white")
button_frame.pack(pady=20)

# Tạo các nút chức năng
buttons = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
for btn_text in buttons:
    button = tk.Button(button_frame, text=btn_text, bg="magenta", fg="black", font=('Arial', 12), width=15, height=2)
    button.pack(side=tk.LEFT, padx=10, pady=5)

# Thêm nhãn trạng thái vào khu vực nội dung chính
status_label = tk.Label(main_content, text="Get Premium to Enable: (Web Protection), (Full Scan), (Simple Update)", font=('Arial', 10), bg="white", fg="red")
status_label.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
