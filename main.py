# 📝 Grades Classifier - Session 5: elif Statement and Logical Operators
# Welcome to Python School! Let's help you process your exam scores like a pro 📚✨
# We will update our last session's project to assign grades based on boundaries instead
# of a simple pass/fail output. We will also use

# Print welcome message
print("Welcome to Grades Classifier")

# Ask for student name
name = input("Enter the student's name: ").capitalize()

# Take marks for three subjects (out of 100 each)
math = float(input("Enter your marks in Math (Out of 100): "))
science = float(input("Enter your marks in Science (Out of 100): "))
english = float(input("Enter your marks in English (Out of 100): "))
# ➕ Addition to Last Project: Print a warning if either of the subjects' marks
# exceed 100. This should only be a warning and program should continue with invalid inputs.
# Hint: Use a single if with an appropriate logical operator to combine conditions.
if math > 100 or science > 100 or english > 100:
  print("The marks must be less than 100.\n")
# Total marks possible
total_marks = 300

# Total obtained
obtained_marks = math + science + english

# Calculate average and percentage
avg = round(obtained_marks / 3, 2)
percentage = round((obtained_marks / total_marks) * 100, 2)
# Round for nicer output
# Print student report
print("-" * 30)
print("Student's Report\n")
# Display results
print("Student:", name)
print("Marks in Math:", math)
print("Marks in Science:", science)
print("Marks in English:", english)
print(f"Total Marks: {obtained_marks}/{total_marks}")
print("Average:", avg)
print("Percentage:", str(percentage), "%")
# ℹ️ Update this part of pass/fail decision from last session project to
# instead assign a grade based on following boundaries.
#
# 90+   - A+
# 80-89 - A
# 70-79 - B
# 60-69 - C
# 50-59 - D
# <50   - F
#
# Hint: Use elif statements.
if percentage >= 90:
  print("Grade: A+")
elif 80 <= percentage <= 89:
  print("Grade: A")
elif 70 <= percentage <= 79:
  print("Grade: B")
elif 60 <= percentage <= 69:
  print("Grade: C")
elif 50 <= percentage <= 59:
  print("Grade: D")
else:
  print("Grade: F")
# Encouraging message
print("\nKeep working hard and keep learning! 💡📘\n")
print("-" * 30)
# 💡 Notes for learners:
# - Arithmetic: + for addition, / for division, () controls order (precedence).
# - Comparison: >= checks "greater than or equal to".
# - A comparison returns True or False, which we can print as a result.
