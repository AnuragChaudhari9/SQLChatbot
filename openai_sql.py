from openai import OpenAI
from dotenv import load_dotenv
import os
from logger import logger

# Load your OpenAI key from local .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "utils", ".env"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sql_from_question(user_input, table, columns):
    column_list = "\n- ".join(columns)

    prompt = f"""
You are an intelligent SQL assistant that helps generate syntactically correct and efficient SQL queries for MySQL databases.

The table is called '{table}' and has the following columns:
- {column_list}

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
     WHERE column = (SELECT MAX(column) FROM {table})
   so that all matching records are returned.

5. Never use SELECT *.
   Always select only relevant columns — typically 'name' and the attribute being asked (e.g., name and salary, name and experience).
   Only include extra columns if explicitly mentioned.

6. If the user asks whether someone *is* a certain role (e.g., "who are the managers"),
   assume that the keyword might be part of a longer designation (e.g., "HR Manager", "Sales Manager").
   Use `LIKE '%keyword%'` in such cases instead of exact equality.

7. If the user's question contains multiple distinct sub-tasks (e.g., show records AND compute aggregate),
   then **split the request into separate SQL queries**.

   Example:
   User question: "Who all are managers, and what is average salary of all of them?"
   → Should become:
     -- Query 1
     SELECT name, designation FROM {table} WHERE designation LIKE '%Manager%';
     -- Query 2
     SELECT AVG(salary) FROM {table} WHERE designation LIKE '%Manager%';

   NEVER combine aggregate values (like AVG) and raw fields (like name/designation) in a single query unless GROUP BY is used properly.

8. When combining raw columns (like `name`, `designation`) with aggregates (like `AVG(salary)`), always use `GROUP BY` for the non-aggregated columns.

9. If ONLY_FULL_GROUP_BY mode is enabled, avoid selecting columns that aren't in GROUP BY or aggregated.

Only return valid MySQL queries based on the question below. If needed, return multiple SQL queries with clear separation (e.g., -- Query 1, -- Query 2). Do not explain.

Question:
\"{user_input}\"
"""

    logger.info(f"Prompt sent to OpenAI:\n{prompt.strip()}")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    sql_query = response.choices[0].message.content.strip()
    logger.info(f"Generated SQL:\n{sql_query}")
    return sql_query
