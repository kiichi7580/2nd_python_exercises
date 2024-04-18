# ① 財布の中に入っているレシートの合計金額を数えるプログラムを書いてください
wallet = []
count = input('レシートの枚数を教えてください : ')

for i in range(int(count)):
    r = input('商品の値段を教えてください : ')
    wallet.append(int(r))


print(f"合計金額は{sum(wallet)}円です")

# ② 日本語をローマ字に変換するプログラムを書いてください
import romkan

# 日本語の文字列をローマ字に変換する例
japanese_text = "こんにちは、元気ですか？"
romaji_text = romkan.to_roma(japanese_text)
print(romaji_text)  # Output: "konnichiwa, genki desu ka?"

# ローマ字を日本語に変換する例
romaji_input = "konnichiwa, genki desu ka?"
japanese_output = romkan.to_hiragana(romaji_input)
print(japanese_output)  # Output: "こんにちは、げんきですか？"

text = "はしめまして"
rote = romkan.to_roma(text)
print(rote)

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

# 顔の検出
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 検出された顔の周りに四角形を描画する
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)  # 緑色の四角形を描画

# 結果の画像を表示
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)  # キー入力を待つ
cv2.destroyAllWindows()  # すべてのウィンドウを閉じる