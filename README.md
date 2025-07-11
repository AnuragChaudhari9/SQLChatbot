# SQL Chatbot Using OpenAI & MySQL

This chatbot accepts natural language questions and returns results from a real MySQL database using GPT-3.5.

## Features:
- Connects to a MySQL table (`employees`)
- Uses GPT to generate SQL queries
- Executes query and displays result

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
