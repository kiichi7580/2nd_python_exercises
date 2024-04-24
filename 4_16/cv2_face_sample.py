# ③ 画像から顔を認識して資格で囲むプログラムを書いてください

import cv2
    
# 画像ファイルのパス
  
image_path = 'path_to_your_image2.jpg'

# 画像を読み込む
image = cv2.imread(image_path)

# グレースケールに変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# OpenCVの顔検出用のHaar Cascade分類器を読み込む
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 検出された顔の周りに四角形を描画する
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)  # 緑色の四角形を描画

# 結果の画像を表示
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)  # キー入力を待つ
cv2.destroyAllWindows()  # すべてのウィンドウを閉じる


# 顔の検出
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
