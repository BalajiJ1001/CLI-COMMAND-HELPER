import streamlit as st
from core.ai_engine import ask_ai

def extract_parts(output):
    explanation = ""
    command = ""

    lines = output.split("\n")

    for i, line in enumerate(lines):
        if "explanation" in line.lower():
            explanation = line.split(":", 1)[-1].strip()

        if "command" in line.lower():
            parts = line.split(":", 1)
            if len(parts) > 1 and parts[1].strip():
                command = parts[1].strip().strip("`")
            elif i + 1 < len(lines):
                command = lines[i + 1].strip().strip("`")

    return explanation, command

st.title("💻 CLI Command Helper Agent")

user_input = st.text_input("Ask me a task:")

if st.button("Generate"):
    with st.spinner("Generating your command....."):
        output = ask_ai(user_input)
    explanation, cmd = extract_parts(output)
    st.subheader("Explanation")     
    st.write(explanation)

    st.subheader("💻 Command")
    if cmd:
        st.code(cmd, language="bash")
