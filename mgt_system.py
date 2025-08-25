student_record = {}

# FNCTION FOR ADDING STUDENT

def add_student():
	name = input("\n Enter Name: ")
	dept = input("\n Department: ")
	score = input("\n Score: ")
	age = int(input("\n Enter age: "))

	new_key = len(student_record) + 1
	student_record[new_key] = {
		"mat": new_key,
		"name": name,
		"dept": dept,
		"score": score,
		"age": age
		}
# FUNCTION TO DELETE STUDENT

def get_student():
	student_mat = int(input("\n Enter Student ID: "))
	flag = False

	for student_id in student_record:
		if student_id == student_mat:
			print(student_record[student_id])
			flag = True
	else:
		if flag == False:
			print("\n Student Not Found!")

# FUNCTION TO DELETE A STUDENT

def delete_student():
	student_no = int(input("\n Please Enter Student ID: "))
	flag = False

	for student_id in student_record:
		if student_id == student_no:
			del student_record[student_id]
			print("\n Student with ID: {student_no} Deleted Successfully!")
			flag = True
	else:
		if flag == False:
			print("\n Student Not Found!")

# FUNCTION TO DISPLAY ALL STUDENTS

def display_student():
	if student_record:
		print(student_record)
	else:
		print("\n No student. Please Add student to the Data Base")

# FUNCTION TO START PROGRAM

def start():
	while True:
		print("""
		1. ADD STUDENT
		2. DELETE STUDENT
		3. UPDATE STUDENT
		4. GET A SINGLE STUDENT
		5. DISPLAY ALL STUDENTS
		""")

		options = int(input("\n Please select an Option: "))
		if options == 1:
			print("\n ADD STUDENT")
			add_student()
			print(f"\n {student_record}")

		elif options == 2:
			print("\n DELETE A STUDENT BY ID")
			delete_student()

		elif options == 4:
			print("\n GET A STUDENT BY ID")
			get_student()

		elif options == 5:
			print("\n DISPLAY ALL STUDENT")
			display_student()
		else:
			print("\n Invalid Input!")
start()




	
