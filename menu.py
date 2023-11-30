#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
import mysql.connector
from mysql.connector import errorcode
import hashlib
from prettytable import PrettyTable


# Your existing database and table definitions

# def signup():
#         email = input("Enter email address: ")
#         pwd = input("Enter password: ")
#         confirm_pwd = input("Confirm password: ")

#         if confirm_pwd == pwd: 
#             enc = confirm_pwd.encode()
#             hash1 = hashlib.md5(enc).hexdigest()

#             with open("credentials.txt", "w") as f:
#                     f.write(email + "\n")
#                     f.write(hash1)
#             f.close()
#             print("You have registered successfully!")
#         else:
#             print("Password is not same as above! \n")

# def login():
#     email = input("Enter email: ")
#     pwd = input("Enter password: ")
#     auth = pwd.encode()
#     auth_hash = hashlib.md5(auth).hexdigest()
#     with open("credentials.txt", "r") as f:
#         stored_email, stored_pwd = f.read().split("\n")
#     f.close()
#     if email == stored_email and auth_hash == stored_pwd:
#          print("Logged in Successfully!")
#          return True
#     else:
#          print("Login failed! \n")
#          return False

def signup(flag):
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        confirm_pwd = input("Confirm password: ")

        if confirm_pwd == pwd: 
            enc = confirm_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()

            with open("credentials.txt", "w") as f:
                    f.write(email + "\n")
                    f.write(hash1)
            f.close()
            flag = 1
            print("You have registered successfully!")
            return flag
          
        else:
            flag = 3
            print("Password is not same as above! \n")
            return flag
        return flag
        
     
def login(flag):
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         flag = 1
         return flag
    else:
         flag = 2
         print("Login failed! \n")
         return flag
    return flag 

def connect_to_database():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            user='root',
            host='localhost',
            database='TRAIN_COMPANY'
        )

        cursor = connection.cursor()
        cursor.execute("USE TRAIN_COMPANY")
        cursor.close()

        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Error: Database {'TRAIN_COMPANY'} does not exist.")
        else:
            print(f"Error: {err}")
        return None
    

