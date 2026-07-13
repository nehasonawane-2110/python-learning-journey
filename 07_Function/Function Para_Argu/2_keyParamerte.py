# 2) Keyword Paramerter/ argument.
# A keyword parameter means we pass arguments to a function using the parameter name (keyword) while calling the function.
# so the order of argument do not matter
# Example-
# 1. Assisging value to para/ argu in the function call
# 2. flow is right to left
# 3. Neglecting position para/ argu concept.

def emp(id, name, dept, sal):
    print("ID:", id)
    print("NAME:", name)
    print("DEPARTMENT:", dept)
    print("SALARY:", sal)


emp(101, "Neha Sonawane", sal=100000, dept="Computer engg")

