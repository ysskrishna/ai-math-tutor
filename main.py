import streamlit as st
from ai.tutor import get_step_by_step_solution

def create_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #ccc;
            font-size: 1rem;
            padding: 1.8rem 0;
            background-color: #181c28;
            border-radius: 8px;
        '>
            <p style='margin: 0.3rem 0; color: #aaa;'>Built with ❤️ by <strong>Y. Siva Sai Krishna</strong> (@ysskrishna)</p>
            <div style='margin-top: 0.6rem; display: flex; gap: 1.2rem;'>
                <a href="https://github.com/ysskrishna" target="_blank" style="color: #ccc; text-decoration: none; display: flex; align-items: center; gap: 0.3rem;">
                    <img src="https://img.icons8.com/material-rounded/20/ffffff/github.png"/> GitHub
                </a>
                <a href="https://linkedin.com/in/ysskrishna" target="_blank" style="color: #ccc; text-decoration: none; display: flex; align-items: center; gap: 0.3rem;">
                    <img src="https://img.icons8.com/material-rounded/20/ffffff/linkedin.png"/> LinkedIn
                </a>
                <a href="https://github.com/ysskrishna/ai-math-tutor" target="_blank" style="color: #ccc; text-decoration: none; display: flex; align-items: center; gap: 0.3rem;">
                    <img src="https://img.icons8.com/material-rounded/20/ffffff/source-code.png"/> Repository
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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
    

    create_footer()

if __name__ == "__main__":
    main()
