import streamlit as st

def render_questions():
    st.title("Loan Calculator")
    salary = st.number_input("What is your net salary:", min_value=0)
    work_experience = st.number_input("How many months of work experience do you have:", min_value=0, format="%d")
    debts = st.number_input("How much do you pay in debts each month:", min_value=0)
    birthdate = st.date_input("What is your date of birth:", min_value=None, max_value=None)
    return salary, work_experience, debts, birthdate

def render_result(maximum_loan_term, maximum_loan_amount):
    st.write("### Maximum Loan Details:")
    st.write(f"- **Maximum Loan Term:** {maximum_loan_term} years")
    st.write(f"- **Maximum Loan Amount:** ${maximum_loan_amount:,.2f}")
