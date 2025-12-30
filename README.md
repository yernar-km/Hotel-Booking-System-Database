# 🏨 Hotel Booking Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-316192.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)

**A modern hotel reservation management system with a graphical user interface**


## 📋 Description

Hotel Booking Management System is a desktop application for managing hotel room reservations. The system provides a user-friendly graphical interface for working with clients, rooms, bookings, and payments.

## ✨ Features

### Core Functionality

| Feature | Description |
|---------|-------------|
| 📋 **Data Display** | View tables for clients, rooms, bookings, employees, services, and payments |
| 🔍 **Client Search** | Search by first or last name using ILIKE pattern matching |
| ➕ **Add Clients** | Registration form for new clients |
| ✏️ **Update Status** | Change room status (available/occupied/maintenance) |
| 🗑️ **Delete Payments** | Remove payment records with confirmation dialog |
| 🧮 **Calculations** | Calculate stay cost (days × price per night) |
| 📊 **Reports** | Booking statistics by room type (GROUP BY aggregation) |
| 🔀 **Cross Join** | Demonstrate all client-service-employee combinations |
| 📈 **Dashboard** | Overview statistics and recent bookings |

### Interface Highlights

- 🎨 Modern dark theme with gradient effects
- ✨ Smooth window fade-in animation
- 🖱️ Interactive buttons with hover effects
- 📱 Responsive tables with scrolling
- 🎯 Informative icons and color coding

## 🛠️ Technologies

- **Python 3.8+** — Core programming language
- **Tkinter** — GUI framework
- **PostgreSQL** — Database management system
- **psycopg2** — PostgreSQL adapter for Python

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hotel-booking-system.git
cd hotel-booking-system
```

### 2. Install Dependencies

```bash
pip install psycopg2-binary
```

### 3. Set Up the Database

Create a PostgreSQL database and run the SQL script to create tables:

```sql
-- Create database
CREATE DATABASE hotel_booking;

-- Connect to the database and create tables
-- (see "Database Structure" section below)
```

### 4. Configure Connection

Open `main.py` and update the connection parameters:

```python
self.db_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'hotel_booking',  # Your database name
    'user': 'postgres',           # Your username
    'password': 'your_password'   # Your password
}
```

### 5. Run the Application

```bash
python main.py
```

## 📸 Screenshots

### Dashboard (Main Screen)
<img width="2083" height="1236" alt="изображение" src="https://github.com/user-attachments/assets/f543287c-224a-4db7-a121-78451997328d" />

*Main screen displaying overall statistics: total clients, bookings, available rooms, and revenue*

### Data View
<img width="2095" height="1245" alt="изображение" src="https://github.com/user-attachments/assets/40596261-a7d5-400f-8ee0-c2604d298713" />


*Viewing the bookings table with client and room information*

### Client Search

<img width="2092" height="1228" alt="изображение" src="https://github.com/user-attachments/assets/d2111c64-951c-469a-9831-30af9a82c55b" />


*Searching for clients by first or last name*

### Add New Client
<img width="2086" height="1235" alt="изображение" src="https://github.com/user-attachments/assets/26e00755-20d2-4633-a399-b960b4a89df4" />


*Form for registering a new client*

### Reports & Statistics
<img width="2092" height="1245" alt="изображение" src="https://github.com/user-attachments/assets/31382c77-af8b-4535-b5e5-393c0d7394d5" />


*Booking statistics grouped by room type*

### Cost Calculations
<img width="2097" height="1234" alt="изображение" src="https://github.com/user-attachments/assets/7e0c83b2-4537-4f92-b32b-f81e4ee90622" />

*Stay cost calculation with computed fields*

## 🗄️ Database Structure

### ER Diagram

```
<img width="1442" height="1064" alt="изображение" src="https://github.com/user-attachments/assets/0a72ea99-3f5f-48b9-9b4e-6885179fb400" />

```

### SQL Schema

```sql
-- Room Types
CREATE TABLE room_types (
    room_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Rooms
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    room_type_id INTEGER REFERENCES room_types(room_type_id),
    price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'available' 
        CHECK (status IN ('available', 'occupied', 'maintenance'))
);

-- Clients
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

-- Employees
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    position VARCHAR(50)
);

-- Services
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2)
);

-- Bookings
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id),
    room_id INTEGER REFERENCES rooms(room_id),
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_price DECIMAL(10, 2),
    CHECK (check_out_date > check_in_date)
);

-- Payments
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    booking_id INTEGER REFERENCES bookings(booking_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50)
);
```

## 📖 Usage

### Viewing Data

1. Click the **"📋 Display Data"** button
2. Select the desired table from the list
3. Data will appear in the table on the right panel

### Searching Clients

1. Click the **"🔍 Search Clients"** button
2. Enter a first or last name in the search field
3. Click **"Search"** to get results

### Adding a Client

1. Click the **"➕ Add Client"** button
2. Fill in all form fields
3. Click **"💾 Save"** to save the record

### Updating Room Status

1. Click the **"✏️ Update Status"** button
2. Enter the Room ID
3. Select a new status from the dropdown
4. Click **"✏️ Update"**

### Deleting a Payment

1. Click the **"🗑️ Delete Payment"** button
2. Enter the Payment ID
3. Confirm the deletion


```

## 🔧 Requirements

- Python 3.8 or higher
- PostgreSQL 13 or higher
- Python libraries:
  - `psycopg2-binary` >= 2.9.0
  - `tkinter` (usually included with Python)






**⭐ If you found this project useful, please give it a star! ⭐**
