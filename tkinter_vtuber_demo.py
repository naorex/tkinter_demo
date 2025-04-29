import tkinter


class Application(tkinter.Frame):
    """tkinter.Frame クラスを継承して widget を作成"""

    def __init__(self, root):
        super().__init__(
            root, width=420, height=320, borderwidth=4, relief="groove"  # 境界線の太さ
        )  # 境界線の種類
        self.root = root
        self.pack()  # 位置を設定して配置
        self.pack_propagate(0)  # サイズ調整
        self.create_widgets()

    def create_widgets(self):

        # Quit button
        quit_btn = tkinter.Button(self)
        quit_btn["text"] = "Close"
        quit_btn["command"] = self.root.destroy
        quit_btn.pack(side="bottom")

        # Text box
        self.text_box = tkinter.Entry(self)
        self.text_box["width"] = 10
        self.text_box.pack()

        # Execute button
        submit_btn = tkinter.Button(self)
        submit_btn["text"] = "Execute"
        submit_btn["command"] = self.input_handler
        submit_btn.pack()

        # Message output
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_handler(self):
        text = self.text_box.get()
        self.message["text"] = text + "!!"


root = tkinter.Tk()
root.title("Demo App")
root.geometry("400x300")
app = Application(root=root)
app.mainloop()
