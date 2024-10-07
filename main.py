import tkinter as tk
from tkinter import ttk
import "NEA-science_GUI-calculator/infos.py" as INFO-FILE
CONSTANTS = INFO-FILE.constants_dictionary
TESTS = INFO-FILE.molecule_tests
AMINOS = INFO-FILE.amino_acids

#might use for undo and redo
#class Stack:
  #def peek(self):
  #  return self[len(self)-1]
  
  #def push(self, value):
  #  self = self.append(value)
  #  return self

  #def pop(self):
  #  self = self.remove(self[len(self)-1])
  #  return self

class Sci_Calculator:
  def __init__(self):
    self.master = tk.Tk()
    self.master.geometry("500x500")
    self.master.state("zoomed")
    self.master.title("Science Calculator")
    self.navigation
  def navigation(self):
    pass #display main options

gui_calc = Calculator()
gui_calc.master.mainloop()
