students = {}

while True:
   print("-------MENU-------")
   print("1. Add a student record")
   print("2. Display all student names who have an average mark above 80")
   print("3. Update marks")
   print("4. Display Student Records")
   print("5. Close Program")

   choice = int(input("Enter your choice: "))

   if choice == 1:
      rno = int(input("Enter the roll number of the student: "))
      name = input("Enter the name of the student: ")

      marks = []
      for i in range(3):
         print("Enter marks of subject", i + 1)
         marks.append(int(input()))

      students[rno] = (name, marks)
      print("\nFinal Record:\n", students)

   elif choice == 2:
      print("\nStudents with average marks above 80:\n")
      for name, marks in students.values():
         average = sum(marks) / len(marks)
         if average > 80:
            print("\n",name)

   elif choice == 3:
      rno = int(input("\nEnter the roll number of the student: "))
      if rno in students:
         name, marks = students[rno]
         for i in range(3):
            marks[i] = int(input(f"Enter new marks for subject {i + 1}: "))
         students[rno] = (name, marks)
         print("\nUpdated Record: \n", students)
      else:
         print("Student not found.")

   elif choice == 4:
      print("\nStudent Records:\n")
      print(students)
     
   elif choice == 5:
      print("Program closed.")
      break

   else:
      print("Invalid choice.")