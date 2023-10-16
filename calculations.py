from datetime import datetime

def calculate_maximum_loan_term(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    maximum_age = 75
    maximum_loan_term = min(30, maximum_age - (datetime.now().year - fecha_nacimiento.year))
    return maximum_loan_term

def calculate_maximum_loan_amount(salary, debts, work_experience):
    if work_experience < 18:
        return 0
    maximum_salary = salary * 0.25
    maximum_loan_amount = max(0, maximum_salary - debts)
    return maximum_loan_amount
