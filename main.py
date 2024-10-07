import tkinter as tk
from tkinter import ttk
import "NEA-science_GUI-calculator/infos.py" as INFO-FILE
CONSTANTS = INFO-FILE.constants_dictionary
TESTS = INFO-FILE.molecule_tests
AMINOS = INFO-FILE.amino_acids

#will use for undo and redo
class Stack:
  def __init__(self):
    self.stack = []
  
  def peek(self):
    try:
      return self.stack[-1]
    except:
      return None
  
  def push(self, value):
    self.stack.append(value)

  def pop(self):
    try:
      popped = self.stack[-1]
      self.stack.remove(self.stack[-1])
      return popped
    except:
      return None

actions_list = Stack()

class Sci_Calculator:
  def __init__(self):
    self.master = tk.Tk()
    self.master.geometry("500x500")
    self.master.state("zoomed")
    self.master.title("Science Calculator")
    self.navigation()
  def navigation(self):
    pass #display main options

gui_calc = Calculator()
gui_calc.master.mainloop()
