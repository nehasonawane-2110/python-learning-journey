# calculates the percentage.
Clang = int(input("Enter the marks of subject 1 :"))
python = int(input("Enter the marks of subject 2: "))
java = int(input("Enter the marks of subject3: "))
html = int(input("Enter the marks of subject4: "))
css = int(input("Enter the marks of subject5: "))

gain_marks = Clang + python + java + html + css
percentage = (gain_marks / 500) * 100
print(f"The percentage in the Exam: {percentage}%.")
