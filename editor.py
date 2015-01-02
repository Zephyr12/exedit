import Tkinter as tk
import tkMessageBox as tkmsg
import tkFileDialog as tkfile
'''
Author : Amartya Vadlamani
This Code is licenced under the GNU Public Licence V2
'''
def langload(state):
	tkmsg.askyesno("Hey you! Hey Listen!","Did you see date when this was published? Do you think I have the time. Gimme a week")

def new(widgets,state):
	if(state["unsaved changes"]):
		if(tkmsg.askyesno("Are you sure","You didn't save")):
				widgets["textarea"].delete(1.0,"end")

def save(widgets,state):
	outfile = tkfile.asksaveasfile(mode="w",defaultextension=".txt")
	if outfile == None:#user canceled with cancel button
		return
	text = str(widgets["textarea"].get(1.0,"end"))
	outfile.write(text)
	outfile.close()

def openandload(widgets,state):
	new(widgets,state)
	infile = tkfile.askopenfile(mode="r")
	text = infile.read()
	widgets["textarea"].insert(1.0,text)

def onchange(state):
	state["unsaved changes"] = True

mainwin = {}
programstate ={"unsaved changes":False}
def initComponents():
	mainwin["basepanel"] = tk.Tk()
	mainwin["basepanel"].option_add("*tearOff","FALSE")
	
	mainwin["menubar"] = tk.Menu(mainwin["basepanel"])
	
	mainwin["menubar"].add_command(label="New",command=lambda:new(mainwin,programstate))
	mainwin["menubar"].add_command(label="Open",command=lambda:openandload(mainwin,programstate))
	mainwin["menubar"].add_command(label="Save",command=lambda:save(mainwin,programstate))
	mainwin["menubar"].add_command(label="Set Language File",command=lambda:langload(programstate))
	mainwin["textarea"] = tk.Text(mainwin["basepanel"],width=80,height=10)
	mainwin["textarea"].bind("<<Modified>>",lambda x: onchange(programstate))
	mainwin["textarea"]["wrap"] = "none"
	mainwin["textarea"].pack(fill="both",expand=1)
	mainwin["basepanel"].config(menu=mainwin["menubar"])


initComponents()

mainwin["basepanel"].mainloop()