def edit_employees_data():
    print("Editing Employees Data...")

    # Connect to the MySQL database
    connection = connect_to_database()
    if not connection:
        return

    try:
        # Example: Ask the user to input new employee data
        # Modify this part based on your 'employees' table structure
        ssn = input("Enter SSN: ")
        last_name = input("Enter last name: ")
        first_name = input("Enter first name: ")
        gender = input("Enter gender (M/F): ")
        age = int(input("Enter age: "))
        clearance_level = input("Enter clearance level: ")
        salary = float(input("Enter salary: "))
        phone_number = input("Enter phone number: ")
        shift_schedule = input("Enter shift schedule: ")
        position = input("Enter position: ")
        address = input("Enter address: ")

        # Example: Insert the new employee data into the 'employees' table
        cursor = connection.cursor()
        insert_query = (
            "INSERT INTO employees "
            "(ssn, last_name, first_name, gender, age, clearance_level, salary, phone_number, shift_schedule, position, address) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (ssn, last_name, first_name, gender, age, clearance_level, salary, phone_number, shift_schedule, position, address))

        # Commit the changes
        connection.commit()

        print("Employee data updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Similar functions for other tables

def edit_trains_data():
    print("Editing Trains Data...")

    connection = connect_to_database()
    if not connection:
        return

    try:
        routes = input("Enter routes: ")
        train_schedule = input("Enter train schedule: ")
        location = input("Enter location: ")

        cursor = connection.cursor()
        insert_query = "INSERT INTO trains (routes, train_schedule, location) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (routes, train_schedule, location))

        connection.commit()

        print("Train data updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def edit_passengers_data():
    print("Editing Passengers Data...")

    connection = connect_to_database()
    if not connection:
        return

    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        ticket_number = input("Enter ticket number: ")
        age = int(input("Enter age: "))
        phone_number = input("Enter phone number: ")
        gender = input("Enter gender (M/F): ")

        cursor = connection.cursor()
        insert_query = "INSERT INTO passengers (first_name, last_name, ticket_number, age, phone_number, gender) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (first_name, last_name, ticket_number, age, phone_number, gender))

        connection.commit()

        print("Passenger data updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def edit_service_conditions_data():
    print("Editing Service Conditions Data...")

    connection = connect_to_database()
    if not connection:
        return

    try:
        engine_cars = int(input("Enter engine cars: "))
        train_station = input("Enter train station: ")
        num_passenger_cars = int(input("Enter number of passenger cars: "))
        maintenance_description = input("Enter maintenance description: ")

        cursor = connection.cursor()
        insert_query = "INSERT INTO service_conditions (engine_cars, train_station, num_passenger_cars, maintenance_description) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (engine_cars, train_station, num_passenger_cars, maintenance_description))

        connection.commit()

        print("Service conditions data updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def edit_delays_data():
    print("Editing Delays Data...")

    connection = connect_to_database()
    if not connection:
        return

    try:
        estimate_delay_time = int(input("Enter estimate delay time (minutes): "))
        status = input("Enter status: ")
        train_affected = int(input("Enter train affected: "))

        cursor = connection.cursor()
        insert_query = "INSERT INTO delays (estimate_delay_time, status, train_affected) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (estimate_delay_time, status, train_affected))

        connection.commit()

        print("Delays data updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def view_table_data(table_name):
    print(f"Viewing {table_name} Data...")

    # Connect to the MySQL database
    connection = connect_to_database()
    if not connection:
        return

    try:
        cursor = connection.cursor()

        # Check if the table exists
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        if not cursor.fetchone():
            print(f"Error: Table '{table_name}' does not exist.")
            return

        # Get column names
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        column_names = [row[0] for row in cursor.fetchall()]

        # Fetch all the rows
        select_query = f"SELECT * FROM {table_name}"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Create a PrettyTable object
        table = PrettyTable(column_names)

        # Add rows to the table
        for row in rows:
            table.add_row(row)

        # Print the formatted table
        print(table)
        

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

def update_record(table_name):
    print(f"Updating Record in {table_name}...")


    # Connect to the MySQL database
    connection = connect_to_database()
    
    if not connection:
        return

    try:
        cursor = connection.cursor()

        # Check if the table exists
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        if not cursor.fetchone():
            print(f"Error: Table '{table_name}' does not exist.")
            return

        # Get column names
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        column_names = [row[0] for row in cursor.fetchall()]

        # Display a menu for selecting the primary key column
        primary_key_column = select_from_menu("Select the primary key column:", column_names)

        if primary_key_column is None:
            # User canceled the selection
            print("Update canceled.")
            return

        # Prompt user for the primary key value to identify the record to update
        primary_key_value = input(f"Enter the {primary_key_column} value to update: ")

        # Use a flag to determine whether to keep updating
        update_flag = True

        while update_flag:
            # Prompt user for the column to update and the new value
            update_column = input("Enter the column name to update (or 'exit' to finish): ")

            if update_column.lower() == 'exit':
                # Break the loop if the user enters 'exit'
                update_flag = False
            elif update_column not in column_names:
                print(f"Error: Column '{update_column}' does not exist in the table.")
            else:
                new_value = input(f"Enter the new value for {update_column}: ")

                # Build the UPDATE query
                update_query = f"UPDATE {table_name} SET {update_column} = %s WHERE {primary_key_column} = %s"

                # Execute the UPDATE query
                cursor.execute(update_query, (new_value, primary_key_value))

                # Commit the changes
                connection.commit()

                print(f"Updated {update_column} to {new_value}.")

        print("Record updated successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

def select_from_menu(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = input("Enter the number of your choice (or 'cancel' to cancel): ")

    if choice.lower() == 'cancel':
        return None

    try:
        index = int(choice) - 1
        if 0 <= index < len(options):
            return options[index]
        else:
            print("Invalid choice. Please enter a valid number.")
            return select_from_menu(prompt, options)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return select_from_menu(prompt, options)


def delete_record(table_name):
    print(f"Deleting Record in {table_name}...")

    # Connect to the MySQL database
    connection = connect_to_database()
    if not connection:
        return

    try:
        cursor = connection.cursor()

        # Check if the table exists
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        if not cursor.fetchone():
            print(f"Error: Table '{table_name}' does not exist.")
            return

        # Get column names
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        column_names = [row[0] for row in cursor.fetchall()]

        # Display a menu for selecting the primary key column
        primary_key_column = select_from_menu("Select the primary key column:", column_names)

        if primary_key_column is None:
            # User canceled the selection
            print("Deletion canceled.")
            return

        # Prompt user for the primary key value to identify the record to delete
        primary_key_value = input(f"Enter the {primary_key_column} value to delete: ")

        # Build the DELETE query
        delete_query = f"DELETE FROM {table_name} WHERE {primary_key_column} = %s"

        # Execute the DELETE query
        cursor.execute(delete_query, (primary_key_value,))

        # Commit the changes
        connection.commit()

        print("Record deleted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# The select_from_menu function remains the same as in the previous response.


def main():
    options = ["Enter Employee Data", "Enter Train Data", "Enter Passenger Data", "Enter Service Data", "Enter Delay Data", "View Table Data", "Update Data", "Delete Data", "Exit"]
    terminal_menu = TerminalMenu(options)
    flag = 0
    while 1:
            print("------------Train Company System-----------")
            print(" 1.Signup ")
            print(" 2.login ")
            print(" 3.Exit ")
            ch  = int(input("Enter number choice: "))
            if ch == 1:
                signup(flag)
                            
                
            elif ch == 2:
                
                flag = login(flag)
                print(flag)
                while flag == 1 :
                        menu_entry_index = terminal_menu.show()

                        if menu_entry_index == len(options) - 1:
                            print("Exiting program. Goodbye!")
                            break

                        selected_option = options[menu_entry_index]

                        if selected_option == "Enter Employee Data":
                            edit_employees_data()
                        elif selected_option == "Enter Train Data":
                            edit_trains_data()
                        elif selected_option == "Enter Passenger Data":
                            edit_passengers_data()
                        elif selected_option == "Enter Service Data":
                            edit_service_conditions_data()
                        elif selected_option == "Enter Delays Data":
                            edit_delays_data()
                        elif selected_option == "View Table Data":
                            table_name = input("Enter table name to view (Employees, Passengers, Trains, Service_conditions, or Delays): ")
                            view_table_data(table_name)
                        elif selected_option == "Update Data":
                            table_name = input("Enter table name to update (Employees, Passengers, Trains, Service_conditions, or Delays): ")
                            update_record(table_name)
                        elif selected_option == "Delete Data":
                            table_name = input("Enter table name to delete from (Employees, Passengers, Trains, Service_conditions, or Delays): ")
                            delete_record(table_name)
                        elif ch == 3:
                            break
                else:
                    print("Try again, Numbers only!")
                    
            





# def main():
#     options = ["Enter Employee Data", "Enter Train Data", "Enter Passenger Data", "Enter Service Data", "Enter Delay Data", "View Table Data", "Update Data", "Delete Data", "Exit"]
#     terminal_menu = TerminalMenu(options)
    
#     while 1:
#         print("------------Login Train Company System-----------")
#         print(" 1. Signup ")
#         print(" 2. Login ")
#         print(" 3. Exit ")
#         ch = int(input("Enter number choice: "))
        
#         if ch == 1:
#             signup()
#             ch = int(input("Enter number choice: "))
#         elif ch == 2:
#             login()
#             flag = 1
#         elif ch == 3:
#             break
#         else:
#             print("Try again, Numbers only!")
        
#         while flag <= 1:
#             menu_entry_index = terminal_menu.show()

#             if menu_entry_index == len(options) - 1:
#                 print("Exiting program. Goodbye!")
#                 break

#             selected_option = options[menu_entry_index]

#             if selected_option == "Enter Employee Data":
#                 edit_employees_data()
#             elif selected_option == "Enter Train Data":
#                 edit_trains_data()
#             elif selected_option == "Enter Passenger Data":
#                 edit_passengers_data()
#             elif selected_option == "Enter Service Data":
#                 edit_service_conditions_data()
#             elif selected_option == "Enter Delays Data":
#                 edit_delays_data()
#             elif selected_option == "View Table Data":
#                 table_name = input("Enter table name to view (Employees, Passengers, Trains, Service_conditions, or Delays): ")
#                 view_table_data(table_name)
#             elif selected_option == "Update Data":
#                 table_name = input("Enter table name to update (Employees, Passengers, Trains, Service_conditions, or Delays): ")
#                 update_record(table_name)
#             elif selected_option == "Delete Data":
#                 table_name = input("Enter table name to delete from (Employees, Passengers, Trains, Service_conditions, or Delays): ")
#                 delete_record(table_name)
        
        # Reset flag after inner while loop
#         flag = 0

if __name__ == "__main__":
    main()














#SQL CODE----------------------------------------------------------------

# CREATE TABLE employees (
#   ssn varchar(11) NOT NULL PRIMARY KEY,
#   last_name varchar(50) NOT NULL,
#   first_name varchar(50) NOT NULL,
#   gender enum('M','F') NOT NULL,
#   age int NOT NULL,
#   clearance_level varchar(50),
#   salary decimal(10,2) NOT NULL,
#   phone_number varchar(15),
#   shift_schedule varchar(50),
#   position varchar(50),
#   address varchar(100),
#   PRIMARY KEY (ssn)
# );

# CREATE TABLE trains (
#   routes varchar(100),
#   train_schedule varchar(50),
#   location varchar(100)
# );

# CREATE TABLE passengers (
#   first_name varchar(50) NOT NULL,
#   last_name varchar(50) NOT NULL,
#   ticket_number varchar(20) NOT NULL,
#   age int NOT NULL,
#   phone_number varchar(15),
#   gender enum('M','F')
# );

# CREATE TABLE service_conditions (
#   engine_cars int,
#   train_station varchar(100),
#   num_passenger_cars int,
#   maintenance_description varchar(255)
# );

# CREATE TABLE delays (
#   estimate_delay_time int,
#   status varchar(50),
#   train_affected int
# );
