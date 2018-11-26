import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        # Рекомендуемая практика определять все состовлющие класса в __init__.
        # В данном случае имя hi_there и quit которое поторое используется для объекта
        # tkinter.Button
        self.hi_there: tk.Button = None
        self.quit: tk.Button = None

    def create_widgets(self):
        self.hi_there = tk.Button(self, bg="green")
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    @staticmethod
    def say_hi(self):
        print("hi there, everyone!")


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = tk.StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # Привязываем свойство "textvariable" объекта tkinter.Entry
        # к переменной типа: tkinter.StringVar
        self.entrythingy["textvariable"] = self.contents
        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->", self.contents.get())
        print(type(self))
        if self.contents.get() == "quit":
            root.destroy()


def fun(event):
    print(event)


root = tk.Tk()
app = App(master=root)
ent0 = tk.Entry()
ent0.pack()
ent0.bind('<Key>', fun)
app.mainloop()