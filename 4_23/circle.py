import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 画像読み込み
img_rgb = plt.imread('resource/4-23icon.png')

# 画像の中心座標を計算
height, width, _ = img_rgb.shape
center_x, center_y = width // 2, height // 2

# 切り出す円の半径を画像の横幅の1/4に設定
radius = width // 4

# 描画
fig, ax = plt.subplots()
im = ax.imshow(img_rgb)

# 円形にクリップするための円のパッチを作成
clip_circle = patches.Circle((center_x, center_y), radius=radius, transform=ax.transData)

# クリップパスを設定
im.set_clip_path(clip_circle)

# 軸の非表示化
ax.axis('off')

# 保存
plt.savefig('resource/clip_circle.jpg', dpi=150)