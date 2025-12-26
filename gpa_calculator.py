from tkinter import *
import customtkinter as ctk
root = ctk.CTk()
root.geometry("650x650")
root.title("GPA_Calculator")
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")
label1 = ctk.CTkLabel(root, text="Select your Semester:", font=("Helvetica", 16, "bold"))
label1.pack(pady=(30, 10))
semesters = ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5"]


semester_menu = ctk.CTkOptionMenu(root, values=semesters)
semester_menu.pack(pady=10)
def semester_one():
    Theory_subjects = ["MF :", "DP :", "WP :", "C :", "COM :"]
    T_grades = {}
    TLabel= ctk.CTkLabel(root, text="Theory Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Theory_subjects:
        lbl = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333",       
    border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        T_grades[subject] = e

    Lab_subjects = ["COM :", "WP :", "C :"]
    L_grades = {}
    LLabel= ctk.CTkLabel(root, text="Lab Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Lab_subjects:
        LLabel = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333", border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        L_grades[subject] = e

    def calculate_gpa():
        theory_total = 0
        lab_total = 0
        for subject, entry in T_grades.items():
            theory_total += int(entry.get()) * 4

    
        for subject, entry in L_grades.items():
            lab_total += int(entry.get()) * 2

        result = (theory_total + lab_total) / 26

        for widget in root.winfo_children():
            widget.destroy()
        flbl = ctk.CTkLabel(root, text=f"Final GPA: {result:.2f}", font=("Arial", 18))
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        flbl.grid(row=0, column=0)

    space = ctk.CTkLabel(root, text=" ").pack()
    sub = ctk.CTkButton(root, text="Submit", command=calculate_gpa).pack()
def semester_two():
    Theory_subjects = ["FPS :", "OOPS :", "CA :", "DS :", "CN :"]
    T_grades = {}
    TLabel= ctk.CTkLabel(root, text="Theory Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Theory_subjects:
        lbl = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333",       
    border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        T_grades[subject] = e

    Lab_subjects = ["OOPS :", "DS :", "IT :"]
    L_grades = {}
    LLabel= ctk.CTkLabel(root, text="Lab Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Lab_subjects:
        LLabel = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333", border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        L_grades[subject] = e

    def calculate_gpa():
        theory_total = 0
        lab_total = 0
        for subject, entry in T_grades.items():
            theory_total += int(entry.get()) * 4

    
        for subject, entry in L_grades.items():
            lab_total += int(entry.get()) * 2

        result = (theory_total + lab_total) / 26

        for widget in root.winfo_children():
            widget.destroy()
        flbl = ctk.CTkLabel(root, text=f"Final GPA: {result:.2f}", font=("Arial", 18))
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        flbl.grid(row=0, column=0)

    space = ctk.CTkLabel(root, text=" ").pack()
    sub = ctk.CTkButton(root, text="Submit", command=calculate_gpa).pack()
    Lab_subjects = ["OOPS", "CN", "EC"]
def semester_three():
    Theory_subjects = [ "AM :", "JAVA :", "EVS :", "OS :", "DD :" ]
    T_grades = {}
    TLabel= ctk.CTkLabel(root, text="Theory Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Theory_subjects:
        lbl = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333",       
    border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        T_grades[subject] = e

    Lab_subjects = ["JAVA :", "OS :", "DD :"]
    L_grades = {}
    LLabel= ctk.CTkLabel(root, text="Lab Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Lab_subjects:
        LLabel = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333", border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        L_grades[subject] = e

    def calculate_gpa():
        theory_total = 0
        lab_total = 0
        for subject, entry in T_grades.items():
            theory_total += int(entry.get()) * 4

    
        for subject, entry in L_grades.items():
            lab_total += int(entry.get()) * 2

        result = (theory_total + lab_total) / 26

        for widget in root.winfo_children():
            widget.destroy()
        flbl = ctk.CTkLabel(root, text=f"Final GPA: {result:.2f}", font=("Arial", 18))
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        flbl.grid(row=0, column=0)

    space = ctk.CTkLabel(root, text=" ").pack()
    sub = ctk.CTkButton(root, text="Submit", command=calculate_gpa).pack()
def semester_four():
    Theory_subjects = [ "DCC :", "NS :", "SE :", "Python :", "AI :" ]
    T_grades = {}
    TLabel= ctk.CTkLabel(root, text="Theory Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Theory_subjects:
        lbl = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333",       
    border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        T_grades[subject] = e

    Lab_subjects = ["NS", "SE", "PY"]
    L_grades = {}
    LLabel= ctk.CTkLabel(root, text="Lab Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Lab_subjects:
        LLabel = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333", border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        L_grades[subject] = e

    def calculate_gpa():
        theory_total = 0
        lab_total = 0
        for subject, entry in T_grades.items():
            theory_total += int(entry.get()) * 4

    
        for subject, entry in L_grades.items():
            lab_total += int(entry.get()) * 2

        result = (theory_total + lab_total) / 26

        for widget in root.winfo_children():
            widget.destroy()
        flbl = ctk.CTkLabel(root, text=f"Final GPA: {result:.2f}", font=("Arial", 18))
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        flbl.grid(row=0, column=0)

    space = ctk.CTkLabel(root, text=" ").pack()
    sub = ctk.CTkButton(root, text="Submit", command=calculate_gpa).pack()
def semester_five():
    Theory_subjects = ["ASP.NET :", "UNIX :", "OOSD :", "SQT :", "DM :"]
    T_grades = {}
    TLabel= ctk.CTkLabel(root, text="Theory Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Theory_subjects:
        lbl = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333",       
    border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        T_grades[subject] = e

    Lab_subjects = ["ASP.NET :", "UNIX :", "OOSD :"]
    L_grades = {}
    LLabel= ctk.CTkLabel(root, text="Lab Subjects", font=("Helvetica", 15, "bold" )).pack()
    for subject in Lab_subjects:
        LLabel = ctk.CTkLabel(root, text=subject, font=("Times", 13, "bold"), text_color="#E3E1E1").pack()
        e = ctk.CTkEntry(root, fg_color="#333333", border_color="#113E71",   
    text_color="white",       
    corner_radius=60, font=("Arial", 14))
        e.pack()
        L_grades[subject] = e

    def calculate_gpa():
        theory_total = 0
        lab_total = 0
        for subject, entry in T_grades.items():
            theory_total += int(entry.get()) * 4

    
        for subject, entry in L_grades.items():
            lab_total += int(entry.get()) * 2

        result = (theory_total + lab_total) / 26

        for widget in root.winfo_children():
            widget.destroy()
        flbl = ctk.CTkLabel(root, text=f"Final GPA: {result:.2f}", font=("Arial", 18))
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        flbl.grid(row=0, column=0)

    space = ctk.CTkLabel(root, text=" ").pack()
    sub = ctk.CTkButton(root, text="Submit", command=calculate_gpa).pack()
menu_actions = {
    "Semester 1" : semester_one,
    "Semester 2" : semester_two,
    "Semester 3" : semester_three,
    "Semester 4" : semester_four,
    "Semester 5" : semester_five
}
    
def on_button_click():
    label1.destroy()
    semester_menu.destroy()
    ok_button.destroy()


    user_choice = semester_menu.get()
    action = menu_actions.get(user_choice)
    if action:
        action()
    
ok_button = ctk.CTkButton(root, text="OK", command=on_button_click)
ok_button.pack(pady=20)
root.mainloop()







