
# GUI Code
import tkinter
import sys
import threading

class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
    def End_Tyrone(self):
        print("Closing Tyrone")
        sys.exit()


    def run(self):
        self.root = tkinter.Tk()
        self.root.protocol("WM_DELTE_WINDOW", self.callback)
        self.root.winfo_toplevel().title("Tyrone")
        Exit_button = tkinter.Button(self.root, text="Stop Tyrone", command=self.End_Tyrone)

        Exit_button.pack()
        self.root.mainloop()
