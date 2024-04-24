# import speech_recognition as speech_recognition

# def transcribe_video(video_file):
#     # 音声認識用のRecognizerオブジェクトを作成
#     recognizer = speech_recognition.Recognizer()

#     # 自己紹介動画から音声を読み込む
#     with speech_recognition.AudioFile(video_file) as source:
#         audio_data = recognizer.record(source)

#     # Google Speech Recognition APIを使用して音声を文字起こしする
#     try:
#         transcript = recognizer.recognize_google(audio_data, language="ja-JP")
#         return transcript
#     except speech_recognition.UnknownValueError:
#         return "音声が認識できませんでした"
#     except speech_recognition.RequestError:
#         return "Google Speech Recognition APIにアクセスできませんでした"

# # 自己紹介動画のファイルパスを指定して文字起こしを実行
# video_path = 'sample_move1.wav'  # 音声ファイルが必要です
# result = transcribe_video(video_path)

# # 文字起こし結果を出力
# print(result)
import sys

sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
# speech_recognition.path.append('/opt/homebrew/lib/python3.11/site-packages')
import speech_recognition as sr
from moviepy.editor import VideoFileClip

def transcribe_video(video_path):
    # 動画から音声を抽出してWAVファイルとして保存する
    audio_path = "sample_move1.wav"
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    # 音声認識を行う
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)  # 音声ファイルを読み込む

    # Google Web Speech APIを使用して音声から文字起こしを取得する
    try:
        text = recognizer.recognize_google(audio, language="ja-JP")
        return text
    except sr.UnknownValueError:
        return "音声を認識できませんでした"
    except sr.RequestError:
        return "Google Web Speech API にアクセスできませんでした"

if __name__ == "__main__":
    video_path = "sample_move1.mp4"  # 自己紹介動画のパスを指定する
    result = transcribe_video(video_path)
    print("文字起こし結果:")
    print(result)