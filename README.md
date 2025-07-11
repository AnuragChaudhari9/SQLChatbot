# SQL Chatbot – Natural Language to SQL Query Generator

SQL is a powerful and widely-used language for interacting with structured databases. However, its technical complexity often limits usage to experienced SQL professionals within a company. This chatbot aims to democratize data access by enabling users to write queries in plain English and receive real-time results from a MySQL database.

Powered by **GPT-3.5**, this chatbot translates natural language inputs into valid SQL queries that are executed against a live MySQL database. It simplifies interaction with structured data while preserving query accuracy and execution safety.

---

## Intended Audience & Use Case

This project is ideal for:

- **Data analysts and business users** who need insights but lack SQL knowledge.
- **Developers** building interfaces that enable natural language querying of structured databases.
- **Non-technical decision-makers** who want to independently explore business data.

By using this chatbot, users can access database insights without writing SQL, reducing reliance on technical teams and enabling faster, data-informed decisions.

---

## Features

- Connects to a MySQL table (e.g., `employees`)
- Uses GPT-3.5 to generate SQL queries from natural language
- Executes queries and displays results in real-time
- Secure and schema-aware interaction with the database

## Technologies:
- Python
- OpenAI GPT-3.5
- MySQL
- dotenv
- Streamlit

## How to Run:
1. Create db using `setup_employees.sql` file
2. Convert `.env.example` into `.env`
3. Add your API key and DB credentials in `.env`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app:
   ```streamlit run app.py```
## Examples
![Screenshot (442)](https://github.com/user-attachments/assets/5b10529f-3f0c-44b6-ad36-0790ca688e1d)
![Screenshot (443)](https://github.com/user-attachments/assets/45dbb374-47db-40a7-bc29-9dd77dbae1bc)
![Screenshot (441)](https://github.com/user-attachments/assets/c904444b-25ee-4dcf-b988-7e7d50fed21e)
![Screenshot (440)](https://github.com/user-attachments/assets/9d0b9590-614b-4dbb-8aa4-aef71e5596dc)
![Screenshot (436)](https://github.com/user-attachments/assets/989c6abe-2cf4-4f2e-b481-6008c4e4c31d)
