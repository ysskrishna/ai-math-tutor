import streamlit as st
from ai.tutor import get_step_by_step_solution

SAMPLE_PROBLEMS = [
    "Solve for x: 2x + 5 = 13",
    "Find the area of a circle with radius 7 cm", 
    "A train travels 240 miles in 4 hours. What is its average speed?"
]

def display_sample_questions():
    with st.expander("Try Sample Problems", expanded=False):
        st.markdown("Click on any problem below to auto-populate the input field:")
        
        for i, problem in enumerate(SAMPLE_PROBLEMS):
            if st.button(
                f"📝 {problem}", 
                key=f"sample_{i}",
                use_container_width=True,
                help="Click to use this sample problem"
            ):
                st.session_state.problem_input = problem
                st.rerun()

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

def display_solution(solution):
    st.markdown("---")
    st.subheader("Solution")
    
    for i, step in enumerate(solution.steps, 1):
        st.markdown(f"**Step {i}:** {step.explanation}")
        
        st.code(step.output, language="text")
        
        if i < len(solution.steps):
            st.markdown("")
    
    st.markdown("---")
    st.success(f"**🎯 Final Answer:** {solution.final_answer}")

def handle_problem_input():
    problem = st.text_area(
        "Enter your math problem to get a step-by-step solution:", 
        height=150,
        placeholder="Example: Solve for x: 2x + 5 = 13",
        key="problem_input"
    )
    
    # Button row
    button_col1, button_col2, button_col3 = st.columns([1, 1, 2])
    
    with button_col1:
        if st.button("Submit", use_container_width=True):
            if problem.strip():
                with st.spinner("Let me put on my thinking cap and solve this mathematical mystery..."):
                    try:
                        st.session_state.solution = get_step_by_step_solution(problem)
                    except Exception as e:
                        st.session_state.solution = f"Error: {str(e)}"
            else:
                st.error("Please enter a math problem first.")
    
    with button_col2:
        if st.button("Reset", use_container_width=True):
            st.session_state.solution = None
            if 'problem_input' in st.session_state:
                del st.session_state.problem_input
            st.rerun()
    
    return problem

def main():
    st.set_page_config(page_title="AI Math Tutor", layout="wide")
    st.title("AI Math Tutor")

    st.session_state.setdefault('solution', None)
    st.session_state.setdefault('problem_input', "")

    display_sample_questions()

    handle_problem_input()

    # Display solution if available
    if st.session_state.solution:
        display_solution(st.session_state.solution)

    # Create footer
    create_footer()

if __name__ == "__main__":
    main()
