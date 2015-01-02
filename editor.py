import Tkinter as tk

'''
Author : Amartya Vadlamani
This Code is licenced under the GNU Public Licence V2
'''

mainwin = {}

mainwin["basepanel"] = tk.Tk()
mainwin["basepanel"].option_add("*tearOff","FALSE")

mainwin["menubar"] = tk.Menu(mainwin["basepanel"])

mainwin["menubar"].add_command(label="New")
mainwin["menubar"].add_command(label="Open")
mainwin["menubar"].add_command(label="Save")
mainwin["menubar"].add_command(label="Set Language File")
mainwin["textarea"] = tk.Text(mainwin["basepanel"],width=80,height=10)
mainwin["textarea"]["wrap"] = "none"
mainwin["textarea"].pack(fill="both",expand=1)
mainwin["basepanel"].config(menu=mainwin["menubar"])
mainwin["basepanel"].mainloop()

