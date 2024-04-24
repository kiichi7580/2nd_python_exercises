import cv2
import dlib


def detect_faces(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)
    
    if image is None:
        print("画像が読み込めませんでした。")
        return None, None

    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Dlibの顔検出器を初期化
    detector = dlib.get_frontal_face_detector()

    # 顔の検出
    faces = detector(gray)

    if len(faces) == 0:
        print("顔が検出されませんでした。")
        return None, None

    return image, faces