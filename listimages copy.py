import os
from PIL import Image
import matplotlib.pyplot as plt

# 指定要列出檔案的資料夾路徑
folder_path = '/Users/jason'

# 設定縮圖的大小
thumbnail_size = (100, 100)

# 取得資料夾內所有圖像檔案
image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# 準備顯示圖像
fig, axes = plt.subplots(1, len(image_files), figsize=(len(image_files) * 2, 2))

# 如果只有一張圖片，axes 不是 list，需要轉成 list
if len(image_files) == 1:
    axes = [axes]

# 讀取和顯示每張圖像的縮圖
for ax, file in zip(axes, image_files):
    image_path = os.path.join(folder_path, file)
    img = Image.open(image_path)
    img.thumbnail(thumbnail_size)  # 建立縮圖
    ax.imshow(img)
    ax.axis('off')  # 隱藏軸線
    ax.set_title(file)  # 顯示檔案名稱

plt.show()
