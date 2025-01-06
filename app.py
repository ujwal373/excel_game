import streamlit as st
import random

# Expanded question bank with 30 distinct questions
question_bank = [
    {"riddle": "Sum the sales figures in cells B2 to B10.", "answer": "=SUM(B2:B10)", "hint": "=SUM", "level": "Nerd"},
    {"riddle": "Find the average sales figures in column C.", "answer": "=AVERAGE(C:C)", "hint": "=AVERAGE", "level": "Nerd"},
    {"riddle": "Find the total sales for all items excluding 'Bananas' in column A and sales in column B.", "answer": "=SUMIF(A:A, \"<>Bananas\", B:B)", "hint": "=SUMIF", "level": "Legend"},
    {"riddle": "Retrieve the 5th highest salary from the list in column C.", "answer": "=LARGE(C:C, 5)", "hint": "=LARGE", "level": "Advance"},
    {"riddle": "Find the price of 'Apples' from the product list in column A and prices in column B.", "answer": "=VLOOKUP(\"Apples\", A:B, 2, FALSE)", "hint": "=VLOOKUP", "level": "Pro"},
    {"riddle": "Count the number of non-empty cells in column D.", "answer": "=COUNTA(D:D)", "hint": "=COUNTA", "level": "Nerd"},
    {"riddle": "Find the sum of all sales in column B where the product is 'Oranges'.", "answer": "=SUMIF(A:A, \"Oranges\", B:B)", "hint": "=SUMIF", "level": "Pro"},
    {"riddle": "Average the sales in column B for rows where column A is 'Apples'.", "answer": "=AVERAGEIF(A:A, \"Apples\", B:B)", "hint": "=AVERAGEIF", "level": "Pro"},
    {"riddle": "Show the minimum salary from the list in column D.", "answer": "=MIN(D:D)", "hint": "=MIN", "level": "Nerd"},
    {"riddle": "Find the maximum sales figure in column B.", "answer": "=MAX(B:B)", "hint": "=MAX", "level": "Nerd"},
    {"riddle": "Show the number of occurrences of 'Bananas' in column A.", "answer": "=COUNTIF(A:A, \"Bananas\")", "hint": "=COUNTIF", "level": "Nerd"},
    {"riddle": "Extract the first 3 characters from the string in cell A1.", "answer": "=LEFT(A1, 3)", "hint": "=LEFT", "level": "Nerd"},
    {"riddle": "Extract the last 3 characters from the string in cell A1.", "answer": "=RIGHT(A1, 3)", "hint": "=RIGHT", "level": "Nerd"},
    {"riddle": "Concatenate the values in cells A1 and B1 with a space in between.", "answer": "=A1 & \" \" & B1", "hint": "Concatenate", "level": "Nerd"},
    {"riddle": "Convert text in cell A1 to uppercase.", "answer": "=UPPER(A1)", "hint": "=UPPER", "level": "Nerd"},
    {"riddle": "Convert text in cell A1 to lowercase.", "answer": "=LOWER(A1)", "hint": "=LOWER", "level": "Nerd"},
    {"riddle": "Replace the first occurrence of 'Apple' with 'Mango' in the string in A1.", "answer": "=SUBSTITUTE(A1, \"Apple\", \"Mango\", 1)", "hint": "=SUBSTITUTE", "level": "Pro"},
    {"riddle": "Check if the value in cell A1 is greater than 100.", "answer": "=IF(A1 > 100, \"Yes\", \"No\")", "hint": "=IF", "level": "Legend"},
    {"riddle": "Find the length of the string in cell A1.", "answer": "=LEN(A1)", "hint": "=LEN", "level": "Nerd"},
    {"riddle": "Count the number of cells with numeric values in column B.", "answer": "=COUNT(B:B)", "hint": "=COUNT", "level": "Nerd"},
    {"riddle": "Find the current date.", "answer": "=TODAY()", "hint": "=TODAY", "level": "Nerd"},
    {"riddle": "Find the current time.", "answer": "=NOW()", "hint": "=NOW", "level": "Nerd"},
    {"riddle": "Round the number in cell A1 to two decimal places.", "answer": "=ROUND(A1, 2)", "hint": "=ROUND", "level": "Pro"},
    {"riddle": "Find the 3rd smallest number in the list in column C.", "answer": "=SMALL(C:C, 3)", "hint": "=SMALL", "level": "Pro"},
    {"riddle": "Retrieve the name of the month from the date in cell A1.", "answer": "=TEXT(A1, \"mmmm\")", "hint": "=TEXT", "level": "Pro"},
    {"riddle": "Join the values in cells A1, B1, and C1 into a single string with commas.", "answer": "=TEXTJOIN(\", \", TRUE, A1, B1, C1)", "hint": "=TEXTJOIN", "level": "Pro"},
    {"riddle": "Find the year of the date in cell A1.", "answer": "=YEAR(A1)", "hint": "=YEAR", "level": "Pro"},
    {"riddle": "Count the number of rows with data in column A.", "answer": "=COUNTA(A:A)", "hint": "=COUNTA", "level": "Nerd"},
    {"riddle": "Add up the sales in column B for all rows where column A is not 'Apples'.", "answer": "=SUMIF(A:A, \"<>Apples\", B:B)", "hint": "=SUMIF", "level": "Legend"},
    {"riddle": "Apply a conditional formatting rule to highlight cells in column B that are greater than 500.", "answer": "Conditional Formatting > Highlight Cells > Greater Than > 500", "hint": "Conditional Formatting", "level": "Legend"},
    {"riddle": "Calculate the average of numbers in cells B2 to B10, excluding zeros.", "answer": "=AVERAGEIF(B2:B10, \"<>0\")", "hint": "=AVERAGEIF", "level": "Pro"},
    {"riddle": "Find the total sales excluding blanks in column B.", "answer": "=SUMIF(B:B, \"<>\" )", "hint": "=SUMIF", "level": "Pro"}
]

