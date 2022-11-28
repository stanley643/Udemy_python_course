service_years= input('How long have you been employed?  ')
salary= input('how much is your salary: ')
if int(service_years)>= 5:
    new_salary = (float(salary) * 0.05) + float(salary)
    print(new_salary)

else:
    print(salary)