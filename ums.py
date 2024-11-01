import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Person:
    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Mobile Number: {self.mobile}"

class Student(Person):
    def __init__(self, name, email, mobile, branch):
        self.branch = branch
        super().__init__(name, email, mobile)

    def __str__(self):
        return super().__str__() + f", Branch: {self.branch}"

class Teacher(Person):
    def __init__(self, name, email, mobile, subject):
        self.subject = subject
        super().__init__(name, email, mobile)

    def __str__(self):
        return super().__str__() + f", Subject: {self.subject}"

class College:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_students(self):
        if not self.students:
            print("No students are there in this college")
        else:
            for i, student in enumerate(self.students, start=1):
                print(f"Student {i} details: {student}")

    def display_teachers(self):
        if not self.teachers:
            print("No teachers are there in this college")
        else:
            for i, teacher in enumerate(self.teachers, start=1):
                print(f"Teacher {i} details: {teacher}")

def send_otp_via_email(receiver_email):
    otp = random.randint(100000, 999999)
    
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "20bec016@iiitdwd.ac.in"  # Replace with your email
    sender_password = "pahk edsb yljy zfzv"  # Replace with your email password or app password

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Your OTP Code"
    
    body = f"Your OTP code is: {otp}"
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.send_message(message)
            print(f"OTP sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send OTP: {e}")

    return otp

colleges = []
while True:
    print("\nChoose any option: ")
    print("1. Create College")
    print("2. Create Student")
    print("3. Create Teacher")
    print("4. Display Students")
    print("5. Display Teachers")
    print("6. Exit")
    try:
        x = int(input("Enter opted Value: "))
        if x == 1:
            cname = input("Enter College Name: ")
            if any(c.name == cname for c in colleges):
                print("College already exists with the same name")
            else:
                colleges.append(College(cname))
        elif x == 2:
            cname = input("Enter College name: ")
            college = next((c for c in colleges if c.name == cname), None)
            if college:
                sname = input("Enter student name: ")
                semail = input("Enter student email: ")
                smobile = input("Enter mobile number: ")
                otp = send_otp_via_email(semail)
                user_otp = int(input("Enter the OTP received: "))
                if user_otp == otp:
                    sbranch = input("Enter Student Branch: ")
                    college.add_student(Student(sname, semail, smobile, sbranch))
                    print("Student added successfully!")
                else:
                    print("Invalid OTP. Student not added.")
            else:
                print("College does not exist")
        elif x == 3:
            cname = input("Enter College name: ")
            college = next((c for c in colleges if c.name == cname), None)
            if college:
                tname = input("Enter teacher name: ")
                temail = input("Enter teacher email: ")
                tmobile = input("Enter mobile number: ")
                otp = send_otp_via_email(temail)
                user_otp = int(input("Enter the OTP received: "))
                if user_otp == otp:
                    tsubject = input("Enter teacher subject: ")
                    college.add_teacher(Teacher(tname, temail, tmobile, tsubject))
                    print("Teacher added successfully!")
                else:
                    print("Invalid OTP. Teacher not added.")
            else:
                print("College does not exist")
        elif x == 4:
            cname = input("Enter College name: ")
            college = next((c for c in colleges if c.name == cname), None)
            if college:
                college.display_students()
            else:
                print("College does not exist")
        elif x == 5:
            cname = input("Enter College name: ")
            college = next((c for c in colleges if c.name == cname), None)
            if college:
                college.display_teachers()
            else:
                print("College does not exist")
        elif x == 6:
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

