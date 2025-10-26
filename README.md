 # HCL_Hackathon - SmartBank - Account Creation

  **Usecase 2**

A sleek, full-stack **banking application** that brings **account creation** to life with **FastAPI**, **React**, and **PostgreSQL**. Designed for hackathons, built for real-world clarity, and engineered to impress!  

##  Table of Contents
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Setup Instruction](#-setup-instruction)
- [Backend Setup (FastAPI + PostgreSQL)](#-backend-setup-fastapi--postgresql)
- [Frontend Setup (React.js)](#-frontend-setup-reactjs)
- [API Endpoint](#-api-endpoint)
- [Technologies Used](#-technologies-used)
- [Flow Summary](#-flow-summary)
- [Key Highlights](#-key-highlights)

## Features

- **Create New Accounts** effortlessly:  
  - Savings  
  - Current  
  - Fixed Deposit (FD)  
- **Automatic 16-digit account numbers** – unique & secure  
- **Smart deposit validation**:  
  - Savings: Min $500  
  - Current: Min $1000  
  - FD: Min $5000  
- Clean **Controller → Service → Repository architecture**  
- Fast, lightweight, and intuitive **REST API** with **FastAPI**  
- Beautiful **React frontend** for instant account creation  

## Project Structure

```banking-system/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── config.py
│ │ ├── database.py
│ │ ├── models/
│ │ │ └── account_model.py
│ │ ├── controllers/
│ │ │ └── account_controller.py
│ │ ├── services/
│ │ │ └── account_service.py
│ │ ├── repositories/
│ │ │ └── account_repository.py
│ │ ├── schemas/
│ │ │ └── account_schema.py
│ │ └── utils/
│ │ └── helpers.py
│ ├── requirements.txt
│ └── README.md
└── frontend/
├── src/
│ ├── components/
│ │ └── AccountForm.js
│ ├── App.js
│ ├── index.js
│ └── api/
│ └── accountApi.js
└── package.json 
```

## Setup Instruction

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+

## Backend Setup (FastAPI + PostgreSQL)

# Clone the repo
git clone <repo-url>
cd banking-system/backend

# Install dependencies
pip install -r requirements.txt

# Set environment variables
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=banking_db

# Run FastAPI server
uvicorn app.main:app --reload

## Frontend Setup (React.js)

cd ../frontend
npm install
npm start

##  API Endpoint

| Endpoint      | Method | Request Body                                           | Response                                           |
|---------------|--------|--------------------------------------------------------|--------------------------------------------------|
| `/accounts/`  | POST   | `{"account_type": "savings", "initial_deposit": 1000}` | `{"account_number": "...", "account_type": "savings", "initial_deposit": 1000}` |

## Technologies Used

- **Backend:** FastAPI, SQLAlchemy, PostgreSQL  
- **Frontend:** React.js, Axios  
- **Others:** Python, Pydantic, dotenv

## Flow Summary

1. **User selects account type** (Savings, Current, FD)  
2. **Backend validates the initial deposit**  
3. **System generates a unique 16-digit account number**  
4. **Account saved in PostgreSQL**  
5. **Response returned to frontend**

## Key Highlights

- **Strict validation of minimum deposits**  
- **Automatic unique account number generation**  
- **Controller-Service-Repository pattern** for clean, maintainable code
