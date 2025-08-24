import streamlit as st

def main():
    st.set_page_config(page_title="AI Math Tutor", layout="wide")
    st.title("AI Math Tutor")

    st.text_area("Enter your math problem to get a step-by-step solution.")
    if st.button("Solve"):
        st.write("Solving...")
        st.write("Solution:")
        st.write("1. Add 2 and 2")
        st.write("2. The answer is 4")


if __name__ == "__main__":
    main()
