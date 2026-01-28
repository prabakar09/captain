import streamlit as st

st.title("Hello World")
students=[
   {"name": "virat","age":38},
   {"name": "ajith","age":57}
 ]
st.table(students)          