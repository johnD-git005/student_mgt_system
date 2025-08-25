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

	if student_mat in student_record:
		key = student_record[student_mat]
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
	print(f"\n {student_record}")
	
	for students in student_record:
		key = student_record[students]
		print(f"\n ID: {students}, Name: {key['name']}, DEPT: {key['dept']}, SCORE: {key['score']}, AGE: {key['age']}")

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
			new_name = input("\n Enter Name: ")
			student_record[student_id].update({'name':new_name})
			print("\n Name Updated Successfully!")
			print(f"\n {student_record[student_id]}")

		elif option == 2:
			print("\n UPDATE AGE")
			new_age = input("\n Enter Age: ")
			student_record[student_id].update({'age':new_age})
			print("\n Age Updated successfully!")
			print(f"\n {student_record[student_id]}")

		elif option == 3:
			print("\n UPDATE DEPARTMENT")
			new_dept = input("\n Enter Department: ")
			student_record[student_id].update({'dept':new_dept})
			print("\n Department Updated successfully!")
			print(f"\n {student_record[student_id]}")

		else:
			prnt("\n Invalid Selection!")
	else:
		print("\n Student Not Found!")

# FUNCTION TO SEARCH STUDENT BY NAME

def search_student_by_name():

	print("\n SEARCH BY NAME")

	student_name = input("\n Enter Student Name: ")
	flag = False

	for student in student_record:
		key = student_record[student]

		if student_name == key["name"]:
			print(f"\n ID: {student}, Name: {key['name']}, DEPT: {key['dept']}, SCORE: {key['score']}, AGE: {key['age']}")
			flag = True
	else:
		if flag == False:
			print(f"\n Student {student_name} Not Found!")

# FUNCTION TO FILTER STUDENT BY AGE

def filter_by_age():
	print("\n FILTER STUDENT BY AGE")

	student_age = int(input("\n Enter Student Age: "))
	flag = False

	for student in student_record:
		key = student_record[student]
				
		if key["age"] > student_age:
			print(f"\n ID: {student}, Name: {key['name']}, DEPT: {key['dept']}, SCORE: {key['score']}, AGE: {key['age']}")
			flag = True
	else:
		if flag == False:
			print(f"\n Student Greater Than Age:{student_age} Not Found!")

def count_students():
	
	total_number_of_students = len(student_record)
	print(f"\n TOTAL NUMBER OF STUDENTS: {total_number_of_students}")

# FUNCTION TO START PROGRAM

def start():
	while True:
		print("""
		1. ADD STUDENT
		2. DELETE STUDENT
		3. UPDATE STUDENT
		4. GET A SINGLE STUDENT
		5. DISPLAY ALL STUDENTS
		6. SEARCH STUDENT BY NAME
		7. FILTER STUDENT BY AGE
		8. TOTAL NUMBER OF SUDENTS
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

		elif options == 6:
			search_student_by_name()

		elif options == 7:
			filter_by_age()

		elif options == 8:
			count_students()
		else:
			print("\n Invalid Input!")
start()


