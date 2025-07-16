import streamlit as st
from utils.env_loader import load_env_file
from utils.sql_tools import create_sqlalchemy_engine, get_schema_overview
from openai_sql import generate_sql_from_question
from logger import logger
import pandas as pd
from sqlalchemy.sql import text

st.set_page_config(page_title="SQL-GPT Assistant", layout="centered")
st.title("🧠 SQL Chatbot with MLOps 🔧")

st.markdown("### Step 1: Upload your `.env` file to connect to your database")

uploaded_env = st.file_uploader("Upload .env file", type="env")

if uploaded_env is not None:
    env_dict = load_env_file(uploaded_env)

    if env_dict:
        st.success("✅ .env file loaded!")
        logger.info(".env file loaded by user.")

        try:
            engine = create_sqlalchemy_engine(env_dict)
            logger.info("Successfully connected to database.")
            schema = get_schema_overview(engine)

            selected_table = st.selectbox("📋 Select a table to explore:", list(schema.keys()))
            if selected_table:
                logger.info(f"User selected table: {selected_table}")
                st.markdown("### Columns in this table:")
                st.code(", ".join(schema[selected_table]))

                st.markdown("### Step 2: Ask your question in natural language")
                user_question = st.text_input("💬 Your question:")

                if st.button("Generate SQL and Run"):
                    with st.spinner("Generating and executing..."):
                        try:
                            logger.info(f"User question: {user_question}")
                            query = generate_sql_from_question(user_question, selected_table, schema[selected_table])
                            st.markdown("#### 🤖 GPT-Generated SQL Query:")
                            st.code(query)

                            queries = query.strip().split(";")
                            for i, q in enumerate(queries):
                                if q.strip():
                                    with engine.connect().execution_options(autocommit=True) as conn:
                                        df = pd.read_sql(text(q.strip()), con=conn)
                                        st.success(f"✅ Result of Query {i+1}:")
                                        st.dataframe(df)
                                        logger.info(f"Query {i+1} executed successfully:\n{q.strip()}")

                        except Exception as e:
                            st.error(f"❌ Error while running query:\n{e}")
                            logger.exception(f"Query execution failed:\n{e}")
        except Exception as e:
            st.error(f"❌ Could not connect to the database:\n{e}")
            logger.exception("Database connection failed.")
