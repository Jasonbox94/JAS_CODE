import os
from PIL import Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
import textwrap

# 指定要列出檔案的資料夾路徑
folder_path = '/Users/jason/Desktop'

try:
    print("檢查資料夾是否存在並取得圖像檔案...")
    # 檢查資料夾是否存在並取得圖像檔案
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if not image_files:
        print("Error: No image files found in the specified directory.")
    else:
        print("找到圖像檔案，開始設置視窗...")
        # 設定縮圖的大小
        thumbnail_size = (200, 200)
        images_per_row = 5  # 每行顯示圖片數量

        # 使用 Arial Unicode MS 字體路徑
        font_path = '/Library/Fonts/Arial Unicode.ttf'  # macOS 示例路徑，請根據實際路徑修改
        font_prop = FontProperties(fname=font_path)

        # 初始化 tkinter 視窗
        root = tk.Tk()
        root.title("Image Viewer")

        # 設置視窗大小為螢幕解析度的 90%
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        root.geometry(f"{window_width}x{window_height}")
        print("視窗初始化完成。")

        # 創建滾動框架
        frame = ttk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        # 創建畫布以放置滾動區域
        canvas = tk.Canvas(frame)
        v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
        
        # 配置畫布的滾動條
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # 使用 Frame 作為畫布中的可滾動內容
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # 更新滾動區域
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 設置 matplotlib 圖像
        print("設置 matplotlib 圖像...")
        num_rows = (len(image_files) + images_per_row - 1) // images_per_row  # 計算行數
        fig, axes = plt.subplots(num_rows, images_per_row, figsize=(images_per_row * 2, num_rows * 2.5))
        fig.subplots_adjust(hspace=1.2)  # 調整圖片與文字的間距

        # 將 axes 二維陣列轉成一維，方便迭代處理每個圖像
        axes = axes.flatten()

        # 讀取和顯示每張圖像的縮圖
        print("讀取和顯示每張圖像的縮圖...")
        for ax, file in zip(axes, image_files):
            image_path = os.path.join(folder_path, file)
            img = Image.open(image_path)
            img.thumbnail(thumbnail_size)  # 建立縮圖
            ax.imshow(img)
            ax.axis('off')

            # 設定檔案名稱並將文字顯示在圖片下方
            wrapped_title = "\n".join(textwrap.wrap(file, width=15))  # 調整寬度以適應圖片
            ax.set_title(wrapped_title, fontproperties=font_prop, fontsize=8, y=-0.3, ha='center')  # 固定 y 值將文字置於圖片下方

        # 隱藏多餘的軸
        for ax in axes[len(image_files):]:
            ax.axis('off')

        # 使用 FigureCanvasTkAgg 將 matplotlib 圖表嵌入 tkinter 視窗
        print("將圖表嵌入 tkinter 視窗...")
        canvas_plot = FigureCanvasTkAgg(fig, master=scrollable_frame)
        canvas_plot.draw()
        canvas_plot.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # 啟動 tkinter 視窗
        print("啟動 tkinter 視窗...")
        root.mainloop()

except FileNotFoundError:
    print(f"Error: The directory '{folder_path}' does not exist.")
except Exception as e:
    print(f"Unexpected error: {e}")

# 避免程式直接退出
input("Press Enter to exit...")
