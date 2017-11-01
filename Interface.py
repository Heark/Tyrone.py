
# GUI Code
import tkinter
import sys
import threading

class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.WINDOW.quit()
    def End_Tyrone(self):
        print("Closing Tyrone")
        sys.exit()


    def run(self):
        self.WINDOW = tkinter.Tk()
        self.WINDOW.protocol("WM_DELTE_WINDOW", self.callback)
        self.WINDOW.winfo_toplevel().title("Tyrone")
        Exit_button = tkinter.Button(self.WINDOW, text="Stop Tyrone", command=self.End_Tyrone)

        Exit_button.pack()
        self.WINDOW.mainloop()
