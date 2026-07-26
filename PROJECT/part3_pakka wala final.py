#in this part the student attendance is searched
student_name = input("Enter the student name:") #this takes the input for the name of student that u want to find
import pandas as pd
df = pd.read_excel("C:\\Users\\dhrumi\\OneDrive\\Documents\\BSC-IT\\python\\student_attendance (1).xlsx")
student = df[df["Name"] == student_name] #this checks whether the name entered by the user is there or not in the dataset
if not student.empty: #Jo naam user ne enter kiya hai, us naam ka data table me search karne ke baad agar student ka record mila hai toh student DataFrame empty nahi hai, matlab uske andar data hai, isliye if condition chalegi."
    print("Student Found")
    total_lec = student.iloc[0]["Total_Lectures"]
    attend_lec = student.iloc[0]["Attended_Lectures"]
    percentage = (attend_lec / total_lec) * 100 #this is to calculate the percentage of attendance of the student
    print("Attendance Percentage :", percentage)
else:
    print("Student not found")
if percentage < 75 :
    print("Safe")
else:
    print("Need to attend lectures")
#now in this only the deduction of the lecture not attended part is remaining, so that will be done in the next part