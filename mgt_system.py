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
# FUNCTION TO GET A STUDENT

def get_student():
	student_mat = int(input("\n Enter Student ID: "))
	key = student_record[student_mat]

	if student_mat in student_record:
		print(f"\n ID: {student_mat}, Name: {key['name']}, DEPT: {key['dept']}, SCORE: {key['score']}, AGE: {key['age']}")

	else:
		print("\n Student Does Not Exist!")

# FUNCTION TO DELETE A STUDENT

def delete_student():
	student_no = int(input("\n Please Enter Student ID: "))
	flag = False

	if student_no in student_record:
		del student_record[student_no]
		print(f"\n Student with ID: {student_no} Deleted Successfully!")
	else:
		print("\n Student Not FOund!")

# FUNCTION TO DISPLAY ALL STUDENTS

def display_student():
	if student_record:
		print(student_record)
	else:
		print("\n No student. Please Add student to the Data Base")

# FUNCTION TO UPDATE A STUDENT

def update_student():

	student_id = int(input("\n Enter student ID: "))

	if student_id in student_record:

		print(f"\n {student_record[student_id]}")

		print("""
		1. UPDATE NAME
		2. UPDATE AGE
		3. UPDATE DEPARTMENT
		""")

		option = int(input("\n Select an Option: "))

		if option == 1:
			print("\n UPDATE NAME")
			new_name = input("\n Enter Name to Update: ")
			student_record[student_id].update({'name':new_name})
			print("\n Name Update Successfully!")
			print(f"\n {student_record[student_id]}")


		else:
			prnt("\n Invalid Selecetion!")
	else:
		print("\n Student Not Found!")


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

		elif options == 3:
			print("\n UPDATE A STUDENT")
			update_student()

		elif options == 4:
			print("\n GET A STUDENT BY ID")
			get_student()

		elif options == 5:
			print("\n DISPLAY ALL STUDENT")
			display_student()
		else:
			print("\n Invalid Input!")
start()




	
