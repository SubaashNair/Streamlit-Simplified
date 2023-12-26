import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load or create score data
def load_scores():
    try:
        return pd.read_csv('scores.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['Name', 'Score'])

# Function to save scores
def save_score(name, score):
    df = load_scores()
    new_row = pd.DataFrame({'Name': [name], 'Score': [score]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('scores.csv', index=False)


# Initialize session state
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}

# Quiz Questions
quiz_questions = {
    # [Add 20 Questions Here]
    # Example Question:
    "What does 'pip' stand for?": {
        "options": ["Preferred Installer Program", "Python Installation Package", "Python Interpreter Program", "Package Installer for Python"],
        "answer": "Preferred Installer Program"
    },
    "Which Python keyword is used for defining a function?": {
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    "What is Streamlit primarily used for?": {
        "options": ["Data Analysis", "Web Development", "Machine Learning", "Game Development"],
        "answer": "Web Development"
    },
    "What does HTML stand for?": {
        "options": ["Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyper Text Markup Language", "Hyperlinks Text Mark Language"],
        "answer": "Hyper Text Markup Language"
    },
    "Which of these is a valid Python comment?": {
        "options": ["// comment", "# comment", "<!-- comment -->", "/* comment */"],
        "answer": "# comment"
    },
    # [Questions 6-10]
    "Which of these is not a Python data type?": {
        "options": ["List", "Tuple", "Array", "Dictionary"],
        "answer": "Array"
    },
    "What is a correct syntax to return the first character in a string in Python?": {
        "options": ["x[0]", "x(0)", "x{0}", "first(x)"],
        "answer": "x[0]"
    },
    "In Streamlit, which function is used to write text?": {
        "options": ["st.write()", "st.text()", "st.display()", "st.show()"],
        "answer": "st.write()"
    },
    "Which module in Python is used for web development?": {
        "options": ["Django", "NumPy", "Pygame", "Matplotlib"],
        "answer": "Django"
    },
    "What is the output of print(2 ** 3)?": {
        "options": ["8", "6", "9", "5"],
        "answer": "8"
    },
    # [Questions 11-15]
    "What is the method for adding an element to a list in Python?": {
        "options": ["list.add()", "list.append()", "list.insert()", "list.set()"],
        "answer": "list.append()"
    },
    "Which of the following is used to define a block of code in Python?": {
        "options": ["Curly braces {}", "Parentheses ()", "Indentation", "Square brackets []"],
        "answer": "Indentation"
    },
    "In Streamlit, how do you create a sidebar?": {
        "options": ["st.sidebar()", "st.side()", "st.bar()", "st.navigation()"],
        "answer": "st.sidebar()"
    },
    "What does CSS stand for?": {
        "options": ["Computing Style Sheet", "Creative Style System", "Computer Syntax Sheet", "Cascading Style Sheets"],
        "answer": "Cascading Style Sheets"
    },
    "Which HTML tag is used to define an internal style sheet?": {
        "options": ["<css>", "<style>", "<script>", "<stylesheet>"],
        "answer": "<style>"
    },
    # [Questions 16-20]
    "How do you insert COMMENTS in Python code?": {
        "options": ["//This is a comment", "#This is a comment", "<!--This is a comment-->", "**This is a comment**"],
        "answer": "#This is a comment"
    },
    "Which Python library is used for Machine Learning?": {
        "options": ["NumPy", "PyTorch", "Pandas", "Keras"],
        "answer": "PyTorch"
    },
    "What is the correct file extension for Python files?": {
        "options": [".python", ".py", ".pt", ".pyth"],
        "answer": ".py"
    },
    "In Streamlit, which method is used to add a slider widget?": {
        "options": ["st.slider()", "st.scroll()", "st.selectSlider()", "st.range()"],
        "answer": "st.slider()"
    },
    "Which of these is a Python framework for developing GUI applications?": {
        "options": ["Django", "Flask", "Tkinter", "PyQt"],
        "answer": "Tkinter"
    },
}

# Streamlit app layout
def run_quiz():
    st.title("Python and Streamlit Trivia Quiz")

    # Player name input
    name = st.text_input("Enter your name:")
    if not name:
        st.warning("Please enter your name to start the quiz.")
        st.stop()

    # Display questions and store answers
    for question, details in quiz_questions.items():
        st.subheader(question)
        selected_option = st.radio("Choose an option:", details["options"], key=question)
        st.session_state['answers'][question] = selected_option

    # Submit button
    if st.button("Submit Quiz"):
        score = 0
        for question, details in quiz_questions.items():
            if st.session_state['answers'][question] == details["answer"]:
                score += 1

        # Save score and display results
        save_score(name, score)
        st.write(f"Your final score is: {score}/{len(quiz_questions)}")

        # Show correct answers
        st.subheader("Correct Answers")
        for question, details in quiz_questions.items():
            st.text(f"{question}: {details['answer']}")

        # Displaying overall scores with Seaborn visualization
        st.subheader("Leaderboard")
        score_data = load_scores()
        sns.set_style("darkgrid")
        plt.figure(figsize=(10, 6))
        bar_palette = sns.color_palette("hsv", len(score_data))
        sns.barplot(x='Score', y='Name', data=score_data, palette=bar_palette)
        plt.title("Quiz Scores Leaderboard")
        st.pyplot(plt)

if __name__ == "__main__":
    run_quiz()

