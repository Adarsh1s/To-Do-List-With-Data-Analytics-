import streamlit as st
import requests

import subprocess
import time
import requests

# Define Django project path correctly
DJANGO_PROJECT_PATH = "C:\\PP_Project\\todo_analytics\\backend"  # Set your exact path

# Start Django server in the background
def start_django():
    try:
        process = subprocess.Popen(
            ["python", "manage.py", "runserver"], 
            cwd=DJANGO_PROJECT_PATH, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            shell=True
        )
        time.sleep(3)  # Give Django some time to start

        # Check if Django is running
        retries = 5
        for i in range(retries):
            try:
                response = requests.get("http://localhost:8000/")
                if response.status_code == 200:
                    print("✅ Django started successfully")
                    return
            except requests.ConnectionError:
                time.sleep(2)  # Wait and retry

        print("❌ Django failed to start")
    except Exception as e:
        print(f"Error starting Django: {e}")

start_django()



# API Endpoint
API_URL = "http://localhost:8000/api/tasks/"  # Use 'localhost' instead of '127.0.0.1'


# Streamlit UI
st.title("📝 To-Do List with Analytics")

# Fetch tasks from API
response = requests.get(API_URL)
if response.status_code == 200:
    tasks = response.json()
else:
    st.error("Failed to load tasks")

# Show tasks with checkboxes
if tasks:
    for task in tasks:
        checked = st.checkbox(task["title"], value=task["completed"])
else:
    st.write("No tasks found.")

# Input for new tasks
st.subheader("Add a New Task")
new_task = st.text_input("Task Title")
task_description = st.text_area("Task Description")
if st.button("Add Task"):
    task_data = {"title": new_task, "description": task_description, "completed": False}
    response = requests.post(API_URL, json=task_data)
    if response.status_code == 201:
        st.success("Task added successfully!")
        st.experimental_rerun()
    else:
        st.error("Failed to add task")
 
import matplotlib.pyplot as plt

# Task Analytics
completed_tasks = sum(task["completed"] for task in tasks)
pending_tasks = len(tasks) - completed_tasks

st.subheader("📊 Task Completion Overview")

if len(tasks) > 0:
    fig, ax = plt.subplots()
    ax.pie([completed_tasks, pending_tasks], labels=["Completed", "Pending"], autopct="%1.1f%%", colors=["green", "red"])
    st.pyplot(fig)
else:
    st.write("No tasks to display analytics.")
