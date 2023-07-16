import tkinter as tk
import csv
import random as rd

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("380x200")
        self.master.title("英→日テスト")

        self.canvas = tk.Canvas(self.master, bg = "white", width = 50, height = 50)
        self.canvas.place(x = 30,y = 135)
        self.Load_dictionary_from_csv()
        self.SetVar()
        self.widget()

        #self.master.bind("<Return>", self.EnterJudge)

    def SetVar(self):
        self.judgeNum = -1
        self.num = rd.randint(0,len(self.wordlist) - 1)


#csvファイルの読み込み
    def Load_dictionary_from_csv(self):
        f = open("dictionary.csv","r",encoding = "utf-8-sig")

        self.wordlist = list(csv.reader(f))

        f.close()

    #部品の配置
    def widget(self):

        self.text1 = tk.Entry(self.master, width = 33)
        self.text1.place(x = 50, y = 30)

        self.text1.insert(0,self.wordlist[self.num][0])
        self.text2 = tk.Entry(self.master, width = 33)
        self.text2.place(x = 50, y = 90)

        self.BtnJudge = tk.Button(self.master, text = "check", command = self.Judge, width = 10)
        self.BtnJudge.place(x = 110, y = 148)

        self.BtnNext = tk.Button(self.master, text = "次の単語", command = self.Next, width = 10)
        self.BtnNext.place(x = 215, y = 148)

    def Judge(self):
        if self.text2.get() == self.wordlist[self.num][1]:
            self.marupro()
        else:
            self.batsupro()

    def ClickJudge(self):
        self.Judge()

    def marupro(self):
        self.canvas.delete("batsu1")
        self.canvas.delete("batsu2")
        self.judgeNum = 1
        self.canvas.create_oval(10,10,43,43,outline = "red", width = 5, tag = "maru")

    def batsupro(self):
        self.canvas.create_line(10,10,43,43,fill = "black", width = 5, tag = "batsu1")
        self.canvas.create_line(10,43,43,10,fill = "black", width = 5, tag = "batsu2")
        self.text2.delete(0,tk.END)

    def Next(self):
        if self.judgeNum == 1:
            self.canvas.delete("maru")
            self.num = rd.randint(1,len(self.wordlist) - 1)
            self.text1.delete(0,tk.END)
            self.text2.delete(0,tk.END)
            self.text1.insert(0,self.wordlist[self.num][0])
            ##self.select4()
            self.judgeNum = -1

def main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()


if __name__ == "__main__":
    main()

