#in this part the student attendance is searched
student_name = input("Enter the student name:")
import pandas as pd
df = pd.read_excel("C:\\Users\\dhrumi\\OneDrive\\Documents\\BSC-IT\\python\\student_attendance (1).xlsx")
print(df.columns)
student = df[df["Name"] == student_name]
if not student.empty:
    print("Student Found")
    print(student)
    total_lec = student.iloc[0]["Total Lectures"]
    attend_lec = student.iloc[1]["Attended Lectures"]
    percentage = (attend_lec / total_lec) * 100
    print("Attendance Percentage :", percentage)
else:
    print("Student not found")