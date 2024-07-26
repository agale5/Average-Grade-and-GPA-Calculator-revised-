import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import ImageTk, Image

#This method sets the instance, which instantiates the object).
class GradingCalculator:
    def __init__(self, root):
        #Displays title at the top for the entry box.
        self.root = root
        self.root.title("Average Grade and GPA Calculator")
       
        #Imports the images from my computer.
        image1 = Image.open("C://Users//andre/Downloads/Final Project M08/images/calculator.jpg")
        image2 = Image.open("C://Users//andre//Downloads//Final Project M08/images/report card.jpg")
       
        #Resizes the images.
        new_size = (100,100)
        resized_image1 = image1.resize(new_size)#These variables are use to resize the images.
        resized_image2 = image2.resize(new_size)

        self.img1_tk = ImageTk.PhotoImage(resized_image1)
        self.img2_tk = ImageTk.PhotoImage(resized_image2)

        #Creates frame for the images.
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        #Displays images in the entry box.
        self.image1_label = tk.Label(self.image_frame, image = self.img1_tk)
        self.image1_label.grid(row=0, column=0, padx=5)
        
        self.image2_label = tk.Label(self.image_frame, image = self.img2_tk)
        self.image2_label.grid(row=0, column=1, padx=5) 
        
        #Displays a title in the entry box.
        self.title_label = tk.Label(self.root, text = "Calculate your average and GPA!")
        self.title_label.pack(pady=10)
        
        #This is the frame for the entry box.
        self.frame_average = tk.Frame(self.root)
        self.frame_average.pack(pady = 30)
       
        #Displays a label for the "Number of Courses for Average Grade" entry.
        self.label_courses_average = tk.Label(self.frame_average, text = "Number of Courses for Average Grade: ")
        self.label_courses_average.grid(row = 0, column = 0)
       
        #Creates the entry box for "Number of Courses" within the frame.
        self.num_courses_average = tk.IntVar(value = 1)#This variable is used to store the number of average courses.
        self.entry_courses_average = tk.Entry(self.frame_average, textvariable = self.num_courses_average)
        self.entry_courses_average.grid(row = 0, column = 1)
        
        #Displays a buttom to initiate calculation.
        self.calculate_average_button = tk.Button(self.frame_average, text = "Calculate Average Grades", command = self.calculate_average)
        self.calculate_average_button.grid(row = 1, column = 0)
        
        #Displays a label for "Average Grade".
        self.average_grade_label = tk.Label(self.root, text = "")
        self.average_grade_label.pack()
        
        #This is the frame for the entry box.
        self.frame_gpa = tk.Frame(self.root)
        self.frame_gpa.pack(pady = 30)
        
        #Displays a label for the "Number of Courses for GPA" entry.
        self.label_courses_gpa = tk.Label(self.frame_gpa, text = "Number of Courses for GPA: ")
        self.label_courses_gpa.grid(row = 2, column = 0)
        
        #Creates entry box for "Number of Courses for GPA".
        self.num_courses_gpa = tk.IntVar(value = 1)#This variable is used to store the number of courses for the GPA.
        self.entry_courses_gpa = tk.Entry(self.frame_gpa, textvariable = self.num_courses_gpa)
        self.entry_courses_gpa.grid(row = 2, column = 1)
        
        #Displays a buttom to initiate calculation.
        self.calculate_gpa_button = tk.Button(self.frame_gpa, text = "Calculate GPA", command = self.calculate_gpa)
        self.calculate_gpa_button.grid(row = 3, column = 0)
        
        #Displays a label for "GPA".
        self.gpa_label = tk.Label(self.root, text = "")
        self.gpa_label.pack()
        
        #Displays a button to exit the application.
        self.exit_button = tk.Button(self.root, text = "Exit Calculator", command = self.exit_app)
        self.exit_button.pack()
    #Method calculates the average grade.    
    def calculate_average(self):

        #Use try-except for catching errors.
        try:
            #Retreive number of courses entered.
            num_courses1 = self.num_courses_average.get()#This variable stores the total grade percentage.
           
            #Initialize new variable: total_grades.
            total_grades = 0.0
            for i in range(num_courses1):
                
                #Create new entry box for entering the grade percentage for each course.
                grade_percentage = simpledialog.askfloat(title="Grade Percentage", prompt = f"Enter your grade percentage for course {i + 1}: ")#This variable stores the individual grade percentages for each course.
                #Cancels the user's input.
                if grade_percentage is None:
                    return
                #Logic for determining valid input.
                if not (0 <= grade_percentage <= 100):
                    messagebox.showerror("ERROR!!!", "Please input a valid number 0-100")
                    return
                
                #Calculation for grade average -->
                total_grades += grade_percentage
            average_grade = total_grades / num_courses1#This variable stores the average grade.
            average_letter_grade = self.points_to_letterGrade(average_grade)#This variable is used for the final display of the results.
            
            #Display average grade result.
            self.average_grade_label.config(text = f"Average Grade: {round(average_grade, 2)}  = {average_letter_grade}")
        #Returns an error message to the user if there's an invalid input.    
        except Exception:
            messagebox.showerror("ERROR!!!", "Please enter a number.")
           

    def calculate_gpa(self):
        #Use try-except for catching errors.
        try:
            #Retreive number of courses entered.
            num_courses2 = self.num_courses_gpa.get()#This variable stores the number of course for GPA.
            #Initialize new variables: total_gradepoints and total_credits.
            total_gradePoints = 0#This variable tores the total grade points for the GPA calculation.
            total_credits = 0#This variable stores the total credits for the GPA calculation.
            for i in range(num_courses2):
                #Create new entry box for entering the letter grade for each course.
                letter_grade = simpledialog.askstring(title = "Letter Grade", prompt = f"Enter your letter grade for course {i + 1}: ") #This variable stores the letter grade for the GPA calculation.
                #Cancels the user's input.
                if letter_grade is None:
                    return 
                if not self.valid_letter_grade(letter_grade):
                    messagebox.showerror("Error!!!", "Please input a valid letter grade: A, B, C, D, F")
                    return
                grade_points = self.grade_points(letter_grade)
                #Create new entry box for entering amount of credits per course.
                course_credits = simpledialog.askfloat(title = "Credits", prompt = f"Enter the amount of credits for this course {i + 1}: ")
                #Cancels the user's input.
                if course_credits is None:
                    return
                if course_credits <= 0:
                    messagebox.showerror("Error!!!", "Please enter a valid number.")
                #Calculation for gpa -->
                total_gradePoints += grade_points * course_credits
                total_credits += course_credits
            if total_credits > 0:
                gpa = total_gradePoints / total_credits
                self.gpa_label.config(text = f"GPA: {round(gpa, 2)}")
            else:
                messagebox.showerror("Error!!!")
        
        #Returns an error message to the user if there's an invalid input. 
        except Exception:
            messagebox.showerror("ERROR", "Please enter a number.")
                                  
    #This method is a conversion for the grading scale.
    def points_to_letterGrade(self, average_letter_grade):
        if (average_letter_grade >= 92):
            return "A"
        elif (average_letter_grade >= 90):
            return "A-"
        elif (average_letter_grade >= 85):
            return "B+"
        elif (average_letter_grade >= 82):
            return "B"
        elif (average_letter_grade >= 80):
            return "B-"
        elif (average_letter_grade >= 75):
            return "C+"
        elif (average_letter_grade >= 72):
            return "C"
        elif (average_letter_grade >= 70):
            return "C-"
        elif (average_letter_grade >= 65):
            return "D+"
        elif (average_letter_grade >= 62):
            return "D"
        elif (average_letter_grade >= 60):
            return "D-"
        else:
            return "F"
    
    #This method is a validator for checking letter grades.
    def valid_letter_grade(self, letter_grade):
        valid_grades = ["A", "B", "C", "D", "F"] #This variable is for a list that stores the valid grade letters.
        return letter_grade.upper() in valid_grades
    
    #This method exits the loop.
    def exit_app(self):
        self.root.destroy()
    
#Calls the main function to start.
if __name__ == "__main__":
    root = tk.Tk()
    calculator = GradingCalculator(root)
    root.mainloop()

