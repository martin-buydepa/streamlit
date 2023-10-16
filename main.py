import streamlit as st
from views import render_questions, render_result
from calculations import calculate_maximum_loan_term, calculate_maximum_loan_amount
import time

def set_session_state(value, salary, work_experience, debts, birthdate):
    def func():
        st.session_state.show_questions = value
        st.session_state.salary = salary
        st.session_state.work_experience = work_experience
        st.session_state.debts = debts
        st.session_state.birthdate = birthdate
    return func

def loan_calculator():
    st.session_state.show_questions = st.session_state.get("show_questions", True)
    
    if st.session_state.show_questions:
        salary, work_experience, debts, birthdate = render_questions()
        st.button("Calculate", on_click=set_session_state(False, salary, work_experience, debts, birthdate))
        
    if not st.session_state.show_questions:
        salary = st.session_state.salary
        work_experience = st.session_state.work_experience
        debts = st.session_state.debts
        birthdate = st.session_state.birthdate
        with st.spinner("Calculating..."):
            time.sleep(2)
            maximum_loan_term = calculate_maximum_loan_term(str(birthdate))
            maximum_loan_amount = calculate_maximum_loan_amount(salary, debts, work_experience)
            render_result(maximum_loan_term, maximum_loan_amount)

if __name__ == "__main__":
    loan_calculator()
