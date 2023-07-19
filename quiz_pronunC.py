import tkinter as tk
import azure.cognitiveservices.speech as speechsdk
import csv
from random import sample

class SpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x500")
        self.master.title("発音Checker")

        entry_font = ("Arial", 25)

        self.text2 = tk.Entry(self.master, width=15, font=entry_font)
        self.text2.place(x=50, y=90)
        self.text2.focus_set()

        self.text_box = tk.Text(self.master, width=40, height=5, font=("Arial", 12))
        self.text_box.pack()

        self.speech_config = speechsdk.SpeechConfig(subscription="dc618b934d984348b8e4813047d851d4", region="japaneast")
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

        self.speech_recognizer.recognized.connect(self.process_speech)

        self.start_button = tk.Button(self.master, text="音声入力開始", command=self.start_speech)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="音声入力停止", command=self.stop_speech)
        self.stop_button.pack()

    def process_speech(self, event):
        if event.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            recognized_text = event.result.text
            self.text_box.insert(tk.END, recognized_text + "\n")

    def start_speech(self):
        self.speech_recognizer.start_continuous_recognition()

    def stop_speech(self):
        self.speech_recognizer.stop_continuous_recognition()

def main():
    win = tk.Tk()
    app = SpeechApp(win)
    win.mainloop()

if __name__ == "__main__":
    main()