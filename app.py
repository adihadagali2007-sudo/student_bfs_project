import streamlit as st
from collections import deque

st.set_page_config(
    page_title="Student Support Path Finder",
    page_icon="🎓"
)


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    explored_order = []

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        explored_order.append(node)

        if node == goal:
            return path, explored_order

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None, explored_order


graph = {
    "Start": ["Identify Weak Subject"],
    "Identify Weak Subject": [
        "Revise Concepts",
        "Ask Teacher"
    ],
    "Revise Concepts": ["Practise Questions"],
    "Ask Teacher": ["Revise Concepts"],
    "Practise Questions": ["Take Mock Test"],
    "Take Mock Test": ["Review Performance"],
    "Review Performance": []
}


st.title("🎓 Student Academic Support Path Finder")
st.subheader("📊 Project Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Nodes", len(graph))

with col2:
    st.metric(
        "Total Connections",
        sum(len(neighbours) for neighbours in graph.values())
    )

with col3:
    st.metric("Algorithm", "BFS")
st.subheader("🗺️ Academic Support Graph")

graph_description = """
digraph AcademicSupport {
    Start -> "Identify Weak Subject";
    "Identify Weak Subject" -> "Revise Concepts";
    "Identify Weak Subject" -> "Ask Teacher";
    "Revise Concepts" -> "Practise Questions";
    "Ask Teacher" -> "Revise Concepts";
    "Practise Questions" -> "Take Mock Test";
    "Take Mock Test" -> "Review Performance";
}
"""

st.graphviz_chart(graph_description)    
st.subheader("About This Project")

st.write(
    "This project demonstrates Breadth-First Search (BFS) "
    "to find a pathway through academic support activities."
)

st.write("*Algorithm:* Breadth-First Search (BFS)")
st.write("*Data structure:* FIFO Queue")
st.write("*Programming language:* Python")
st.write("*User interface:* Streamlit")

st.write(
    "Find a study-support pathway using "
    "Breadth-First Search (BFS)."
)

st.info(
    "This educational project demonstrates a search algorithm. "
    "It does not predict official examination results."
)

st.header("Enter Student Details")

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

name = st.text_input(
    "Student Name",
    key="student_name"
)

study_hours = st.slider(
    "Study Hours Per Day", 0, 12, 4
)

attendance = st.slider(
    "Attendance Percentage", 0, 100, 75
)

previous_marks = st.slider(
    "Previous Exam Marks", 0, 100, 50
)

goal = st.selectbox(
    "Choose your goal",
    list(graph.keys()),
    index=6
)

if st.button("Find Academic Support Path"):
    if not name.strip():
        st.warning("Please enter the student's name.")
        st.stop()
    
    
    if attendance < 75 or previous_marks < 40:
        st.metric("Academic Support Priority", "High")
    elif study_hours < 2:
        st.metric("Academic Support Priority", "Medium")
    else:
        st.metric("Academic Support Priority", "Normal")
   
    st.subheader("Personalised Study Advice")
    if attendance < 75:
        st.warning(
            "Priority: Improve attendance and check your "
            "college attendance requirements."
        )
    elif previous_marks < 40:
        st.warning(
            "Priority: Revise basic concepts and practise "
            "previous exam questions."
        )
    elif study_hours < 2:
        st.info(
            "Priority: Create a regular daily study routine."
        )
    else:
        st.success(
            "Keep following your study routine and test "
            "your understanding with mock questions."
        )


    path, explored_order = bfs(graph, "Start", goal)

    st.subheader("Student Summary")
    import pandas as pd

    student_data = {
        "Detail": [
            "Student Name",
            "Study Hours Per Day",
            "Attendance",
            "Previous Exam Marks"
        ],
        "Value": [
            name if name else "Not provided",
            f"{study_hours} hours",
            f"{attendance}%",
            f"{previous_marks}%"
        ]
    }

    st.table(pd.DataFrame(student_data))
    st.write("Student:", name if name else "Not provided")
    st.write("Study hours per day:", study_hours)
    st.write("Attendance:", f"{attendance}%")
    st.write("Previous exam marks:", f"{previous_marks}%")

    st.subheader("BFS Academic Support Path")

    if path:
       st.subheader("BFS Node Exploration Order")
       st.write(" → ".join(explored_order))
       st.subheader("Your Academic Support Journey")
       for step_number, step in enumerate(path, start=1):
        st.info(f"Step {step_number}: {step}")
        if step_number < len(path):
            st.write("⬇️")

        st.subheader("BFS Result")
        st.write(" → ".join(path))
        st.write("Total steps:", len(path) - 1)

    else:
        st.error("No support pathway found.")
with st.expander("📘 How does BFS work?"):
    st.write(
        "Breadth-First Search (BFS) is an uninformed "
        "search algorithm that explores nodes level by level."
    )

    st.write("**Steps followed by BFS:**")

    st.write("1. Start from the initial node.")
    st.write("2. Insert nodes into a FIFO queue.")
    st.write("3. Remove the first node from the queue.")
    st.write("4. Check whether it is the goal node.")
    st.write("5. Add unvisited neighbouring nodes to the queue.")
    st.write("6. Continue until the goal is found or the queue is empty.")

    st.write(
        "**Data structures used:** Queue and visited set."
    )

    st.write(
        "**Time complexity:** O(V + E), using an adjacency-list "
        "graph and standard BFS."
    )
st.divider()

st.caption(
    "BCA Artificial Intelligence Project | "
    "Student Academic Support Path Finder | "
    "Algorithm: Breadth-First Search (BFS)"
)
def reset_student_name():
    st.session_state.student_name = ""

st.button(
    "Reset Form",
    on_click=reset_student_name
)