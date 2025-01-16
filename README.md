# Django Project

## Installation and Setup

### Prerequisites
- Python (3.7 or later)
- pip (Python package manager)
- virtualenv (optional, but recommended)
- SQLite (default database for Django)

### Steps to Set Up the Project
1. Clone the Repository:
   
   git clone <repository-url>
   cd <repository-name>
   

2. Create a Virtual Environment (Optional):
   
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. Install Required Packages:
   
   pip install -r requirements.txt
   

4. Run Migrations:
   
   python manage.py makemigrations
   python manage.py migrate
   

5. Start the Development Server:
   
   python manage.py runserver
   

6. Access the Application:
   Visit http://127.0.0.1:8000/ in your browser.

## API Endpoints

### 1. Register User
   - Endpoint: POST /register/
   - Description: Registers a new user.
   - Request Body:
     
     {
         "username": "<username>",
         "password": "<password>"
     }
     
   - Response:
     - 201 Created:
       
       {
           "message": "User created successfully"
       }
       
     - 400 Bad Request:
       
       {
           "error": "Invalid username or password"
       }
       

### 2. Login User
   - Endpoint: POST /login/
   - Description: Authenticates a user and generates a token.
   - Request Body:
     
     {
         "username": "<username>",
         "password": "<password>"
     }
     
   - Response:
     - 200 OK:
       
       {
           "message": "Login successful",
           "token": "<generated_token>"
       }
       
     - 400 Bad Request:
       
       {
           "error": "Invalid username"
       }
       
       or
       
       {
           "error": "Invalid password"
       }
       

### 3. Chat Interaction
   - Endpoint: POST /chat/
   - Description: Sends a chat message and deducts 100 tokens per message.
   - Headers:
     

     Authorization: <user_token>
     
   - Request Body:
     
     {
         "message": "<message_text>"
     }
     
   - Response:
     - 201 Created:
       
       {
           "message": "<message_text>",
           "response": "Response to <message_text>"
       }
       
     - 400 Bad Request:
       
       {
           "error": "Invalid message"
       }
       
       or
       
       {
           "error": "Insufficient tokens"
       }
       
     - 401 Unauthorized:
       
       {
           "error": "Unauthorized"
       }
       

### 4. Check Token Balance
   - Endpoint: GET /tokens/
   - Description: Retrieves the remaining token balance for a user.
   - Headers:
     

     Authorization: <user_token>
     
   - Response:
     - 200 OK:
       
       {
           "tokens": <remaining_tokens>
       }
       
     - 401 Unauthorized:
       
       {
           "error": "Unauthorized Token Not Found"
       }
       

## Models

### User Model
- username: Unique username (max length: 50)
- password: Hashed password
- tokens: Integer field (default: 4000)
- token: User authentication token

### Chat Model
- user: Foreign key to the User model
- message: Text of the user's message
- response: System-generated response
- timestamp: Auto-generated timestamp of the chat

## Additional Notes
- Use the Authorization header with the token received during login for authenticated endpoints.
- Default database is SQLite. For production, switch to a robust database like PostgreSQL.
- Create a superuser for admin panel access:
  
  python manage.py createsuperuser
  
- Admin panel: http://127.0.0.1:8000/admin/