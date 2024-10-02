import tkinter as tk
from tkinter import ttk
import "NEA-science_GUI-calculator/infos.py" as INFO-FILE
CONSTANTS = INFO-FILE.constants_dictionary
TESTS = INFO-FILE.molecule_tests
AMINOS = INFO-FILE.amino_acids

class Calculator:
  def __init__(self):
    master = tk.Tk()
