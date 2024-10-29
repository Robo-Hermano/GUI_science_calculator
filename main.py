#to do list
#menu (DONE)
#normal calculator
#graphs (DONE)
#conversions (NEXT)
#constants (DONE)
#vocabulary (DONE)
#physics menu (DONE) and sub stuff: SUVAT (DONE), circuits (NEXT), rays (DONE)
#bio menu (DONE) and sub stuff: amino acids (DONE), punnett squares, cell diagrams (DONE)
#chem menu (DONE) and sub stuff: periodic table (DONE), reactivity series (DONE), ionic equations, chemical equations, balancing equations

#debugging

import tkinter as tk
from tkinter import messagebox
from tkinter.PIL import ImageTk, Image
import math
import matplotlib.pyplot as plt
from matplotlib.back_ends.backend_tkagg import FigureCanvasTkAgg
import "infos.py" as INFO_FILE
CONSTANTS = INFO_FILE.constants_dictionary
TESTS = INFO_FILE.molecule_tests
AMINOS = INFO_FILE.amino_acids
CIRCUITS = INFO_FILE.circuit_definitions

table_periodic = ImageTk.PhotoImage(Image.open("periodic_table.png")) #used for displaying periodic table
table_reactivity = ImageTk.PhotoImage(Image.open("Reactivityseriesofmetals.png")) #used for displaying periodic table
cells_image = ImageTk.PhotoImage(Image.open("cells.jpg")) #used for cell diagrams
convex_ray = ImageTk.PhotoImage(Image.open("convex.webp"))
concave_ray = ImageTk.PhotoImage(Image.open("concave.webp"))

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
    go_back = tk.Button(self.physics_frame, text = "Return to main menu", command = lambda(self.return_to_menu("main_menu", args = [self.physics_frame])))
    go_back.grid(row = 2, column = 1)

  def suvat(self):
    self.physics_frame.forget()
    self.suvat_frame = tk.Frame(self.master)
    main_label = tk.Label(self.suvat_frame, text = "Enter 3 suvat values you know, otherwise it won't be enough")
    main_label.grid(row = 0, column = 2)
    u_label = tk.Label(self.suvat_frame, text = "Enter initial speed")
    u_label.grid(row = 1, column = 0)
    self.u_text = tk.Text(self.suvat_frame)
    self.u_text.grid(row = 2, column = 0)
    v_label = tk.Label(self.suvat_frame, text = "Enter final speed")
    v_label.grid(row = 1, column = 1)
    self.v_text = tk.Text(self.suvat_frame)
    self.v_text.grid(row = 2, column = 1)
    a_label = tk.Label(self.suvat_frame, text = "Enter acceleration")
    a_label.grid(row = 1, column = 2)
    self.a_text = tk.Text(self.suvat_frame)
    self.a_text.grid(row = 2, column = 2)
    s_label = tk.Label(self.suvat_frame, text = "Enter displacement")
    s_label.grid(row = 1, column = 3)
    self.s_text = tk.Text(self.suvat_frame)
    self.s_text.grid(row = 2, column = 3)
    t_label = tk.Label(self.suvat_frame, text = "Enter time")
    t_label.grid(row = 1, column = 4)
    self.t_text = tk.Text(self.suvat_frame)
    self.t_text.grid(row = 2, column = 4)
    confirm_button = tk.Button(self.suvat_frame, text = "Enter when done", commannd = self.suvat_calculations)
    confirm_button.grid(row = 3, column = 3)
    go_back = tk.Button(self.master, text = "Return to physics menu", command = lambda(self.return_to_menu("physics_menu", args = [go_back, self.suvat_frame])))
    go_back.pack()

  def suvat_calculations(self):
    try:
      u = self.u_text.get()
      v = self.v_text.get()
      a = self.a_text.get()
      s = self.s_text.get()
      t = self.t_text.get()
      if t <= 0:
        raise ValueError("incorrect entering")
      elif u == '' and v == '':
        u = (s-(0.5*a*t**2))/t
        v = u + a*t
      elif u == '' and a == '':
        a = (v*t-s)/(t**2)
        u = v-a*t
      elif u == '' and s == '':
        u = v-a*t
        s = u*t+0.5*a*t**2
      elif u == '' and t == '':
        u = math.sqrt(v**2-2*a*s)
        t = 2*s/(v+u)
      elif v == '' and a == '':
        a = (s-u*t)/t**2
        v = u+a*t
      elif v == '' and s == '':
        v = u+a*t
        s = u*t+0.5*a*t**2
      elif v == '' and t == '':
        v = math.sqrt(u**2+2*a*s)
        t = 2*s/(v+u)
      elif a == '' and s == '':
        s = 0.5*t*(v+u)
        a = (s-u*t)/t**2
      elif a == '' and t == '':
        t = 2*s/(v+u)
        a = (s-u*t)/t**2
      elif s == '' and t == '':
        s = (v**2-u**2)/2/a
        t = 2*s/(v+u)
      show_vals = tk.Label(self.suvat_frame, text = f"inital speed: {u}, final speed: {v}, time taken: {t}, displacement: {s}, acceleration: {a}")
      show_vals.grid(row = 3, column = 2)
    except:
      error_label = tk.Label(self.suvat_frame, text = "not enough values entered or time entered incorrectly")
      error_label.grid(row = 3, column = 2)

  def ray_diagrams(self):
    self.physics_frame.forget()
    convex_img = tk.Label(self.master, img = convex_ray)
    convex_img.place(x=0, y=0, width = 200, height = 200)
    convex_informational = tk.Label(self.master, text = "If object is further away than focal point, an upside down, diminished real image will be produced. \n If not a ray will be virtually retracted and a virtual but upright and magnified image will be produced")
    convex_informational.pack(x = 250, y = 100)
    concave_img = tk.Label(self.master, img = concave_ray)
    concave_img.place(x=0, y = 210, width = 200, height = 200)
    concave_informational = tk.Label(self.master, text = "For a concave ray, the image produced has to be virtual, whether it's upright or upside down, magnified or diminished depends on how the object is placed in relation to focal points")
    concave_informational.pack(x=250, y = 310)
    go_back = tk.Button(self.master, text = "go back", command = lambda(self.return_to_menu("physics_menu", args = [convex_img, convex_informational, concave_img, concave_informational, go_back])))

  def circuit_diagrams(self):
    self.physics_frame.forget()
    self.circuit_frame = tk.Frame(self.master)
    self.img1 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("LDR.png")))
    self.img1.grid(row = 0, column = 0)
    self.button1 = tk.Button(self.circuit_frame, text = "Light Dependent Resistor", command = lambda(self.messagebox_display("Light Dependent Resistor",CIRCUITS["Light Dependent Resistor"])))
    self.button1.grid(row = 1, column = 0)
    self.img2 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("bulb.png")))
    self.img2.grid(row = 0, column = 1)
    self.button2 = tk.Button(self.circuit_frame, text = "Bulb", command = lambda(self.messagebox_display("Bulb", CIRCUITS["Bulb"])))
    self.button2.grid(row = 1, column = 1)
    self.img3 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("diode.png")))
    self.img3.grid(row = 0, column = 2)
    self.button3 = tk.Button(self.circuit_frame, text = "Diode", command = lambda(self.messagebox_display("Diode", CIRCUITS["Diode"])))
    self.button3.grid(row = 1, column = 2)
    self.img4 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("heater.png")))
    self.img4.grid(row = 0, column = 3)
    self.button4 = tk.Button(self.circuit_frame, text = "Heater", command = lambda(self.messagebox_display("Heater", CIRCUITS["Heater"])))
    self.button4.grid(row = 1, column = 3)
    self.img5 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("potentiometer.png")))
    self.img5.grid(row = 2, column = 0)
    self.button5 = tk.Button(self.circuit_frame, text = "Potentiometer", command = lambda(self.messagebox_display("Potentiometer", CIRCUITS["Potentiometer"])))
    self.button5.grid(row = 3, column = 0)
    self.img6 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("thermistor.png")))
    self.img6.grid(row = 2, column = 1)
    self.button6 = tk.Button(self.circuit_frame, text = "Thermistor", command = lambda(self.messagebox_display("Thermistor", CIRCUITS["Thermistor"])))
    self.button6.grid(row = 3, column = 1)
    
  
  def chem_menu(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.chem_frame = tk.Frame(self.master)
    display = tk.Label(self.chem_frame, text = "CHEMISTRY MENU", font = ("Times", 20))
    display.grid(row = 0, column = 1)
    self.react_series = tk.Button(self.chem_frame, text = "Reactivity Series", command = lambda(self.display_image(table_reactivity, self.chem_menu, "chem_menu")))
    self.react_series.grid(row = 1, column = 0)
    self.periodic_table = tk.Button(self.chem_frame, text = "Periodic Table", command = lambda(self.display_image(table_periodic, self.chem_menu, "chem_menu")))
    self.periodic_table.grid(row = 1, column = 1)
    self.balancing = tk.Button(self.chem_frame, text = "Balancing Equations", command = self.balance_equations)
    self.balancing.grid(row = 1, column = 2)
    self.ionic = tk.Button(self.chem_frame, text = "Ionic Equations", command = self.ionic_equations)
    self.ionic.grid(row = 2, column = 0)
    self.chemical = tk.Button(self.chem_frame, text = "Calculating Chemical equations", command = self.chemical_equations)
    self.chemical.grid(row = 2, column = 1)
    go_back = tk.Button(self.chem_frame, text = "Return to main menu", command = lambda(self.return_to_menu("main_menu", args = [self.chem_frame])))
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
    self.cells = tk.Button(self.bio_frame, text = "Animal Cell Diagram", command = lambda(self.display_image(cell_image, self.bio_frame, "bio_menu")))
    self.cells.grid(row = 1, column = 2)
    go_back = tk.Button(self.bio_frame, text = "Return to Main Menu", command = lambda(self.return_to_menu("main menu", args = [self.bio_frame])))
    go_back.grid(row = 2, column = 1)
    
  def amino_acids(self):
    self.bio_frame.forget()
    label = tk.Label(self.master, text = "Enter RNA codon")
    label.pack()
    error_label = tk.Label(self.master, text = "Invalid codon inputted")
    text = tk.Text(self.master)
    text.pack()
    button2 = tk.Button(self.master, text = "go back", command = lambda(self.return_to_menu("bio_menu", args = [label, error_label, text, button2, button])))
    button2.pack()
    try:
      button = tk.Button(self.master, text = "click here once you enter codon", command = lambda(self.messagebox_display(text.get(), AMINOS[text.get()])))
      button.pack()
    except:
      error_label.pack()
  
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
    go_back = tk.Button(self.constantframe, text = "Return to main menu", command = lambda(self.return_to_menu("main_menu", args = [self.constantframe])))
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
    go_back = tk.Button(self.vocabframe, text = "Return to main menu", command = lambda(self.return_to_menu("main_menu", args = [self.vocabframe])))
    go_back.grid(row = 5, column = 3)
  
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
    try:
      self.figure.forget()
      self.go_back.forget()
    except:
      pass
    self.x_list = []
    self.y_list = []
    self.x_label = tk.Label(self.master, text = "Enter x value")
    self.x_label.pack()
    self.x_value = tk.Text(self.master)
    self.x_value.pack()
    self.y_label = tk.Label(self.master, text = "Enter y value")
    self.y_label.pack()
    self.y_value = tk.Text(self.master)
    self.y_value.pack()
    self.graph_errors = tk.Label(self.master, text = "Return to menu and come back to reset x and y")
    self.graph_errors.pack()
    self.record_button = tk.Button(self.master, text = "Record values", command = self.record_values_for_graph)
    self.record_button.pack()
    self.graph_button = tk.Button(self.master, text = "Draw graph from entered data", command = self.display_graph)
    self.graph_button.pack()
    self.go_back = tk.Button(self.master, text = "Return to main menu", command = lambda(self.return_to_menu("main_menu", args = [self.x_label, self.x_value, self.y_label, self.y_value, self.record_button, self.graph_button, self.graph_errors, self.go_back])))
    self.go_back.pack()

  def record_values_for_graph(self)
    try:
      x_val = self.x_value.get()
      y_val = self.y_value.get()
      x_val = float(x_val)
      y_val = float(y_val)
      self.x_list.append(x_val)
      self.y_list.append(y_val)
    except:
      self.graphs_errors.config(text = "Please input valid data for both x and y")

  def display_graph(self):
    self.x_label.forget()
    self.y_label.forget()
    self.x_value.forget()
    self.y_value.forget()
    self.graph_errors.forget()
    self.record_button.forget()
    self.graph_button.forget()
    self.go_back.forget()
    self.figure = plt.Figure(figsize = (50,50), dpi = 100)
    self.ax = self.figure.add_subplot(111)
    self.canvas = FigureCanvasTkAgg(self.figure, master=self)
    self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    for i in range(len(self.x_list)):
      self.ax.plot(self.x_list[i], self.y_list[i])
    self.canvas.draw()
    self.go_back = tk.Button(self.master, text = "go back", command = self.data_graphs)
    self.go_back.pack(side = tk.BOTTOM, pady = 10)

  def dislay_image(self, img, frame, menu):
    frame.forget()
    my_img = tk.Label(self.master, image = img)
    my_img.place(x=0, y=0, width = 500, height = 400)
    return_button = tk.Button(self.master, text = "Go back", command = lambda(self.return_to_menu(menu, args = [my_img, return_button])))
    return_button.pack(x = 250, y = 450)

  def messagebox_display(self, key, value):
    messagebox.showinfo(f"{key}: {value}")
  
  def return_to_menu(self, chosen_menu, args):
    for i in args:
      i.forget()
    returning_nav = {"main_menu": self.main_menu(), "physics_menu": self.physics_menu(), "chem_menu", self.chem_menu, "bio_menu", self.bio_menu}
    returning_nav[chosen_menu]
    
gui_calc = Sci_Calculator()
gui_calc.master.mainloop()
