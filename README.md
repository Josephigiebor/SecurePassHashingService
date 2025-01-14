 # SecurePassHashingService

## 📖 **Project Overview**
The **SecurePassHashingService** is a secure password hashing and verification service designed for use in web applications or personal projects. The service provides a REST API to handle password hashing using industry-standard algorithms such as **bcrypt** and **Argon2**, password verification, and strength evaluation.

Key features include:
- Password hashing with **bcrypt** and **Argon2**.
- Password strength evaluation to ensure secure passwords.
- REST API endpoints for integration with external systems.
- Brute-force resistance through secure hashing methods.
- Comprehensive unit tests for all core functionalities.

---

## 🛠️ **Project Structure**
```
SecurePassHashingService/
├── app.py                 # Main application file
├── hashing/               # Password hashing logic
│   ├── hasher.py          # Hashing and verification functions
│   ├── strength.py        # Password strength checker
│   └── __init__.py
├── api/                   # API implementation
│   ├── routes.py          # API endpoints
│   └── __init__.py
├── tests/                 # Unit tests for the application
│   ├── test_hasher.py     # Tests for hashing functionality
│   ├── test_strength.py   # Tests for strength evaluation
│   ├── test_routes.py     # Tests for API endpoints
│   └── __init__.py
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## 📦 **Installation Instructions**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/SecurePassHashingService.git
cd SecurePassHashingService
```

### **Step 2: Set Up a Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.\.venv\Scripts\activate   # On Windows
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Run the Application**
To start the Flask API server:
```bash
python app.py
```
The server will run on `http://127.0.0.1:5000`.

---

## 🔗 **API Documentation**

### **POST /hash**
Endpoint to hash a password using both **bcrypt** and **Argon2**.

#### Request Body:
```json
{
    "password": "YourPassword123!"
}
```

#### Response:
```json
{
    "bcrypt_hashed": "$2b$12$...",
    "argon2_hashed": "$argon2id$v=..."
}
```

---

### **POST /verify**
Endpoint to verify a password against a given hash.

#### Request Body:
```json
{
    "password": "YourPassword123!",
    "hashed_password": "$2b$12$...",
    "method": "bcrypt"  // or "argon2"
}
```

#### Response:
```json
{
    "is_valid": true
}
```

---

### **POST /strength**
Endpoint to evaluate the strength of a password.

#### Request Body:
```json
{
    "password": "YourPassword123!"
}
```

#### Response:
```json
{
    "strength": "Strong",
    "score": 4,
    "reason": "Password is strong."
}
```

---

## 🧪 **Running Tests**
To run the unit tests for the application, use the following command:
```bash
pytest
```

This will run tests for:
- **Hasher Functions** (`test_hasher.py`)
- **Password Strength Checker** (`test_strength.py`)
- **API Endpoints** (`test_routes.py`)

---

## 🚀 **Deployment**
For production deployment, use **Gunicorn** or a cloud platform like **Heroku**, **AWS**, or **Azure**.

### Example with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📚 **Example Usage**
### Using Postman or cURL:

#### **Hash a Password**:
```bash
curl -X POST http://127.0.0.1:5000/hash -H "Content-Type: application/json" -d '{"password":"SecureP@ss123"}'
```

#### **Verify a Password**:
```bash
curl -X POST http://127.0.0.1:5000/verify -H "Content-Type: application/json" -d '{"password":"SecureP@ss123", "hashed_password":"$2b$12$...", "method":"bcrypt"}'
```

#### **Check Password Strength**:
```bash
curl -X POST http://127.0.0.1:5000/strength -H "Content-Type: application/json" -d '{"password":"SecureP@ss123"}'
```

---

## 📖 **Contributing**
Feel free to fork the repository and submit pull requests. Contributions are welcome!

---

## 📜 **License**
This project is licensed under the MIT License. See the LICENSE file for details.


