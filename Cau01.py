
import tkinter as tk
from tkinter import font

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Frame Recorder")
root.geometry("600x300")
root.configure(bg="#d080d0")

# Tạo nhãn tiêu đề
title_font = font.Font(size=24)
title_label = tk.Label(root, text="Frame Recorder", font=title_font, bg="#d080d0")
title_label.pack(pady=20)

# Tạo khung cho trường đầu vào và nhãn
input_frame = tk.Frame(root, bg="#d080d0")
input_frame.pack(pady=10)

fps_label = tk.Label(input_frame, text="create an", bg="#d080d0")
fps_label.pack(side=tk.LEFT)

fps_entry = tk.Entry(input_frame, width=5)
fps_entry.pack(side=tk.LEFT)

fps_label_end = tk.Label(input_frame, text="fps video", bg="#d080d0")
fps_label_end.pack(side=tk.LEFT)

# Tạo khung cho các nút
button_frame = tk.Frame(root, bg="#d080d0")
button_frame.pack(pady=20)

pause_button = tk.Button(button_frame, text="Pause", width=10)
pause_button.pack(side=tk.LEFT, padx=5)

start_button = tk.Button(button_frame, text="Start", width=10)
start_button.pack(side=tk.LEFT, padx=5)

end_button = tk.Button(button_frame, text="End", width=10)
end_button.pack(side=tk.LEFT, padx=5)

# Tạo nhãn trạng thái
status_label = tk.Label(root, text="Recording Paused", bg="#d080d0")
status_label.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
