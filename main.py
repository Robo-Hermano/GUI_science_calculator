import tkinter as tk
from tkinter import ttk
import "NEA-science_GUI-calculator/infos.py" as INFO-FILE
CONSTANTS = INFO-FILE.constants_dictionary
TESTS = INFO-FILE.molecule_tests
AMINOS = INFO-FILE.amino_acids

class Stack: #for undo and redo
  def peek(self, value):
    return self[len(self)-1]
  
  def push(self, value):
    self = self.append(value)
    return self

  def pop(self):
    self = self.remove(self[len(self)-1])
    return self

class Calculator:
  def __init__(self):
    master = tk.Tk()
