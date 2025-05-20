Restaurant-Management-System/
│
├── main.py                  # Entry point of the application
├── README.md                # Project documentation
├── Document/                # Contains documentation links
├── SRC/                     # Source code
│   ├── Authentication/      # User login and signup (admin/staff)
│   │   ├── login.py
│   │   └── sign_up.py
│   │
│   ├── Database/            # Stores data in JSON format
│   │   ├── alltables.json
│   │   ├── foodmenu.json
│   │   ├── order_bill.json
│   │   ├── orderplaced.json
│   │   ├── registered_admin.json
│   │   └── registered_staff.json
│   │
│   ├── Domain/              # Core features of the system
│   │   ├── Bill/
│   │   ├── Menu/
│   │   ├── Order/
│   │   ├── Path/
│   │   ├── Payment/
│   │   ├── ReadFile/
│   │   ├── Report/
│   │   ├── StartMenu/
│   │   ├── Table/
│   │   └── Validation/


### 💡 Features
## Authentication System

Staff can sign up and login

Admin can login only

Validates user via JSON files

## Menu Management

Admin can add, remove, update, and view food items

## Order Management

Place and cancel orders

Track orders per table

## Billing

Generates bill after payment

Seat reset after transaction

## Table Management

Admin can add tables and view table list

## Payment Options

Supports multiple payment methods

Handles order cancellation refunds or resets

## Reports

Admin can view error logs and order reports

## Error Logging

Logs errors for administrative review

### 📚 OOP Concepts Used
Abstraction

Inheritance

