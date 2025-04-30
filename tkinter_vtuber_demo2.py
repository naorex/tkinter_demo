import tkinter


class Application(tkinter.Frame):
    """tkinter.Frame クラスを継承して widget を作成"""

    def __init__(self, root):
        super().__init__(root, width=380, height=580, borderwidth=1, relief="groove")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        button = tkinter.Button(self, text="Execute", command=self.submit)
        button.pack()

        self.text_box = tkinter.Entry(self, width=30)
        self.text_box.pack()

        self.text = tkinter.Text(self, width=20, height=10)
        self.text.pack()

        message = tkinter.Message(self, text="This is my app.", width=200)
        message.pack()

        label = tkinter.Label(self, text="Label1")
        label.pack()

        self.is_student = tkinter.BooleanVar()
        chk_button = tkinter.Checkbutton(self, text="Student", variable=self.is_student)
        chk_button.pack()

        self.selected_radio = tkinter.StringVar()
        radio_1 = tkinter.Radiobutton(
            self, text="TypeA", value="A", variable=self.selected_radio
        )
        radio_1.pack()

        self.items = ["Tokyo", "Chiba", "Saitama"]
        list_items = tkinter.StringVar(value=self.items)
        self.list_box = tkinter.Listbox(self, listvariable=list_items)
        self.list_box.pack()

        itemss = ["TypeA", "TypeB", "TypeC"]
        self.sp = tkinter.Spinbox(self, state="readonly", values=itemss)
        self.sp.pack()

        menu = tkinter.Menu(self.root)
        menu1 = tkinter.Menu(menu, tearoff=False)
        menu1.add_command(label="Screen Setting", command=self.screen_setting)
        menu1.add_command(label="Volume Setting", command=self.volume_setting)
        menu.add_cascade(label="settings", menu=menu1)
        self.root.config(menu=menu)

    def submit(self):
        print("Button was pushed.")

        text = self.text_box.get()
        print(f"Input text: {text}")

        t = self.text.get(1.0, tkinter.END + "-1c")
        print(t)

        print(self.is_student.get())

        print(self.selected_radio.get())

        selected_index = self.list_box.curselection()[0]
        print(self.items[selected_index])

        print(self.sp.get())

    def screen_setting(self):
        print("Screen Setting")

    def volume_setting(self):
        print("Volume Setting")


root = tkinter.Tk()
root.title("Demo App")
root.geometry("400x600")
app = Application(root=root)
app.mainloop()
