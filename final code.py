import datetime
import pywhatkit as kit
import customtkinter as ctk
from tkinter import messagebox
from tabulate import tabulate

# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")  # Dark theme
ctk.set_default_color_theme("blue")  # Green theme

# Function to run the selected application
def run_selected_app(app_number):
    if app_number == 1:
        print()
    elif app_number == 11:
        run_attendance_system_class6a()
    elif app_number == 15:
        run_attendance_system_class8a()
    elif app_number == 17:
        run_attendance_system_class9a()
    elif app_number == 18:
        run_attendance_system_class9b()
    elif app_number == 19:
        run_attendance_system_class10a()
    elif app_number == 20:
        run_attendance_system_class10b()
    elif app_number == 21:
        run_attendance_system_class11a()
    elif app_number == 22:
        run_attendance_system_class11b()
    elif app_number == 23:
        run_attendance_system_class12a()
    elif app_number == 24:
        run_attendance_system_class12b()

# Main function to create the mobile-like interface
def main():
    root = ctk.CTk()  # Main window
    root.title("Multi-Purpose Software")
    root.geometry("350x600")  # Mobile-sized window
    root.resizable(False, False)  # Prevent resizing

    # Create a title label
    title_label = ctk.CTkLabel(master=root, text="Multi-Purpose App", font=("Arial", 24))
    title_label.pack(pady=20)

    # Create a scrollable frame to hold the buttons
    scroll_frame = ctk.CTkScrollableFrame(master=root, width=300, height=450)
    scroll_frame.pack(pady=10)

    # Create buttons for each application inside the scrollable frame
    app_buttons = [
        ("Attendance class 1 A ", 1),
        ("Attendance class 1 B ", 2),
        ("Attendance class 2 A ", 3),
        ("Attendance class 2 B ", 4),
        ("Attendance class 3 A ", 5),
        ("Attendance class 3 B ", 6),
        ("Attendance class 4 A ", 7),
        ("Attendance class 4 B ", 8),
        ("Attendance class 5 A ", 9),
        ("Attendance class 5 B ", 10),
        ("Attendance class 6 A ", 11),
        ("Attendance class 6 B ", 12),
        ("Attendance class 7 A ", 13),
        ("Attendance class 7 B ", 14),
        ("Attendance class 8 A ", 15),
        ("Attendance class 8 B ", 16),
        ("Attendance class 9 A ", 17),
        ("Attendance class 9 B ", 18),
        ("Attendance class 10 A ", 19),
        ("Attendance class 10 B ", 20),
        ("Attendance class 11 A ", 21),
        ("Attendance class 11 B ", 22),
        ("Attendance class 12 A ", 23),
        ("Attendance class 12 B ", 24)
    ]

    for app_name, app_number in app_buttons:
        button = ctk.CTkButton(master=scroll_frame, text=app_name, command=lambda num=app_number: run_selected_app(num), width=250)
        button.pack(pady=10)

    # Run the application
    root.mainloop()


