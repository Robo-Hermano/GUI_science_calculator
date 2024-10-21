#to do list
#calculate
#graphs
#conversions
#physics sub stuff: SUVAT, circuits, rays
#bio sub stuff: amino acids, punnett squares, cell diagrams
#chem sub stuff: periodic table, reactivity series, ionic equations, chemical equations, balancing equations

import tkinter as tk
from tkinter import messagebox
from tkinter.PIL import ImageTk, Image
import math
import numpy as np
import "NEA-science_GUI-calculator/infos.py" as INFO_FILE
CONSTANTS = INFO_FILE.constants_dictionary
TESTS = INFO_FILE.molecule_tests
AMINOS = INFO_FILE.amino_acids

table = ImageTk.PhotoImage(Image.open("periodic_table.png")) #used for displaying periodic table

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
    self.main_menu()

  
  def main_menu(self):
    self.intro = tk.Label(self.master, text = "MAIN MENU", font = ("Times", 20))
    self.intro.pack()
    self.buttonframe = tk.Frame(self.master)
    self.physics = tk.Button(self.buttonframe, text = "Physics", command = self.physics_menu)
    self.physics.grid(row = 0, column = 0)
    self.chemistry = tk.Button(self.buttonframe, text = "Chemistry", command = self.chem_menu)
    self.chemistry.grid(row = 0, column = 1)
    self.biology = tk.Button(self.buttonframe, text = "Biology", command = self.bio_menu)
    self.biology.grid(row = 0, column = 2)
    self.operations = tk.Button(self.buttonframe, text = "Operations", command = self.calculations)
    self.operations.grid(row = 1, column = 0)
    self.constants = tk.Button(self.buttonframe, text = "Display Constants", command = self.display_constants)
    self.constants.grid(row = 1, column = 1)
    self.units = tk.Button(self.buttonframe, text = "Convert Units", command = self.conversions)
    self.units.grid(row = 1, column = 2)
    self.tests = tk.Button(self.buttonframe, text = "Tests for molecules and substances", command = self.vocabulary)
    self.tests.grid(row = 2, column = 0)
    self.graphs = tk.Button(self.buttonframe, text = "Datasheet and Graphs", command = self.data_graphs)
    self.graphs.grid(row = 2, column = 1)

  
  def physics_menu(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.physics_frame = tk.Frame(self.master)
    display = tk.Label(self.physics_frame, text = "PHYSICS MENU", font = ("Times", 20))
    display.grid(row = 0, column = 1)
    self.suvat_calcs = tk.Button(self.physics_frame, text = "S.U.V.A.T. calculations", command = self.suvat)
    self.suvat_calcs.grid(row = 1, column = 0)
    self.rays = tk.Button(self.physics_frame, text = "Ray diagrams", command = self.ray_diagrams)
    self.rays.grid(row = 1, column = 1)
    self.circuits = tk.Button(self.physics_frame, text = "Circuit diagrams", command = self.circuit_diagrams)
    self.circuits.grid(row = 1, column = 2)
    go_back = tk.Button(self.physics_frame, text = "Return to main menu", command = lambda(self.return_to_menu(self.physics_frame, "main_menu")))
    go_back.grid(row = 2, column = 1)


  
  def chem_menu(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.chem_frame = tk.Frame(self.master)
    display = tk.Label(self.chem_frame, text = "CHEMISTRY MENU", font = ("Times", 20))
    display.grid(row = 0, column = 1)
    self.react_series = tk.Button(self.chem_frame, text = "Reactivity Series", command = self.reactivity)
    self.react_series.grid(row = 1, column = 0)
    self.periodic_table = tk.Button(self.chem_frame, text = "Periodic Table", command = self.display_periodic_table)
    self.periodic_table.grid(row = 1, column = 1)
    self.balancing = tk.Button(self.chem_frame, text = "Balancing Equations", command = self.balance_equations)
    self.balancing.grid(row = 1, column = 2)
    self.ionic = tk.Button(self.chem_frame, text = "Ionic Equations", command = self.ionic_equations)
    self.ionic.grid(row = 2, column = 0)
    self.chemical = tk.Button(self.chem_frame, text = "Calculating Chemical equations", command = self.chemical_equations)
    self.chemical.grid(row = 2, column = 1)
    go_back = tk.Button(self.chem_frame, text = "Return to main menu", command = lambda(self.return_to_menu(self.chem_frame, "main_menu")))
    go_back.grid(row = 2, column = 2)


  
  def bio_menu(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.bio_frame = tk.Frame(self.master)
    display = tk.Label(self.bio_frame, text = "BIOLOGY MENU", font = ("Times", 20))
    display.grid(row = 0, column = 0)
    self.punnett = tk.Button(self.bio_frame, text = "Punnett Squares", command = self.punnett_squares)
    self.punnett.grid(row = 1, column = 0)
    self.aminos = tk.Button(self.bio_frame, text = "Amino Acids", command = self.amino_acids)
    self.aminos.grid(row = 1, column = 1)
    self.cells = tk.Button(self.bio_frame, text = "Cell Diagrams", command = self.cell_diagrams)
    self.cells.grid(row = 1, column = 2)
    go_back = tk.Button(self.bio_frame, text = "Return to Main Menu", command = lambda(self.return_to_menu(self.bio_frame, "main menu")))
    go_back.grid(row = 2, column = 1)
    
  
  
  def calculations(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass

  
  def display_constants(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.constantframe = tk.Frame(self.master)
    constant_names = CONSTANTS.keys()
    constant_values = CONSTANTS.values()
    for i in range(6):
      for j in range(6):
        constant = tk.Button(self.constantframe, text = constant_names[i+j], command = lambda(self.messagebox_display(constant_names[i+j],constant_values[i+j])))
        constant.grid(row = i, column = j)
    go_back = tk.Button(self.constantframe, text = "Return to main menu", command = lambda(self.return_to_menu(self.constantframe, "main_menu")))
    go_back.grid(row = 6, column = 3)

  def vocabulary(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.vocabframe = tk.Frame(self.master)
    test_types = TESTS.keys()
    test_descriptions = TESTS.values()
    for i in range(4):
      for j in range(5):
        test = tk.Button(self.vocabframe, text = test_types[i+j], command = lambda(self.messagebox_display(test_types[i+j],test_descriptions[i+j])))
        test.grid(row = i, column = j)
    go_back = tk.Button(self.vocabframe, text = "Return to main menu", command = lambda(self.return_to_menu(self.vocabframe, "main_menu")))
    go_back.grid(row = 5, column = 3)
    

  def messagebox_display(self, key, value):
    messagebox.showinfo(f"{key}: {value}")
  
  def conversions(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass

  
  def data_graphs(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass

  
  
  def return_to_menu(self, frame, chosen_menu):
    frame.forget()
    returning_nav = {"main_menu": self.main_menu(), "physics_menu": self.physics_menu(), "chem_menu", self.chem_menu, "bio_menu", self.bio_menu}
    returning_nav[chosen_menu]
    
gui_calc = Sci_Calculator()
gui_calc.master.mainloop()
