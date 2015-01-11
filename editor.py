# -*- coding: utf-8 -*- 
import Tkinter as tk
import tkMessageBox as tkmsg
import tkFileDialog as tkfile
'''
Author : Amartya Vadlamani
This Code is licenced under the GNU Public Licence V2
'''

exedit = "exedit"
def langload(state):
        tkmsg.askyesno("Hey you! Hey Listen!","Did you see date when this was published? Do you think I have the time. Gimme a week")

def new(widgets,state):
        if(state["unsaved changes"]):
                if(tkmsg.askyesno("Are you sure","You didn't save")):
                                widgets["textarea"].delete(1.0,"end")
        mainwin["basepanel"].title("Untitled Document - %s" % (exedit))

def save(widgets,state):
        outfile = tkfile.asksaveasfile(mode="w",defaultextension=".txt")
        if outfile == None: # User pressed cancel button.
                return None
        state["unsaved changes"] = False
        text = str(widgets["textarea"].get(1.0,"end"))
        outfile.write(text)
        name = outfile.name
        mainwin["basepanel"].title("%s - %s" % (name, exedit))
        outfile.close()

def openandload(widgets,state):
        new(widgets,state)
        infile = tkfile.askopenfile(mode="r")
        if infile == None: # User pressed cancel button.
                return None
        text = infile.read()
        name = infile.name
        mainwin["basepanel"].title("%s - %s" % (name, exedit))
        widgets["textarea"].insert(1.0,text)

def onchange(state):
        print "changed"
        state["unsaved changes"] = True
        if(not mainwin["basepanel"].title().endswith(" - unsaved")):
                mainwin["basepanel"].title( mainwin["basepanel"].title()+" - unsaved")
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
        mainwin["textarea"].bind("<Key>",lambda x: onchange(programstate))
        mainwin["textarea"]["wrap"] = "none"
        mainwin["textarea"].pack(fill="both",expand=1)
        mainwin["basepanel"].config(menu=mainwin["menubar"])


initComponents()

mainwin["basepanel"].title(exedit)
mainwin["basepanel"].mainloop()