def run_attendance_system_class11a():
    # Function to get student data
    def get_student_data():
        return [
            ("Manisha Borah", "g"), ("Rupali Jonak Mahanta", "g"), ("Sakshi Satish Kohle", "g"),
            ("Abhinav Anubhab Khound", "b"), ("Bibhuti Ranjan Borah", "b"), ("Himanshu Gupta", "b"),
            ("Mohd. Farman Usta", "b"), ("Prasujya Pritam Borah", "b"), ("Vansh Behal", "b"),
            ("Anamika Das", "g"), ("Aryan Raj Gupta", "b"), ("Bhagyashree Saikia", "g"),
            ("Bhumika Roy", "g"), ("Bhumika Sarma", "g"), ("Bonani Bhuyan", "g"),
            ("Bedangraj Baruah", "b"), ("Deepanita Chakraborty", "g"), ("Geetashree Baruah", "g"),
            ("Hemphu Engti", "b"), ("Himashree Nag", "g"), ("Himesh Biswas", "b"),
            ("Himanku Rajkhowa", "b"), ("Manyataa Kashyap", "g"), ("Mouchami Nath", "g"),
            ("Prakiti Bora", "g"), ("Priyam Bora", "b"), ("Priyanko Devchoudhary", "b"),
            ("Rituparna Deka", "g"), ("Rupjyoti Borah", "b"), ("Suprabhat Borah", "b"),
            ("Uday Debnath", "b"), ("Kumari Lucky", "g"), ("Tulika Singhal", "g"),
            ("Sumesh Kumar", "b"), ("Debasish Borah", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()



def run_attendance_system_class12a():
    # Function to get student data
    def get_student_data():
        return [
            ("Ihitaa Rai", "g"), ("Krishna Merry Borah", "g"), ("Rongina Basumatary", "g"),
            ("Shristy Limbu", "g"), ("Sonia Mishra", "g"), ("Aryan Borah", "b"),
            ("Binit Sen", "b"), ("Debajeet Banik", "b"), ("Debojit Chakraborty", "b"),
            ("Debojit Sarkar", "b"), ("Gyanam Boruah", "b"), ("Jigyash Borah", "b"),
            ("Kunal Kakoti Bora", "b"), ("MD. Sahid Aktar", "b"), ("Soumya Subham Mahanta", "b"),
            ("Vyshnav .R", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()


def run_attendance_system_class11b():
    # Function to get student data
    def get_student_data():
        return [
            ("Akankhya Sarma", "g"), ("Anjali Bora", "g"), ("Bhumika Sahani", "g"),
            ("Jagriti Bordoloi", "g"), ("Krishti Borah", "g"), ("Kritika Kumari Gupta ", "g"),
            ("Meghashree Saikia", "g"), ("Prachi Biswas", "g"), ("Piyanki Tassa ", "g"),
            ("Pratyusha Mishra", "g"), ("Radhika Debnath", "g"), ("Rakhi Kumari Thakur", "g"),
            ("Shayana Deb", "g"), ("S.M. Tamanna", "g"), ("Subhangi Jaiswal", "g"),
            ("Upasana Parasar", "g"), ("Vanshika Behal", "g"), ("Abhishek Yadav", "b"),
            ("Amit Kumar", "b"), ("Arman Pravesh", "b"), ("Deep Dey", "b"),
            ("Deep Ghosh", "b"), ("Devraj Chetry", "b"), ("Geet Kashyap", "b"),
            ("Harit Baruahh", "b"), ("Karan Limbu", "b"), ("Nilanjan Das", "b"),
            ("MD. Rihan Ahmed", "b"), ("Rishikesh Saikia", "b"), ("Sahil Islam", "b"),
            ("Sidhartha Borah", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class12b():
    # Function to get student data
    def get_student_data():
        return [
            ("Anindita Sarkar", "g"), ("Astha Singh", "g"), ("Disha Baddu", "g"),
            ("Dolly Sobor", "g"), ("Gayatri Garg", "g"), ("Himachi Borah", "g"),
            ("Krissti Limbu", "g"), ("Neha Majumdar", "g"), ("Parishmita Das", "g"),
            ("Rajnandini Sahu", "g"), ("Rashmi Ekka", "g"), ("Rishita Hazarika", "g"),
            ("Tapti Das", "g"), ("Ashok Saha", "b"), ("Ankur Sahu", "b"),
            ("Krish Kumar Mahato", "b"), ("Martin Borah", "b"), ("Nayan Krishna Borah", "b"),
            ("Sumit Kumar", "b"), ("Tonmay Keot", "b"), ("Upasana Devi", "g"),
            (" Pallab Jyoti Borah", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class10a():
    # Function to get student data
    def get_student_data():
        return [
            ("Barun Boraik", "b"), ("Bikash Das", "b"), ("Krishna Kumar Shaw", "b"),
            ("Aman Debnath", "b"), ("Santanu Alchiary", "b"), ("Sunny Sarkar", "b"),
            ("Ankurima Basumatari", "b"), ("Adyanur Rahman", "b"), ("Dibyendu Tarafdar", "b"),
            ("Chanakya Hazarika", "b"), ("Aantara Raisa Samsad", "g"), ("Meghnath Banik", "b"),
            ("Priyakhee", "g"), ("Bhaskor Jyoti Nag", "b"), ("Priyam Kashyap Bhuyan", "b"),
            ("Apurba Sahariah", "b"), ("Tridip Mollick", "b"), ("Biraj Roy", "b"),
            ("Jahnabi Hazarika", "g"), ("Bonsika Raut", "g"), ("Srishti Nandni Pradhan", "g"),
            ("Charjyapad Mahanta", "b"), ("Biki Roy", "b"), ("Swati Kumari", "g"),
            ("Daizy Alchiary", "g"), ("Sujata Saikia", "g"), ("Aditya Kumar Singh", "b"),
            ("Priyanuj Priyam Das", "b"), ("Suman Tamuli", "b"), ("Sayanika Das", "g"),
            ("Arina Bora", "g"), ("Aryan Patel", "b"), ("Aryaman Hazarika", "b"),
            ("Anik Debnath", "b"), ("Bikas Gogai", "b"), ("Rakhi Hainary", "g"),
            ("Piku Das", "b"), ("Pinku Das", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class10b():
    # Function to get student data
    def get_student_data():
        return [
            ("Abhinjab Saikia", "b"), ("Afreen Khatun", "g"), ("Amon Bora", "b"),
            ("Ankita Sarkar", "g"), ("Bastab Borthakur", "b"), ("Bikramjeet Dhar", "b"),
            ("Bornali Kalindi", "g"), ("Borneel Bhuyan", "b"), ("Chahat Gupta", "g"),
            ("Chinmoyjyoti Bora", "b"), ("Deep Krishna", "b"), ("Dipanker Das", "b"),
            ("Gyanjuti Nath", "b"), ("Himanuj Bora", "b"), ("Himashri Talukder", "g"),
            ("Hiyamoni Biswas", "g"), ("Ishika Kumari", "g"), ("Jahnabi Sah", "g"),
            ("Jonak.S. Mahanta", "g"), ("Jaydeep Nahak", "b"), ("Layashree Bora", "g"),
            ("M. Archana", "g"), ("Momi Tasha", "g"), ("Nabanita Das", "b"),
            ("Nabarun Saika", "b"), ("Nafisa Yasmin", "g"), ("Nijush Mandal", "b"),
            ("Nitul Gohain", "b"), ("Pratik Gupta", "b"), ("Rituraj Medhi", "b"),
            ("Sadia Sultana", "g"), ("Sanchita Saika", "g"), ("Sneha Borah", "g"),
            ("Sneha Das", "g"), ("Srineha Hazarika", "g"), ("Toshbina Khatun", "g"),
            ("Viswajuti Borah", "b"), ("Muskan Begum", "g"), ("Krisha Sharma", "g"), ("K.Vaishnavi", "g")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class6a():
    # Function to get student data
    def get_student_data():
        return [
            ("Advita Upadhya", "g"), ("Aradhya Borah", "g"), ("Arya Bharti", "g"),
            ("Baisali Sutradhar", "g"), ("Harshita Bhuyan", "g"), ("Jore Akshara Ashok", "g"),
            ("Jyoti", "g"), ("Kuki Saikia", "g"), ("Mallika Goswami", "g"),
            ("Riya Daimari", "g"), ("Sara Nishant Deshmukh", "g"), ("Shreyashi Choudhary", "g"),
            ("Stuti", "g"), ("Tanavi", "g"), ("Tanaya Jyoti Kashyap ", "g"),
            ("Tanisha Bordoloi", "g"), ("Vaishnavi Ram Jadhav", "g"), ("Arosmita Patra", "g"),
            ("Ayusmita Patra", "g"), ("Arnav Bharti", "b"), ("Arnav Kumar Kushwaha", "b"),
            ("Atharv Boruah", "b"), ("Bijoy Debnath", "b"), ("Evon Bordoloi", "b"),
            ("Himangshu Medhi", "b"), ("Hridoy Ranjan Hazarika", "b"), ("Ishan Nawaz", "b"),
            ("Juned Rehman", "b"), ("Kailyan Jyoti Borah", "b"), ("Kaushik Moni Upadhya", "b"),
            ("Mokshagundam Aditya", "b"), ("Nasim Ahmed", "b"), ("Panjak Saikia", "b"),
            ("Rudra Pratap", "b"), ("Saurabh Das", "b"), ("Shaswat Kumar Nayak", "b"),
            ("Uddhab Dey", "b"), ("Vivaan Sharma", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class9a():
    # Function to get student data
    def get_student_data():
        return [
            ("Angkita Rajak", "g"), ("Aruchi Bhattarai", "g"), ("Bishruti Das", "g"),
            ("Bhagyapriya Devi", "g"), ("Dokhina Kashyap", "g"), ("Ishika Sharma", "g"),
            ("Jerin Shaikh", "g"), ("Kayel Mandal", "g"), ("Puja Nath", "g"),
            ("Ritushri Roy", "g"), ("Sevika Hazarika", "g"), ("Shristi Baglari", "g"),
            ("Siuli Sarkar", "g"), ("Sikha Moni", "g"), ("Sudipta Kumari ", "g"),
            ("Abinit Nayak", "b"), ("Ansh Rajak", "b"), ("Ashmit Sharma", "b"),
            ("Atish Portel", "b"), ("Bastab Jyoti", "b"), ("Bhabarnab bhardwaj", "b"),
            ("Bibek Kumar Ram", "b"), ("Binod Alsiari", "b"), ("D. Srikant", "b"),
            ("Devraaj Singh Duhan", "b"), ("Dipanker Das", "b"), ("Iman Parasar", "b"),
            ("Jatin Sharma", "b"), ("Judhisti Sarkar", "b"), ("Kaushik Roy", "b"),
            ("Mandip Borah", "b"), ("Nirob Raj Bora", "b"), ("Pal Borah", "b"),
            ("Raj Debnath", "b"), ("Sanklpajit", "b"), ("Vivek Prakash", "b"),
            ("Vijay Hazarika", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class9b():
    # Function to get student data
    def get_student_data():
        return [
            ("Adity Jaiswal", "g"), ("Anokhi Gayan", "g"), ("Antara Mandal", "g"),
            ("Anuskha Kumari", "g"), ("Bhagyadipta Sarmah", "g"), ("Dipandita Pradhan", "g"),
            ("Ishika Bhattacharjee", "g"), ("kamolika Sarkar", "g"), ("Liza Devi", "g"),
            ("Liza Roy", "g"), ("Lucky Moni Boruah", "g"), ("Nargis Noor", "g"),
            ("Papori Das", "g"), ("Sahana Begum", "g"), ("Sneha Deka", "g"),
            ("Subasana Mahanta", "g"), ("Subhrata Priyam Saikia", "g"), ("Saanvi Bir", "g"),
            ("Lucky basumatary", "g"), ("Khushi Kumari", "g"), ("P. Bhanushri", "g"),
            ("Akash. R Goswami", "b"), ("Ayush Borah", "b"), ("Aman Kumar Das", "b"),
            ("Biradjyoti Hazarika", "b"), ("LakhyaJyoti Sarkar", "b"), ("Jit karmakar", "b"),
            ("Joy Jyoti Basumatari", "b"), ("Rajdeep Dadhara", "b"), ("Rihan tamim Choudhary", "b"),
            ("Rajjyoti Hazarika", "b"), ("Ritusmin Borah", "b"), ("Shaikh Tanzil Mehbub", "b"),
            ("Prabhat Kumar", "b"), ("Sumit Bhagat", "b"), ("MD. RihaN Ali", "b"),
            ("Gaurav Paul", "b"), ("Adeep Kumar", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class8a():
    # Function to get student data
    def get_student_data():
        return [
            ("Banasree Das", "g"), ("Bidisha Chetry", "g"), ("Deeptakshi Saikia", "g"),
            ("Jyotiporna Borah", "g"), ("Kamcharia Tejasri", "g"), ("Nafisa Ahmed", "g"),
            ("Pabitree Chanda", "g"), ("Pahi Mochahary", "g"), ("Pragya Acharya", "g"),
            ("Shilpi Shikha Bora", "g"), ("Shristi Goswami", "g"), ("Ziya Choudhury", "g"),
            ("Akash Borah", "b"), ("Alaka R. Borah", "b"), ("Ankesh Yadav ", "b"),
            ("Ayushman Borah", "b"), ("Bhanu Pratap Singh", "b"), ("Bhaskar Jyoti", "b"),
            ("Debanga Pratim Bora", "b"), ("Deep Orang", "b"), ("Devansh Das", "b"),
            ("Dhrutiraj Deka", "b"), ("Gourab Jyoti Das", "b"), ("Gourab Debnath", "b"),
            ("Ishant Das", "b"), ("Jyoti Shekar Das", "b"), ("Khilendra Singh", "b"),
            ("Kuldeep Rabha", "b"), ("Madhurjya Das", "b"), ("Mahesh Chetry", "b"),
            ("Manab Barman", "b"), ("Mg Abhineet", "b"), ("Nilotpal Borah", "b"),
            ("Pallab Singha", "b"), ("Tahir Ahmed", "b"), ("Ujjwal Singh", "b"),
            ("Vivek K. Ekka", "b")
        ]
    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_attendance_system_class7b():
    # Function to get student data
    def get_student_data():
        return [
            ("Hirokjoyti Mazumdar", "g"), ("Moitree Nath", "g"), ("Bitupan Das", "g"),
            ("Koushik Bhuyan", "g"), ("Sri Nibir Sharma", "g"), ("Mayuri Bhuyan", "g"),
            ("Harash Raj", "g"), ("Adarash Kumar", "g"), ("Ishika Das", "g"),
            ("Chitranikta Roy", "g"), ("Ayank Kumar", "g"), ("Sudokhina Kashyap", "g"),
            ("Angelina kakoti", "g"), ("Bandita Das", "g"), ("Debpriya Paul", "g"),
            ("Palak Debnath", "g"), ("Parasanta Mudli", "g"), ("Washim Dewan", "g"),
            ("Varnabi Sarmah", "g"), ("Srishti Bezbaruah", "b"), ("divya Saikia", "b"),
            ("Atharv Boruah", "b"), ("Bijoy Debnath", "b"), ("Evon Bordoloi", "b"),
            ("Himangshu Medhi", "b"), ("Hridoy Ranjan Hazarika", "b"), ("Ishan Nawaz", "b"),
            ("Juned Rehman", "b"), ("Kailyan Jyoti Borah", "b"), ("Kaushik Moni Upadhya", "b"),
            ("Mokshagundam Aditya", "b"), ("Nasim Ahmed", "b"), ("Panjak Saikia", "b"),
            ("Rudra Pratap", "b"), ("Saurabh Das", "b"), ("Shaswat Kumar Nayak", "b"),
            ("Uddhab Dey", "b"), ("Vivaan Sharma", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message):
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print("Attendance data sent successfully via WhatsApp.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    # Main function to run the attendance system
    def main():
        if get_password():
            print("Password validated")  # Debug
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                try:
                    save_to_file(filename, attendance, present_count, total_students, absent_students)
                    print("File saved successfully")  # Debug
                except Exception as e:
                    print(f"Error saving file: {e}")  # Debug

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")
                
                # Send WhatsApp message
                send_whatsapp_message("+918399925675", message)

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()



if __name__ == "__main__":
    main()