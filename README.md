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
![Screenshot (202)](https://github.com/user-attachments/assets/793ada4e-d523-49fa-b271-277ecacc85fc)
![Screenshot (201)](https://github.com/user-attachments/assets/71b3503d-9c69-4963-8fff-935477e5f038)
![Screenshot (203)](https://github.com/user-attachments/assets/dbda20d4-9b5b-4c60-a7f7-9502598c34b9)
![Screenshot (436)](https://github.com/user-attachments/assets/39b6505d-8608-4bb9-9831-708da22710c9)
