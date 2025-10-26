# HCL_Hackathon - SmartBank - Account Creation
SmartBank - Modular Banking Backend System with secure account creation, authentication, and user management.

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Project Structure](#project-structure)
4. [Setup Instructions](#setup-instructions)
5. [Security Features](#security-features)
6. [API Endpoints](#api-endpoints)
7. [Features](#features)
8. [Database Schema](#database-schema)

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

## Project Structure

banking-system/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── config.py
│ │ ├── database.py
│ │ ├── models/
│ │ ├── schemas/
│ │ ├── controllers/
│ │ ├── services/
│ │ ├── repositories/
│ │ └── utils/
│ ├── requirements.txt
│ └── .env
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── services/
│ │ └── utils/
│ ├── package.json
│ └── .env
└── README.md

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

## Security Features

- Passwords hashed with bcrypt
- JWT-based authentication
- Protected routes

## API Endpoints

### Register User
POST /api/auth/register
Body:
{
"email": "user@example.com",
"password": "Password123!",
"full_name": "John Doe"
}

### Login User
POST /api/auth/login
Body:
{
"username": "user@example.com",
"password": "Password123!"
}

### Get Current User (Protected)
GET /api/auth/me
Headers: Authorization: Bearer <token>

## Features

### Backend
- User registration with validation
- Secure password hashing (bcrypt)
- JWT token generation
- User authentication
- Protected endpoints
- Duplicate email prevention
- Error handling

### Frontend
- Responsive UI
- Login & registration forms with validation
- Dashboard displaying user info
- JWT token management
- Protected routes
- Error notifications & loading states


##  Database_Scehma

**Users Table:**
- id
- email
- full_name
- hashed_password
- is_active
- created_at
- updated_at





