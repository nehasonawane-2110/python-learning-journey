# write a program to calculate the percentage using lambda function.
# best of 5 scenario


percentage = lambda marks: (sum(marks) / 500) * 100
marks = [85, 90, 75, 95, 85]  # list of marks obtained in 5 subjects
result = percentage(marks)
print(result)
