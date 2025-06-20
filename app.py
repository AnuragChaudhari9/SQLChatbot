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

user_question = st.text_input("Ask me a question about the employees:")

if user_question:
    with st.spinner("Thinking..."):

        prompt = f"""
You are an intelligent SQL assistant. The table is called 'employees' and has the following columns:
- id: unique employee ID
- name: name of the employee
- department: department they work in
- salary: monthly salary in INR
- joining_date: the date they joined the company
- designation: job title
- location: city where the employee is based
- experience: years of work experience

Use SQL's LIKE operator for partial matches (e.g., WHERE designation LIKE '%Manager%') when appropriate.

Convert the following question into a MySQL query.
Question: "{user_question}"
Only return the SQL query.
"""

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            sql_query = response.choices[0].message.content.strip()
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