random.shuffle(question_bank)  # Shuffle the question bank

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'questions' not in st.session_state:
    st.session_state.questions = question_bank
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Reset game
def reset_game():
    st.session_state.score = 0
    st.session_state.questions = random.sample(question_bank, len(question_bank))

# Game intro
st.title("Formula Frenzy: Data Wranglers' Showdown")
st.write("Think you're an Excel genius? Time to see if your ‘**Nerd**’, ‘**Pro**’ & '**Master**' titles are actually worth anything. Flex those formulas, or risk getting utterly destroyed. You might earn the ‘**Legend**’ title… or end up looking like a total joke. Even the best spreadsheet warriors get humbled. Ready for your crushing defeat? Let the showdown begin… if you dare.")

# Enter user name
if st.session_state.user_name == "":
    st.session_state.user_name = st.text_input("What’s Your Name, or Should I Just Call You ‘Failed’?")
    if st.session_state.user_name:
        st.rerun()
st.subheader("– By Ujwal Mojidra")

# Display questions
if st.session_state.user_name:
    # Display all questions
    with st.form(key="questions_form"):
        st.subheader(f"Prepare to Be Excel-lent… Or Not my dear {st.session_state.user_name} 🤣")
        
        # Store answers
        answers = {}
        
        for i, question in enumerate(st.session_state.questions):
            st.write(f"**{i+1}.** {question['riddle']}")
            user_answer = st.text_input(f"Your answer for question {i+1}:", key=f"q{i}")
            answers[i] = user_answer
        
        submit_button = st.form_submit_button("Submit Answers")
        
    # Show hints outside the form
    if st.button("Got a Clue?"):
        for i, question in enumerate(st.session_state.questions):
            st.write(f"**Hint for question {i+1}:** {question['hint']}")

    # Submit answers
    if submit_button:
        # Calculate score
        for i, question in enumerate(st.session_state.questions):
            if answers[i].strip().lower() == question['answer'].strip().lower():
                st.session_state.score += 1
            
        st.write(f"Your score: {st.session_state.score}")

        # Display rankings
        if st.session_state.score == 30:
            st.write("You are a **Formula Master**!🫡 Are you sure? Because you’re too good!")
        elif 20 <= st.session_state.score < 30:
            st.write("You are a **Master**! 😏 Not bad, but still a few secrets left to uncover…")
        elif 10 <= st.session_state.score < 20:
            st.write("You are a **Pro**! 🥲 Cute, but we both know you’re not invincible…")
        elif 1 <= st.session_state.score < 10:
            st.write("You are a **Nerd**! 🤡 Nice try, but you’re in the shallow end, my friend…")
        else:
            st.write("You are an **Excel Newbie**! Don’t worry, you’ll get there… maybe in another lifetime…🫢")
        
        st.button("Play Again", on_click=reset_game)
    
