import streamlit as st
from ai.tutor import get_step_by_step_solution

def main():
    st.set_page_config(page_title="AI Math Tutor", layout="wide")
    st.title("AI Math Tutor")

    problem = st.text_area("Enter your math problem to get a step-by-step solution:", key="problem")
    if st.button("Submit"):
        if problem:
            solution = get_step_by_step_solution(problem)
            st.write(solution)
        else:
            st.error("Please enter a math problem first.")

if __name__ == "__main__":
    main()
