import azure.cognitiveservices.speech as speechsdk
import tkinter as tk

def speech_recognition_with_microphone():
    # Azure Cognitive Services Speechリソースのキーとエンドポイント
    speech_key = "YOUR_SPEECH_KEY"
    service_region = "YOUR_SERVICE_REGION"


    # スピーチ認識用の設定
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("英単語の発音を確認します。話してください...")
    result = speech_recognizer.recognize_once()

    # 結果の表示
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("認識結果: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("音声が認識できませんでした。")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("認識がキャンセルされました。詳細: {}".format(cancellation_details.reason))

if __name__ == "__main__":
    speech_recognition_with_microphone()

#ウィンドウ作成
window = tk.Tk()
window.title("発音&単語クイズ")
window.geometry("300x200")

#ラベル作成
result_label = tk.Label(window, text="結果がここに表示されます", font=("Arial", 12))
result_label.pack(pady=20)

# ボタンを作成
button = tk.Button(window, text="音声認識開始", font=("Arial", 12), command=speech_recognition_with_microphone)
button.pack()

# ウィンドウを表示
window.mainloop()