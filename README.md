# Real-Estate-Management-System

This project is a command-line based Real Estate Management System built with **Python** and **PostgreSQL**. It allows estate agents to manage properties (apartments and houses), handle client data, and generate contracts for rentals or purchases.

## 📁 Project Structure
├── database.py # PostgreSQL connection setup
├── estate_agent.py # Agent account management (create, login, delete)
├── estate.py # CRUD operations for estates (apartment/house)
├── contract.py # Person and contract creation/listing
├── main.py # CLI interface and menu system
├── schema.sql # SQL file to initialize database tables

---

## 🧩 Database Schema

This project uses a **vertical inheritance model** in the PostgreSQL database.

### Core Tables

- `estate_agent`: Stores agent login credentials and profile.
- `estate`: Parent table for all real estate items.
- `apartment`: Inherits from `estate`, contains rental-specific fields.
- `house`: Inherits from `estate`, contains sale-specific fields.
- `person`: Represents individuals who rent or buy property.
- `contract`: Base contract table.
- `tenancy_contract`: Inherits from `contract`, includes rental details.
- `purchase_contract`: Inherits from `contract`, includes purchase details.

Refer to `schema.sql` for full table definitions and relationships.

---

## ⚙️ Features

### 👤 Agent Management
- Create estate agent accounts (requires admin password).
- Login and manage properties.
- Delete agent accounts.

### 🏘️ Estate Management
- Create, update, delete estates.
- Choose between apartment or house when creating.
- Only the agent who created the estate can modify/delete it.

### 📑 Contract Management
- Insert new clients (persons).
- Create contracts (rental or purchase).
- View all contracts in the system.

---

## 🛠️ Setup Instructions

### 1. Database (PostgreSQL)
Make sure you have PostgreSQL installed and running.
This project connects to a PostgreSQL database using localhost, with a local username and password.
Simply connect to your own database instance with your own credentials (no external or predefined database is required).


#### 2. Python Dependencies
pip install psycopg2


Edit database.py and update the connection parameters:

#### 3. Database Configuration

Edit database.py and update the connection parameters:

connection = psycopg2.connect(
    dbname='<your_database>',
    user='<your_username>',
    password='<your_password>',
    host='localhost'  # or your database host
)

## 🔒 Admin Password

To access agent management mode, use the hardcoded admin password (estate_agent.py): 1234
