import cv2
import dlib
import math

from cv2_face import detect_faces

def wear_glasses(image, face):
    # Dlibのshape predictorを初期化
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # 顔器官の検出
    shape = predictor(image, face)

    # 目の座標を取得
    left_eye = (shape.part(36).x, shape.part(36).y)
    right_eye = (shape.part(45).x, shape.part(45).y)

    # 目の間の距離を計算
    eye_distance = math.sqrt((right_eye[0] - left_eye[0])**2 + (right_eye[1] - left_eye[1])**2)

    # メガネ画像の読み込み
    glasses = cv2.imread("/Users/nakasatokiichi/python-exercises/4_24/resource/glasses.png", -1)

    # メガネ画像の幅を目の間の距離に合わせてリサイズ
    glasses_width = int(1.5 * eye_distance)
    glasses_resized = cv2.resize(glasses, (glasses_width, int(glasses.shape[0] * (glasses_width / glasses.shape[1]))))

    # メガネを顔に合わせて合成
    x_offset = left_eye[0] - int(glasses_width / 3)
    y_offset = left_eye[1] - int(glasses_resized.shape[0] / 2)

    # メガネ画像のアルファチャンネルを取得
    alpha_channel = glasses_resized[:, :, 3] / 255.0

    # メガネを合成
    for c in range(0, 3):
        image[y_offset:y_offset + glasses_resized.shape[0], 
              x_offset:x_offset + glasses_width, c] = (
                  alpha_channel * glasses_resized[:, :, c] +
                  (1 - alpha_channel) * image[y_offset:y_offset + glasses_resized.shape[0], 
                                             x_offset:x_offset + glasses_width, c])

    return image

def main():
    # 入力画像ファイルのパス
    image_path = '/Users/nakasatokiichi/python-exercises/4_24/resource/path_to_your_image.jpg'

    # 顔の検出とメガネの合成
    image, faces = detect_faces(image_path)
    print(image)

    if image is not None and faces is not None:
        for face in faces:
            # メガネをかける処理
            image = wear_glasses(image, face)

        # 結果の表示
        cv2.imshow("Glasses", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()