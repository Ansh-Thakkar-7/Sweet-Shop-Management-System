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


## ✅ TDD Progress

### ✅ Step 1: Add Sweet Feature (Start)

1. Created test file: `tests/test_sweet_shop.py`
2. Wrote initial failing test: `test_add_sweet()` in `TestSweetShop` class
   - Purpose: Test adding a new Sweet object to the shop
   - Result: ❌ Test failed as expected (no logic implemented yet)
3. Verified test runs using:
```bash
python -m unittest discover tests
```

### ✅ Step 2: Make `test_add_sweet` Pass

4. Created service class: `SweetShop` in `services/sweet_shop.py`
5. Implemented `add_sweet()` method to insert data into SQLite DB
6. Re-ran test using:
```bash
python -m unittest discover tests
```