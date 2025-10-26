# HCL_Hackathon - SmartBank - Account Creation
SmartBank - Modular Banking Backend System with secure account creation, authentication, and user management.

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Project Structure](#project-structure)
4. [Setup Instructions](#setup-instructions)
5. [Dependencies](#dependencies)
6. [Security Features](#security-features)
7. [API Endpoints](#api-endpoints)
8. [Features](#features)
9. [Testing](#testing)
10. [Database Schema](#database-schema)
11. [Environment Variables](#environment-variables)
12. [Status Codes](#status-codes)
13. [License](#license)
14. [Contributing](#contributing)
15. [Support](#support)

## Overview
This backend service allows customers to request new bank accounts.  
The flow:
1. Customer chooses account type (Savings, Current, FD)  
2. System generates a unique account number  
3. Customer makes an initial deposit

## Architecture

### Backend (FastAPI + PostgreSQL)
- Controller Layer: REST API endpoints
- Service Layer: Business logic and validations
- Repository Layer: Database operations
- Security: JWT authentication, password hashing with bcrypt

### Frontend (React)
- Modern UI with responsive design
- Login, Register, and Dashboard components
- JWT token management
- Protected routes

## Setup Instructions

### Prerequisites
- Python 3.8+  
- Node.js 14+  
- PostgreSQL 12+  

### Backend Setup
1. Create and activate virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

---
banking-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── controllers/
│   │   │   ├── __init__.py
│   │   │   └── auth_controller.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── auth_service.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── user_repository.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── security.py
│   │       └── dependencies.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── utils/
│   │   │   └── auth.js
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   └── .env
└── README.md


Status Codes

200: Success

201: Created

400: Bad Request

401: Unauthorized

404: Not Found

409: Conflict (e.g., email already exists)

500: Internal Server Error
### Backend (FastAPI + PostgreSQL)
- **Controller Layer:** REST API endpoints  
- **Service Layer:** Business logic and validations  
- **Repository Layer:** Database operations  
- **Security:** JWT authentication, password hashing with bcrypt  

### Frontend (React)
- Modern UI with responsive design  
- Login, Register, and Dashboard components  
- JWT token management  
- Protected routes  

---

## 📁 Project Structure
