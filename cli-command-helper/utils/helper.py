import platform
from datetime import datetime

# 🔹 Detect OS (Linux / Windows / Mac)
def get_os():
    return platform.system()


# 🔹 Clean AI output (remove unwanted chars)
def clean_text(text):
    return text.strip().replace("```", "").replace("`", "")


# 🔹 Format output nicely
def format_output(explanation, command):
    return f"""
🧠 Explanation:
{explanation}

💻 Command:
{command}
"""


# 🔹 Save history to file
def save_history(task, output):
    with open("history.txt", "a") as f:
        f.write(f"\n[{datetime.now()}]\nTask: {task}\n{output}\n")


# 🔹 Simple logger (for debugging)
def log(message):
    print(f"[DEBUG] {message}")
