#to do list: a LOT of debugging (especially on calculator)

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
sys.path.append("/GUI_science_calculator/infos.py")
import infos as INFO_FILE

CONSTANTS, AMINOS, CIRCUITS, TESTS = INFO_FILE.get_infos()

table_periodic = ImageTk.PhotoImage(Image.open("periodic_table.png")) #used for displaying periodic table
table_reactivity = ImageTk.PhotoImage(Image.open("Reactivityseriesofmetals.png")) #used for displaying periodic table
cells_image = ImageTk.PhotoImage(Image.open("cells.jpg")) #used for cell diagrams
convex_ray = ImageTk.PhotoImage(Image.open("convex.webp")) #used for ray diagrams
concave_ray = ImageTk.PhotoImage(Image.open("concave.webp")) #used for ray diagrams

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
      self.stack.remove(self.stack[-1])
    except:
      pass
  def view(self):
    return "".join(self.stack)
    
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
    go_back = tk.Button(self.physics_frame, text = "Return to main menu", command = lambda:self.return_to_menu("main_menu", args = [self.physics_frame]))
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
    go_back = tk.Button(self.master, text = "Return to physics menu", command = lambda:self.return_to_menu("physics_menu", args = [go_back, self.suvat_frame]))
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
    go_back = tk.Button(self.master, text = "go back", command = lambda:self.return_to_menu("physics_menu", args = [convex_img, convex_informational, concave_img, concave_informational, go_back]))

  def circuit_diagrams(self):
    self.physics_frame.forget()
    self.circuit_frame = tk.Frame(self.master)
    self.img1 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("LDR.png")))
    self.img1.grid(row = 0, column = 0)
    self.button1 = tk.Button(self.circuit_frame, text = "Light Dependent Resistor", command = lambda:self.messagebox_display("Light Dependent Resistor",CIRCUITS["Light Dependent Resistor"]))
    self.button1.grid(row = 1, column = 0)
    self.img2 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("bulb.png")))
    self.img2.grid(row = 0, column = 1)
    self.button2 = tk.Button(self.circuit_frame, text = "Bulb", command = lambda:self.messagebox_display("Bulb", CIRCUITS["Bulb"]))
    self.button2.grid(row = 1, column = 1)
    self.img3 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("diode.png")))
    self.img3.grid(row = 0, column = 2)
    self.button3 = tk.Button(self.circuit_frame, text = "Diode", command = lambda:self.messagebox_display("Diode", CIRCUITS["Diode"]))
    self.button3.grid(row = 1, column = 2)
    self.img4 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("heater.png")))
    self.img4.grid(row = 0, column = 3)
    self.button4 = tk.Button(self.circuit_frame, text = "Heater", command = lambda:self.messagebox_display("Heater", CIRCUITS["Heater"]))
    self.button4.grid(row = 1, column = 3)
    self.img5 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("potentiometer.png")))
    self.img5.grid(row = 2, column = 0)
    self.button5 = tk.Button(self.circuit_frame, text = "Potentiometer", command = lambda:self.messagebox_display("Potentiometer", CIRCUITS["Potentiometer"]))
    self.button5.grid(row = 3, column = 0)
    self.img6 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("thermistor.png")))
    self.img6.grid(row = 2, column = 1)
    self.button6 = tk.Button(self.circuit_frame, text = "Thermistor", command = lambda:self.messagebox_display("Thermistor", CIRCUITS["Thermistor"]))
    self.button6.grid(row = 3, column = 1)
    self.img7 = tk.Label(self.circuit_frame, img = ImageTk.PhotoImage(Image.open("variable_resistor.png")))
    self.img7.grid(row = 2, column = 2)
    self.button7 = tk.Button(self.circuit_frame, text = "Variable Resistor", command = lambda:self.messagebox_display("Variable Resistor", CIRCUITS["Variable Resistor"]))
    self.button7.grid(row = 3, column = 2)
    go_back = tk.Button(self.circuits_frame, text = "Go back", command = lambda:self.return_to_menu("physics_menu", args = [self.circuit_frame]))
    go_back.grid(row = 3, column = 3)
  
  def chem_menu(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.chem_frame = tk.Frame(self.master)
    display = tk.Label(self.chem_frame, text = "CHEMISTRY MENU", font = ("Times", 20))
    display.grid(row = 0, column = 1)
    self.react_series = tk.Button(self.chem_frame, text = "Reactivity Series", command = lambda:self.display_image(table_reactivity, self.chem_menu, "chem_menu"))
    self.react_series.grid(row = 1, column = 0)
    self.periodic_table = tk.Button(self.chem_frame, text = "Periodic Table", command = lambda:self.display_image(table_periodic, self.chem_menu, "chem_menu"))
    self.periodic_table.grid(row = 1, column = 1)
    self.ionic = tk.Button(self.chem_frame, text = "Ionic Equations (COMING SOON)")
    self.ionic.grid(row = 1, column = 2)
    go_back = tk.Button(self.chem_frame, text = "Return to main menu", command = lambda:self.return_to_menu("main_menu", args = [self.chem_frame]))
    go_back.grid(row = 2, column = 1)
  
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
    self.cells = tk.Button(self.bio_frame, text = "Animal Cell Diagram", command = lambda:self.display_image(cells_image, self.bio_frame, "bio_menu"))
    self.cells.grid(row = 1, column = 2)
    go_back = tk.Button(self.bio_frame, text = "Return to Main Menu", command = lambda:self.return_to_menu("main menu", args = [self.bio_frame]))
    go_back.grid(row = 2, column = 1)
    
  def amino_acids(self):
    self.bio_frame.forget()
    label = tk.Label(self.master, text = "Enter RNA codon")
    label.pack()
    error_label = tk.Label(self.master, text = "Invalid codon inputted")
    text = tk.Text(self.master)
    text.pack()
    button2 = tk.Button(self.master, text = "go back", command = lambda:self.return_to_menu("bio_menu", args = [label, error_label, text, button2, button]))
    button2.pack()
    try:
      button = tk.Button(self.master, text = "click here once you enter codon", command = lambda:self.messagebox_display(text.get(), AMINOS[text.get()]))
      button.pack()
    except:
      error_label.pack()

  def punnett_squares(self):
    self.bio_frame.forget()
    self.punnett_frame = tk.Frame(self.master)
    explain_label = tk.Label(self.punnett_frame, text = "Fill out alleles of parents")
    explain_label.grid(row = 0, column = 0)
    self.father_one = tk.Text(self.punnett_frame)
    self.father_one.grid(row = 0, column = 1)
    self.father_two = tk.Text(self.punnett_frame)
    self.father_two.grid(row = 0, column = 2)
    self.mother_one = tk.Text(self.punnett_frame)
    self.mother_one.grid(row = 1, column = 0)
    self.mother_two = tk.Text(self.punnett_frame)
    self.mother_two.grid(row = 2, column = 0)
    self.genotype_one = tk.Button(self.punnett_frame, text = "Genotype One", command = None)
    self.genotype_one.grid(row = 1, column = 1)
    self.genotype_two = tk.Button(self.punnett_frame, text = "Genotype Two", command = None)
    self.genotype_two.grid(row = 1, column = 2)
    self.genotype_three = tk.Button(self.punnett_frame, text = "Genotype Three", command = None)
    self.genotype_three.grid(row = 2, column = 1)
    self.genotype_four = tk.Button(self.punnett_frame, text = "Genotype Four", command = None)
    self.genotype_four.grid(row = 2, column = 2)
    self.geno_button = tk.Button(self.punnett_frame, text = "Get possible Genotypes", command = self.get_genotypes)
    self.geno_button.grid(row = 3, column = 0)
    go_back = tk.Button(self.punnett_frame, text = "Return to Biology Menu", command = lambda:self.return_to_menu("bio_menu", args = [self.punnett_frame]))
    go_back.grid(row = 3, column = 1)

  def get_genotypes(self):
    father_one = self.father_one.get()
    father_two = self.father_two.get()
    mother_one = self.mother_one.get()
    mother_two = self.mother_two.get()
    if father_one.upper() == father_two.upper() and father_one.upper() == mother_one.upper() and father_one.upper() == mother_two.upper() and father_one.isalpha() and len(father_one) == 1:
      self.genotype_one.config(text = sorted(father_one + mother_one))
      self.genotype_two.config(text = sorted(father_two + mother_one))
      self.genotype_three.config(text = sorted(father_one + mother_two))
      self.genotype_four.config(text = sorted(father_two + mother_two))
    else:
      self.geno_button.config(text = "Alleles entered are invalid")
    
  def calculations(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    messagebox.showinfo("second value if it's there is what is used after you press shift")
    self.action_list = Stack()
    self.output_frame = tk.Frame(self.master, side = tk.TOP())
    self.calc_frame = tk.Frame(self.master, side = tk.BOTTOM())
    self.output_label = tk.Label(self.output_frame)
    self.output_label.pack(expand = True)
    #button time
    go_back = tk.Button(self.calc_frame, text = "EXIT", command = lambda:self.return_to_menu("main_menu", args = [self.output_frame, self.calc_frame]))
    go_back.grid(row = 0, column = 0)
    self.shift_button = tk.Button(self.calc_frame, text = "shift", command = lambda:self.implement_button(self.shift_button))
    self.shift_button.grid(row = 0, column = 1)
    self.shift_on = False
    self.log_button = tk.Button(self.calc_frame, text = "log", command = lambda:self.implement_button("math.log"))
    self.log_button.grid(row = 0, column = 2)
    self.ln_button = tk.Button(self.calc_frame, text = "ln//e", command = lambda:self.implement_button(self.ln_button))
    self.ln_button.grid(row = 0, column = 3)
    self.sin_button = tk.Button(self.calc_frame, text = "sin//sin^-1", command = lambda:self.implement_button(self.sin_button))
    self.sin_button.grid(row = 0, column = 4)
    self.cos_button = tk.Button(self.calc_frame, text = "cos//cos^-1", command = lambda:self.implement_button(self.cos_button))
    self.cos_button.grid(row = 1, column = 0)
    self.tan_button = tk.Button(self.calc_frame, text = "tan//tan^-1", command = lambda:self.implement_button(self.tan_button))
    self.tan_button.grid(row = 1, column = 1)
    self.bracket_one = tk.Button(self.calc_frame, text = "(", command = lambda:self.implement_button("("))
    self.bracket_one.grid(row = 1, column = 2)                        
    self.bracket_two = tk.Button(self.calc_frame, text = ")", command = lambda:self.implement_button(")"))
    self.bracket_two.grid(row = 1, column = 3)
    self.power_button = tk.Button(self.calc_frame, text = "^", command = lambda:self.implement_button("**"))
    self.power_button.grid(row = 1, column = 4)
    self.seven_button = tk.Button(self.calc_frame, text = "7", command = lambda:self.implement_button("7"))
    self.seven_button.grid(row = 2, column = 0)
    self.eight_button = tk.Button(self.calc_frame, text = "8", command = lambda:self.implement_button("8"))
    self.eight_button.grid(row = 2, column = 1)
    self.nine_button = tk.Button(self.calc_frame, text = "9", command = lambda:self.implement_button("9"))
    self.nine_button.grid(row = 2, column = 2)
    self.undo_button = tk.Button(self.calc_frame, text = "UNDO", command = lambda:self.implement_button(self.undo_button))
    self.undo_button.grid(row = 2, column = 3)
    self.ac_button = tk.Button(self.calc_frame, text = "AC", command = lambda:self.implement_button(self.ac_button))
    self.ac_button.grid(row = 2, column = 4)
    self.four_button = tk.Button(self.calc_frame, text = "4", command = lambda:self.implement_button("4"))
    self.four_button.grid(row = 3, column = 0)
    self.five_button = tk.Button(self.calc_frame, text = "5", command = lambda:self.implement_button("5"))
    self.five_button.grid(row = 3, column = 1)
    self.six_button = tk.Button(self.calc_frame, text = "6", command = lambda:self.implement_button("6"))
    self.six_button.grid(row = 3, column = 2)
    self.multiply_button = tk.Button(self.calc_frame, text = "X", command = lambda:self.implement_button("*"))
    self.multiply_button.grid(row = 3, column = 3)
    self.divide_button = tk.Button(self.calc_frame, text = "/", command = lambda:self.implement_button("/"))
    self.divide_button.grid(row = 3, column = 4)
    self.one_button = tk.Button(self.calc_frame, text = "1", command = lambda:self.implement_button("1"))
    self.one_button.grid(row = 4, column = 0)
    self.two_button = tk.Button(self.calc_frame, text = "2", command = lambda:self.implement_button("2"))
    self.two_button.grid(row = 4, column = 1)
    self.three_button = tk.Button(self.calc_frame, text = "3", command = lambda:self.implement_button("3"))
    self.three_button.grid(row = 4, column = 2)
    self.plus_button = tk.Button(self.calc_frame, text = "+", command = lambda:self.implement_button("+"))
    self.plus_button.grid(row = 4, column = 3)
    self.minus_button = tk.Button(self.calc_frame, text = "-", command = lambda:self.implement_button("-"))
    self.minus_button.grid(row = 4, column = 4)
    self.zero_button = tk.Button(self.calc_frame, text = "0", command = lambda:self.implement_button("0"))
    self.zero_button.grid(row = 5, column = 1)
    self.decimal_button = tk.Button(self.calc_frame, text = ".", command = lambda:self.implement_button("."))
    self.decimal_button.grid(row = 5, column = 2)
    self.equals_button = tk.Button(self.calc_frame, text = "=", command = lambda:self.implement_button(self.equals_button))
    self.equals_button.grid(row = 5, column = 3)
  
  def implement_button(self, button_clicked):
    if button_clicked == self.shift_button:
      if self.shift_on:
        self.shift_on = False
      else:
        self.shift_on = True
    elif button_clicked == self.undo_button:
      self.action_list.pop()
    elif button_clicked == self.ac_button:
      while self.action_list.peek() != None:
        self.action_list.pop()
    elif button_clicked == self.ln_button:
      if self.shift_on:
        self.action_list.push("e")
      else:
        self.action_list.push("math.ln")
    elif button_clicked == self.sin_button:
      if self.shift_on:
        self.action_list.push("np.arcsin")
      else:
        self.action_list.push("math.sin")
    elif button_clicked == self.cos_button:
      if self.shift_on:
        self.action_list.push("np.arccos")
      else:
        self.action_list.push("math.cos")
    elif button_clicked == self.tan_button:
      if self.shift_on:
        self.action_list.push("np.arctan")
      else:
        self.action_list.push("math.tan")
    elif button_clicked == self.equals_button:
      operand_list = []
      while self.action_list.peek() != None:
        operand_list.append(self.action_list.peek())
        self.action_list.pop()
      operand_list = operand_list[::-1]
      self.action_list = [eval(''.join(operand_list))]
    else:
      self.action_list.push(button_clicked)
    self.output_label.config(text = self.action_list.view())
    
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
        constant = tk.Button(self.constantframe, text = constant_names[i+j], command = lambda:self.messagebox_display(constant_names[i+j],constant_values[i+j]))
        constant.grid(row = i, column = j)
    go_back = tk.Button(self.constantframe, text = "Return to main menu", command = lambda:self.return_to_menu("main_menu", args = [self.constantframe]))
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
        test = tk.Button(self.vocabframe, text = test_types[i+j], command = lambda:self.messagebox_display(test_types[i+j],test_descriptions[i+j]))
        test.grid(row = i, column = j)
    go_back = tk.Button(self.vocabframe, text = "Return to main menu", command = lambda:self.return_to_menu("main_menu", args = [self.vocabframe]))
    go_back.grid(row = 5, column = 3)
  
  def conversions(self):
    try:
      self.buttonframe.forget()
      self.intro.forget()
    except:
      pass
    self.length = {"m": 1, "cm": 0.01, "mm": 0.001, "um": 10**-6, "nm": 10**-9, "km": 1000}
    self.time = {"s": 1, "m": 60, "h": 3600, "d": 3600*24, "ms": 0.001}
    self.volume = {"l": 1, "ml": 0.001}
    self.conversion_frame = tk.Frame(self.master)
    label1 = tk.Label(self.conversion_frame, text = "Enter value")
    label1.grid(row = 0, column = 1)
    label2 = tk.Label(self.conversion_frame, text = "Enter unit")
    label2.grid(row = 0, column = 2)
    text1 = tk.Text(self.conversion_frame)
    text1.grid(row = 1, column = 1)
    text2 = tk.Text(self.conversion_frame)
    text2.grid(row = 1, column = 2)
    label3 = tk.Label(self.conversion_frame, text = "Enter unit converted to")
    label3.grid(row = 2, column = 2)
    text3 = tk.Label(self.conversion_frame)
    text3.grid(row = 3, column = 2)
    self.conversion_button = tk.Button(self.conversion_frame, text = "Click once you're ready to convert", command = lambda:self.convert(text1, text2, text3))
    self.conversion_button.grid(row = 0, column = 0)
    go_back = tk.Button(self.vocabframe, text = "Return to main menu", command = lambda:self.return_to_menu("main_menu", args = [self.conversion_frame]))
    go_back.grid(row = 2, column = 1)
  
  def convert(self, input_val, input_unit, converted_unit):
    val = input_val.get()
    unit1 = input_unit.get()
    unit2 = converted_unit.get()
    try:
      if unit1 in self.length.keys() or unit1 in self.time.keys() or unit1 in self.volume.keys():
        new_val = val*self.length[unit1]/self.length[unit2]
      elif unit1 == "K" and unit2 == "C":
        new_val = val - 273.15
      elif unit1 == "C" and unit2 == "K":
        new_val = val + 273.15
      elif unit1 == "C" and unit2 == "F":
        new_val = val*1.8+32
      elif unit1 == "K" and unit2 == "F":
        new_val = (val-273.15)*1.8+32
      elif unit1 == "F" and unit2 == "C":
        new_val = (val-32)/1.8
      elif unit1 == "F" and unit2 == "K":
        new_val = (val-32)/1.8+273.15
      else:
        raise ValueError()
      self.messagebox_display("Value in new unit", new_val)
    except:
      self.conversion_button.config(text = "Sorry. Your units are either not in conversion dictionary or an input entered is invalid")
  
  
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
    self.go_back = tk.Button(self.master, text = "Return to main menu", command = lambda:self.return_to_menu("main_menu", args = [self.x_label, self.x_value, self.y_label, self.y_value, self.record_button, self.graph_button, self.graph_errors, self.go_back]))
    self.go_back.pack()

  def record_values_for_graph(self):
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
    return_button = tk.Button(self.master, text = "Go back", command = lambda:self.return_to_menu(menu, args = [my_img, return_button]))
    return_button.pack(x = 250, y = 450)

  def messagebox_display(self, key, value):
    messagebox.showinfo(f"{key}: {value}")
  
  def return_to_menu(self, chosen_menu, args):
    for i in args:
      i.forget()
    returning_nav = {"main_menu": self.main_menu(), "physics_menu": self.physics_menu(), "chem_menu": self.chem_menu, "bio_menu": self.bio_menu}
    returning_nav[chosen_menu]
    
gui_calc = Sci_Calculator()
gui_calc.master.mainloop()
