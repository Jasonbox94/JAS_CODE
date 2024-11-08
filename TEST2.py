import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# 指定要列出檔案的資料夾路徑
folder_path = '/Users/jason/Desktop'

# 右鍵選單保存圖片的功能
def save_image(img, filename):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=filename,
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img.save(file_path)
        print(f"圖片已保存到：{file_path}")

# 主程式
root = tk.Tk()
root.title("Image Viewer")

# 設置視窗大小
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)
root.geometry(f"{window_width}x{window_height}")

# 檢查資料夾是否存在並取得圖像檔案
image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# 創建滾動框架
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=v_scrollbar.set)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 使用 Frame 作為滾動內容的容器
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# 更新滾動區域
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", configure_canvas)

# 設置圖片大小
thumbnail_size = (200, 200)

# 顯示圖片和文字
for file in image_files:
    image_path = os.path.join(folder_path, file)
    img = Image.open(image_path)
    img.thumbnail(thumbnail_size)
    img_tk = ImageTk.PhotoImage(img)

    # 創建 Label 控件顯示圖片
    image_label = tk.Label(scrollable_frame, image=img_tk)
    image_label.image = img_tk  # 保存圖片引用以防止垃圾回收
    image_label.pack(pady=10)

    # 添加右鍵點擊選單
    def on_right_click(event, img=img, filename=file):
        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="另存圖片", command=lambda: save_image(img, filename))
        menu.post(event.x_root, event.y_root)

    image_label.bind("<Button-3>", on_right_click)

    # 顯示圖片名稱
    text_label = tk.Label(scrollable_frame, text=file, wraplength=200, justify="center")
    text_label.pack()

root.mainloop()
