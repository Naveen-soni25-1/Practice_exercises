import streamlit as st
from pathlib import Path
import json

# File to store the tasks
File = Path("todo.json")

# Load tasks from file
def load_file():
    if File.exists():
        return json.loads(File.read_text())
    return []

# Save tasks to file
def save_file(todos):
    File.write_text(json.dumps(todos, indent=2))

# Page layout
st.title("📝 To-Do App")
st.markdown("An app to manage your daily tasks efficiently.")

# Load existing tasks
todo = load_file()

# Add new task
new_task = st.text_input("Add New Task:")
if st.button("Add Task") and new_task.strip():
    todo.append({"Task": new_task.strip(), "Done": False})
    save_file(todo)
    st.success(f"Task '{new_task}' added!")
    st.rerun()

# Show tasks with checkboxes
st.subheader("Your Tasks:")
for i, item in enumerate(todo):
    checked = st.checkbox(item["Task"], value=item["Done"], key=f"task_{i}")
    if checked != item["Done"]:
        todo[i]["Done"] = checked
        save_file(todo)
        st.rerun()

# Delete task dropdown
if todo:
    st.subheader("Delete a Task:")
    task_names = [item["Task"] for item in todo]
    selected_task = st.selectbox("Select a task to delete:", task_names)
    if st.button("Delete Selected Task"):
        todo = [item for item in todo if item["Task"] != selected_task]
        save_file(todo)
        st.success(f"Task '{selected_task}' deleted!")
        st.rerun()
else:
    st.info("No tasks to delete.")