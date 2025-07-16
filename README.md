"# Sweet Shop Management System" 
# Sweet Shop Management System

## ✅ Setup 

### ✅ 1. Sweet Model (OOP using @dataclass)
- File: `models/sweet.py`
- Represents a sweet with id, name, category, price, quantity.

### ✅ 2. SQLite Database Setup
- File: `database/db.py`
- Automatically creates `sweetshop.db` file
- Sets up `sweets` table with correct schema
- No test cases written as it only handles setup (infra layer)

### ✅ 3. Manual Test
- Ran `python database/db.py` to ensure table and DB file created successfully