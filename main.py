import tkinter as tk
import math
import "NEA-science_GUI-calculator/infos.py" as INFO-FILE
CONSTANTS = INFO-FILE.constants_dictionary
TESTS = INFO-FILE.molecule_tests
AMINOS = INFO-FILE.amino_acids
VOCAB = INFO-FILE.bio_vocab

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
  def bio_menu(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
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
  
  def return_to_menu(self, frame, menu):
    frame.forget()
    returning = {"main_menu": self.main_menu(), "physics_menu": self.physics_menu(), "chem_menu", self.chem_menu, "bio_menu", self.bio_menu}
    returning[menu]
gui_calc = Sci_Calculator()
gui_calc.master.mainloop()
