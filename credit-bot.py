import streamlit as st
from datetime import datetime

# Function to calculate the maximum loan term
def calculate_maximum_loan_term(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%m/%d/%Y')
    maximum_age = 75
    maximum_loan_term = min(30, maximum_age - (datetime.now().year - fecha_nacimiento.year))
    return maximum_loan_term

# Function to calculate the maximum loan amount
def calculate_maximum_loan_amount(salary, debts):
    maximum_salary = salary * 0.25
    maximum_loan_amount = max(0, maximum_salary - debts)
    return maximum_loan_amount

# Main function for the loan calculator
def loan_calculator():
    st.title("Calculadora de Préstamos")
    salary = st.number_input("Cuál es tu sueldo líquido:", min_value=0)
    work_experience = st.number_input("Cuántos meses de experiencia laboral tienes:", min_value=0, format="%d")
    debts = st.number_input("Cuánto pagas en deudas cada mes:", min_value=0)
    birthdate = st.date_input("Cuál es tu fecha de nacimiento:", min_value=None)
    if st.button("Calcular"):
        maximum_loan_term = calculate_maximum_loan_term(birthdate.strftime('%m/%d/%Y'))
        if work_experience < 18:
            maximum_loan_amount = 0
        else:
            maximum_loan_amount = calculate_maximum_loan_amount(salary, debts)
        st.write(f"Plazo máximo del préstamo: {maximum_loan_term} años")
        st.write(f"Monto máximo del préstamo: ${maximum_loan_amount:,.2f}")

if __name__ == "__main__":
    loan_calculator()
