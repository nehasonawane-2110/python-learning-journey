# Dictionary Demo example some changes 

employee = {"name": "Kunal Sonawane", "age": 24, "Address": "nashik", "Company": "Propix Pune", "Salary": 30000}  # emp data
print(employee)  # print Whole dictionary (emp Data)
print(employee['name'])  # print value of name key
employee['Address'] = "pune"  # Update value of address key
print(employee)
employee['email'] = "kunal@propix.com"  # add new key value pair in dictionary
print(employee)


for i in employee:
    print(i)  # print only key of dictionary

