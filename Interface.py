
# GUI Code
import tkinter
import sys
import Tyrone as Main
import threading

class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.WINDOW.quit()
    def End_Tyrone(self):
        print("Closing Tyrone")
        Main.tyrone.close()
        sys.exit()


    def run(self):
        self.WINDOW = tkinter.Tk()
        self.WINDOW.protocol("WM_DELTE_WINDOW", self.callback)
        self.WINDOW.winfo_toplevel().title("Tyrone")
        Exit_button = tkinter.Button(self.WINDOW, text="Stop Tyrone", command=self.End_Tyrone)

        Exit_button.pack()
        self.WINDOW.mainloop()

Window = GUI()
Main.tyrone.run("MzAwODczNTk0OTYyMDUxMDcz.DRJ1qQ.alcoIqu19idpANf8dYZVEeapQsg")
