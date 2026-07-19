# Employee Management System

emp = {}

ch = 0
while (ch != 6):   # fixed exit condition (6 is exit now)
    print(''' Please select Option from below Menu:
          1) Add Employee
          2) Update Employee
          3) Delete Employee
          4) Search Employee
          5) Display All Employees
          6) Exit''')   # fixed menu

    ch = int(input("Enter your Choice: "))

    if (ch == 1):  # Add Employee
        eid = input("Enter eid: ")   # changed variable name (id → eid)
        name = input("Enter ename: ")
        sal = float(input("Enter Salary: "))
        # eData =','.join([id, name, sal])  # this will convert list to string with comma separated
        eData = f'{eid},{name},{sal}'  # this will convert list to string with comma separated
        emp[eid] = eData

    elif (ch == 2):    # update employee details
        eid = input("Enter id from updating employee details: ")
        if (eid in emp.keys()):     # if id is present in emp dictionary then only we will update employee details otherwise we will show id not found message.
            eData = emp[eid]        # this will get employee details in string format with comma separated
            elist = eData.split(',')   # this will convert string to list with comma separated
            print(elist)

            chk = input("Do you want to change name? (y/n): ")  # y, YES, Y, yes, Yes
            if chk.lower() in ['y', 'yes']:  # (Dynamic input)
                elist[1] = input("Enter new name: ")

            chk = input("Do you want to change salary? (y/n): ")
            if chk.lower() in ['y', 'yes']:
                elist[2] = str(float(input("Enter new salary: ")))  # ensure salary remains numeric

            eData = ','.join(elist)
            emp[eid] = eData   # VERY IMPORTANT (save updated data back)

        else:
            print("Id not Found.")

    elif (ch == 3):  # Delete employee    fixed (removed quotes)
        eid = input("Enter id to delete: ")
        if eid in emp:
            del emp[eid]          # this will delete employee details from emp dictionary using id as key
            print("Employee deleted successfully....")
        else:
            print("Employee id not found.")

    elif (ch == 4):  # Search employee    fixed (removed quotes)
        eid = input("Enter id to search: ")
        if eid in emp:
            print(f"Employee found: {emp[eid]}")
        else:
            print("Employee not found.")

    elif (ch == 5):  # Display all employee    corrected meaning
        if emp:
            print("All Employees:")
            for eid, details in emp.items():
                print(f"{eid}: {details}")
        else:
            print("No employees found.")

    elif (ch == 6):   # Exit    fixed
        print("Thank you for choosing us!")

    else:
        print("Invalid choice...")
