import streamlit as st
import mysql.connector
import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.set_page_config(page_title="SQL Chatbot", layout="centered")
st.title("SQL Chatbot for Employee Data")

def generate_sql(user_input):
    prompt = f"""
You are an intelligent SQL assistant for a MySQL database.

The table is called 'employees' and has the following columns:
- id: unique employee ID
- name: name of the employee
- department: department they work in (e.g., HR, Sales, Finance)
- salary: monthly salary in INR
- joining_date: the date they joined the company
- designation: job title
- location: city where the employee is based (e.g., Bangalore, Mumbai)
- experience: years of work experience

When generating SQL queries, follow these rules:

1. Do NOT use LIMIT unless the user specifically asks for:
   - "the first"
   - "only one"
   - "top one"
   - "first X", etc.

2. Always return ALL records that satisfy the condition. Avoid using:
   - LIMIT 1
   - LIMIT X
   - FETCH FIRST ROWS ONLY

3. Use ORDER BY only if the user specifically asks for sorted results like:
   - "sorted by salary"
   - "highest to lowest"
   - "top 3 earners"

4. If the question is about maximum or minimum values (e.g., who earns the most),
   use:
     WHERE column = (SELECT MAX(column) FROM employees)
   so that all matching records are returned.

5. Never use SELECT *.
   Always select only relevant columns — typically 'name' and the attribute being asked (e.g., name and salary, name and experience).
   Only include extra columns if explicitly mentioned.

Convert the following natural language question into a valid MySQL query.
Only return the SQL query, without explanation.

Question:
\"{user_input}\"
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

user_question = st.text_input("Ask me a question about the employees:")

if user_question:
    with st.spinner("Thinking..."):
        try:
            sql_query = generate_sql(user_question)
            st.code(sql_query, language="sql")

            conn = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE")
            )
            df = pd.read_sql(sql_query, conn)
            conn.close()

            if not df.empty:
                st.success("Result:")
                st.dataframe(df)
            else:
                st.warning("No results found.")

        except Exception as e:
            st.error(f"Error: {str(e)}")