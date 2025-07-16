# Sweet Shop Management System


## 🚀 Getting Started

Follow these steps to set up and run the Sweet Shop Management System on your local machine.

---
## ✅ Setup
### 🔁 1. Clone the Repository


```bash
git clone https://github.com/your-username/sweetshop.git
cd sweetshop
```
### 🛠️ 2. Create and Activate Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
venv\Scripts\activate
```
### 📦 3. Install Required Dependencies
Install all the required packages using requirements.txt:
```bash
pip install -r requirements.txt
```
### ✅ 4. Run All Unit Tests
We follow Test-Driven Development (TDD). To run all the tests and ensure everything is working:
```bash
python -m unittest discover tests
```
### 🌐 5. Run the Streamlit Frontend UI
Launch the web interface using Streamlit:
```bash
streamlit run sweetshop_ui.py
```
### Once it runs, open your browser and go to:
```bash
http://localhost:8501
```
## 📂 Project Structure


```bash
sweetshop/
├── database/
│ └── db.py # SQLite DB setup and connection handler
│
├── models/
│ └── sweet.py # Sweet data model using @dataclass
│
├── services/
│ ├── add_sweet.py # Logic for adding a sweet (with validation)
│ ├── delete_sweet.py # Delete sweet by ID or name
│ ├── purchase_sweet.py # Handle purchasing logic and stock updates
│ ├── restock_sweet.py # Logic to restock sweets
│ ├── search_sweets.py # Filter/search sweets by name, category, price
│ ├── sort_sweets.py # Sorting sweets by column
│ └── view_sweets.py # Retrieve all sweets from DB
│
├── tests/
│ ├── test_add_sweet.py # TDD tests for adding sweets
│ ├── test_delete_sweet.py # Tests for deletion logic
│ ├── test_purchase_sweet.py # Tests for purchasing logic
│ ├── test_restock_sweet.py # Tests for restocking sweets
│ ├── test_search_sweets.py # Tests for search functionality
│ ├── test_sort_sweets.py # Tests for sorting sweets
│ └── test_view_sweets.py # Tests for viewing inventory
│
├── exceptions/
│ └── exceptions.py # Custom exceptions (e.g., StockError)
│
├── sweetshop_ui.py # 🌐 Streamlit frontend file
├── requirements.txt # List of dependencies
├── README.md # 📄 Project documentation
└── sweetshop.db # (Auto-created) SQLite database file
```


### 1. Data Model
- `models/sweet.py`: Defines the `Sweet` class using `@dataclass`.

### 2. Database Layer
- `database/db.py`: Sets up SQLite DB (`sweetshop.db`) with `sweets` table.
- Auto-created and tested via `python database/db.py`.

---

## ✅ TDD Progress

### 🔹 Add Sweet Feature

**Step 1: Write Initial Failing Test**
- `tests/test_sweet_shop.py`: Wrote `test_add_sweet()` to validate basic insert.
- Confirmed test fails before logic is written.

**Step 2: Pass the Test**
- `services/sweet_shop.py`: Implemented `add_sweet()` method.
- Verified test passes.

**Step 3: Handle Duplicate Sweet IDs**
- Added `test_add_duplicate_sweet_id()` to ensure duplicate inserts are blocked.
- Used test-specific DB (`test_sweetshop.db`) with teardown to avoid locking issues.

**Step 4: Test Execution**
```bash
python -m unittest discover tests
```
**Step 5: Edge Case – Negative Price**
- Added test: `test_add_sweet_with_negative_price` in `tests/test_sweet_shop.py`
- Purpose: Ensure that a sweet with a negative price is not allowed
- Behavior: `add_sweet()` should return `False` if price < 0
- Confirmed test fails before implementation
- ✅ Updated `add_sweet()` to include price validation
- ✅ Test now passes after validation is added

**Step 6: Edge Case – Empty or Invalid Fields**
- Added test: `test_add_sweet_with_missing_or_invalid_fields` in `tests/test_sweet_shop.py`
- Purpose: Ensure sweet has valid name, category, and quantity > 0
- Behavior: `add_sweet()` should return `False` for:
  - Empty name
  - Empty category
  - Zero or negative quantity
- Confirmed test fails before implementation
- ✅ Updated `add_sweet()` to validate non-empty name and category, and quantity > 0
- ✅ Confirmed all invalid inputs are rejected and tests pass (TDD Green)


**Step 7: Edge Case – Non-numeric Price or Quantity**
- Added test: `test_add_sweet_with_non_numeric_price_or_quantity` in `tests/test_sweet_shop.py`
- Purpose: Ensure sweet cannot be added if price or quantity is not a number
- Behavior: `add_sweet()` should return `False` if price or quantity is non-numeric
- Confirmed test fails before implementation
- ✅ Updated `add_sweet()` to validate that price is int/float and quantity is int
- ✅ Confirmed non-numeric inputs are rejected and test passes

**Step 8: Edge Case – Invalid Category**
- Added test: `test_add_sweet_with_invalid_category` in `tests/test_sweet_shop.py`
- Purpose: Only allow predefined sweet categories (e.g., Chocolate, Candy, Pastry, etc.)
- Behavior: `add_sweet()` should return `False` if category is outside the allowed list
- Confirmed test fails before implementation
- ✅ Defined VALID_CATEGORIES list in models/sweet.py
- ✅ Updated add_sweet() to validate category against predefined list
- ✅ Confirmed invalid category test now passes

**Step 9: Edge Case – Valid Sweet Is Successfully Added**
- Added test: `test_add_valid_sweet_passes_all_validations` in `tests/test_sweet_shop.py`
- Purpose: Ensure valid data passes all checks and is inserted into DB
- Behavior: `add_sweet()` should return True for valid sweet
- ✅ Confirmed test passes

**Step 10: Business Rule – Prevent Same Name + Category Combo**
- Added test: `test_add_sweet_with_duplicate_name_and_category()` in `tests/test_add_sweet.py`
- Purpose: Disallow adding sweets with the same name and category (even if ID is different)
- ❌ Confirmed test fails before logic is added
- ✅ Updated `add_sweet()` to reject sweets with the same name and category (even if ID is different)
- ✅ Ensures clean data and avoids logical duplicates in inventory
- ✅ Confirmed test passes for new business rule



## ✅ Refactor: Split Add Sweet Feature

- Moved add logic to `services/add_sweet.py` as `AddSweetService`
- Moved add-related tests to `tests/test_add_sweet.py`
- Follows modular service-based architecture for better maintainability

### 🔹 View All Sweets
**Step 1: Write Initial Failing Test**
- Added test: `test_get_all_sweets_returns_list_of_sweets` in `tests/test_view_sweets.py`
- Purpose: Ensure all added sweets are returned as a list of `Sweet` objects
- Confirmed test fails before implementation
- ✅ Implemented `get_all_sweets()` in `services/view_sweets.py`
- ✅ Fetches all sweets from DB and returns as list of `Sweet` objects
- ✅ Confirmed test passes

**Step 2: Edge Case – Empty Table**
- Added test: `test_get_all_sweets_empty_table` in `tests/test_view_sweets.py`
- Purpose: Ensure `get_all_sweets()` returns an empty list when DB has no rows
- ✅ Confirmed test passes

**Step 3: Edge Case – Large Dataset Performance**
- Added test: `test_get_all_sweets_large_dataset` in `tests/test_view_sweets.py`
- Purpose: Ensure `get_all_sweets()` handles large datasets (1,000+ records) efficiently
- Behavior: Should return correct count and object types without slowdown
- ✅ Confirmed test passes

### 🔹  Delete Sweet
**Step 1:  Write Initial Failing Test**
- Created test: `test_delete_existing_sweet()` in `tests/test_delete_sweet.py`
- Purpose: Ensure a sweet can be removed by ID from the database
- ✅ Confirmed test fails before implementation
- ✅ Implemented `delete_sweet(id)` in `services/delete_sweet.py`
- ✅ Deletes a sweet from DB by ID and returns True/False
- ✅ Confirmed test passes for existing sweet

**Step 2: Edge Case – Delete Non-Existent Sweet**
- Added test: `test_delete_non_existing_sweet()` in `tests/test_delete_sweet.py`
- Purpose: Ensure deleting an ID that doesn’t exist returns False without error
- ✅ Confirmed test passes

**Step 3: Edge Case – Invalid ID Type for Deletion**
- Added test: `test_delete_sweet_with_invalid_id_types()` in `tests/test_delete_sweet.py`
- Purpose: Ensure `delete_sweet()` handles invalid ID types (None, string, float, negative) gracefully
- ❌ Confirmed test fails (expected) before validation
- ✅ Updated delete_sweet() to validate ID type and value before querying DB
- ✅ Ensures unsafe types (None, str, float, negative) are rejected early
- ✅ Confirmed test for invalid types now passes

**Step 4: Edge Case – Double Deletion**
- Added test: `test_delete_sweet_twice_should_return_false_second_time()` in `tests/test_delete_sweet.py`
- Purpose: Ensure deleting the same ID twice only succeeds once
- ✅ Confirmed first delete returns True, second returns False

**Step 18: Optional Feature – Delete Sweet by Name**
- Added test: `test_delete_sweet_by_name_successfully()` in `tests/test_delete_sweet.py`
- Purpose: Allow deletion of sweets by name (alternative to ID)
- ❌ Confirmed test fails before method is implemented
- ✅ Implemented `delete_sweet_by_name()` in `DeleteSweetService`
- ✅ Supports deletion based on sweet name (used in admin/bulk operations)
- ✅ Confirmed test passes for deleting sweet by name

**Step 19: Edge Case – Invalid or Missing Name for delete_sweet_by_name**
- Added test: `test_delete_sweet_by_name_invalid_or_not_found()` in `tests/test_delete_sweet.py`
- Purpose: Ensure invalid name types or non-existent names return False without error
- ✅ Confirmed test passes with proper validation and messaging

### 🔹 Search Sweets by Name
**Step 1: Write Initial Failing Test**
- Created test: `test_search_by_name()` in `tests/test_search_sweets.py`
- Purpose: Allow users to search sweets by partial name match (case-insensitive)
- ❌ Confirmed test fails before implementation
- ✅ Implemented minimal `search_sweets()` logic to support name-based searching
- ✅ Confirmed test passes by only filtering on lowercase name
- ✅ Will expand support to category and price in next steps

**Step 2: Filter – Search by Category**
- Added test: `test_search_by_category()` in `tests/test_search_sweets.py`
- Purpose: Allow users to filter sweets by exact category match
- ❌ Confirmed test fails before adding category logic
- ✅ Implemented category filter in `search_sweets()`
- ✅ Allows searching by exact category
- ✅ Confirmed test passes after update

**Step 3: Improve – Case-Insensitive Name Search**
- Added test: `test_search_by_name_case_insensitive()` in `tests/test_search_sweets.py`
- Purpose: Ensure that search by name matches even if case is different (e.g., 'BaRfI' matches 'Barfi')
- ❌ Confirmed test fails before using LOWER() in SQL
- ✅ Refactored name filter to use `LOWER(name)` in SQL
- ✅ Ensures case-insensitive matching for name search
- ✅ Confirmed test passes for mixed-case input

**Step 4: Filter – Search by Price Range**
- Added test: `test_search_by_price_range()` in `tests/test_search_sweets.py`
- Purpose: Ensure sweets can be filtered by min and max price
- ❌ Confirmed test fails before price filter logic is implemented
- ✅ Implemented price range filtering in `search_sweets()` using min_price and max_price
- ✅ Ensures only sweets within specified price range are returned
- ✅ Confirmed test passes for price filtering

**Step 5: Validation – Handle Invalid Filter Types**
- Added test: `test_invalid_search_inputs()` in `tests/test_search_sweets.py`
- Purpose: Ensure invalid input types do not crash the search function
- ❌ Confirmed test fails or logs error before type checks are added
- ✅ Added input validation in `search_sweets()` for all filters
- ✅ Ensures function returns empty list instead of crashing for invalid types
- ✅ Confirmed all validation tests now pass

**Step 5: Validation Added 3 edge case tests to search_sweets:**
  - ✅ No filters: returns all sweets
  - ✅ Partial price filter (min or max only)
  - ✅ Combined filters (name + category + price range)
- ✅ Confirmed all filters work correctly and independently

### 🔹Inventory 

**Step 1: Write Initial Failing Test**
- Added test: `test_purchase_reduces_quantity()` in `tests/test_purchase_sweet.py`
- Purpose: Ensure that when a valid purchase is made, quantity decreases correctly
- ❌ Confirmed test fails before method is implemented
- ✅ Implemented `purchase_sweet(sweet_id, quantity)` in `PurchaseSweetService`
- ✅ Reduces quantity of a sweet if stock is sufficient
- ✅ Confirmed test passes for quantity reduction logic

**Step 2: Validation – Prevent Over-Purchase**
- Added test: `test_purchase_fails_if_not_enough_stock()` in `tests/test_purchase_sweet.py`
- Purpose: Ensure that a user cannot purchase more than the stock available
- ❌ Confirmed test fails as expected (no validation yet)
- ✅ Implemented stock validation in `purchase_sweet()` to prevent over-purchasing
- ✅ Test now passes if requested quantity > stock returns False and stock remains unchanged

**Step 3: Validation – Invalid sweet_id Handling**
- Added test: `test_purchase_fails_with_invalid_sweet_id()` in `tests/test_purchase_sweet.py`
- Purpose: Ensure function rejects non-integer IDs or non-existent sweet IDs
- ❌ Confirmed test fails before validation is implemented
- ✅ Added validation in `purchase_sweet()` to ensure sweet_id is a positive integer
- ✅ Confirmed test passes when ID is None, string, float, negative, or not found in DB


**Step 4: Validation – Invalid Quantity Handling**
- Added test: `test_purchase_fails_with_invalid_quantity()` in `tests/test_purchase_sweet.py`
- Purpose: Ensure quantity must be a positive integer
- ❌ Confirmed test fails before validation is implemented
- ✅ Added validation in `purchase_sweet()` to reject invalid quantities
- ✅ Ensures quantity must be a positive integer (not string, None, float, negative, or 0)
- ✅ Confirmed all validation tests pass

- ✅ Introduced custom exception: `StockError`
- ✅ Updated `purchase_sweet()` to raise exception if stock is insufficient
- ✅ Updated test to expect exception using `with self.assertRaises(StockError)`


**Step 5: Extend purchase_sweet – Support Name as Input**
- Added test: `test_purchase_by_name_reduces_quantity()`
- Purpose: Allow purchasing sweet using name as first argument
- ❌ Confirmed test fails before enhancement
- ✅ Extended `purchase_sweet()` to support both int (ID) and str (Name)
- ✅ Now users can purchase by name like: `purchase_sweet("Barfi", 3)`
- ✅ Confirmed via test: `test_purchase_by_name_reduces_quantity()`

**Step 6: Inventory – Restock Sweet**
- Added test: `test_restock_increases_quantity()` in `tests/test_restock_sweet.py`
- Purpose: Ensure that quantity increases after restocking
- ❌ Confirmed test fails before implementation
- ✅ Implemented basic logic in `restock_sweet()` to increase quantity for valid sweet ID
- ✅ Confirmed test passes for valid restock

**Step 7: Validation – Invalid Quantity in Restock**
- Added test: `test_restock_fails_with_invalid_quantity()`
- Purpose: Prevent restocking with invalid quantity (None, 0, negative, string, float)
- ❌ Confirmed test fails before validation
- ✅ Added input validation to `restock_sweet()` to ensure quantity is a positive integer
- ✅ Confirmed test passes when quantity is None, string, zero, float, or negative

**Step 8: Validation – Restock Non-existent Sweet**
- Added test: `test_restock_fails_for_nonexistent_sweet()`
- Purpose: Ensure restocking fails if sweet ID is not in database
- ✅ Confirmed behavior (or ❌ failed if not handled yet)
- ✅ Handled non-existent sweet ID in `restock_sweet()`
- ✅ Now returns False and logs error if the sweet is not in the database

**Step 9: Add Support – Restock by Sweet Name**
- Added test: `test_restock_by_name_increases_quantity()`
- Purpose: Allow restocking by sweet name (str input)
- ❌ Confirmed test fails before 
- ✅ Enhanced `restock_sweet()` to support restocking by name (str)
- ✅ Now works with either sweet ID or name input

**Step 10: Validation – Invalid Sweet Identifier in Restock**
- Added test: `test_restock_fails_with_invalid_identifier()`
- Purpose: Ensure restocking fails if identifier is None, empty, float, list, or invalid type
- ✅ Added strict validation for sweet identifier in `restock_sweet()`
- ✅ Restocking now fails if ID is negative or name is empty/numeric/invalid type

### 🔹sorting
**Step 1: Write Initial Failing Test**
- Added test: `test_sort_by_name_ascending()` in `test_sort_sweets.py`
- Purpose: Sort sweets by name alphabetically (A-Z)
- ❌ Confirmed test fails before implementing sorting logic
- ✅ Implemented initial `sort_sweets()` method in `SortSweetsService`
- ✅ Supports sorting by `name` in ascending order
- ✅ Confirmed test passes for alphabetical sorting

**Step 2: Add Sorting Order Support**
- ✅ Added test: `test_sort_by_name_descending()` for reverse order
- ✅ Updated `sort_sweets()` to support order="asc" and "desc"

**Step 3: Sorting by Price (Ascending) — Red Step**
- 🔴 Added test: `test_sort_by_price_ascending()` in `test_sort_sweets.py`
- 🔎 Purpose: Verify that sweets are sorted by price from low to high
- ❌ Confirmed test fails before implementing support for the "price" field in `sort_sweets()`
- ✅ Added test: `test_sort_by_price_ascending()`
- ✅ Updated `sort_sweets()` to allow sorting by `price`
- ✅ Query builds dynamically for any supported field + order

**Step 4: Sorting by Price (Descending) — Red Step**
- 🔴 Added test: `test_sort_by_price_descending()` in `test_sort_sweets.py`
- 🔎 Purpose: Ensure sweets are sorted from high to low price
- ❌ Confirmed test fails before logic handles `order="desc"` for price field
- ✅ Implemented sorting by `price` in descending order
- ✅ Reused flexible SQL logic in `sort_sweets()` with support for any valid field + order
- ✅ Confirmed test passes: high-to-low price sorting works as expected

**Step 5: Sorting by Quantity (Ascending) — Red Step**
- 🔴 Added test: `test_sort_by_quantity_ascending()` in `test_sort_sweets.py`
- 🔎 Purpose: Sort sweets by available stock (from low to high)
- ❌ Confirmed test fails if "quantity" not yet handled by `sort_sweets()`
- ✅ Enabled sorting by `quantity` using `sort_sweets(by="quantity")`
- ✅ Confirmed default ascending order works
- ✅ Logic reuses flexible SQL query with safety checks on field and order

**Step 6: Sorting by Quantity (Descending) — Red Step**
- 🔴 Added test: `test_sort_by_quantity_descending()` in `test_sort_sweets.py`
- 🔎 Purpose: Sort sweets from high to low stock quantity
- ❌ Confirmed test fails if descending quantity sort is not supported yet
- ✅ Implemented sorting by `quantity` in descending order
- ✅ `sort_sweets()` handles both ascending and descending order generically
- ✅ Confirmed result correctness with automated test

**Step 7: Sorting by Category — Red Step**
- 🔴 Added test: `test_sort_by_category_ascending()` in `test_sort_sweets.py`
- 🔎 Purpose: Ensure sweets are sorted by category A-Z
- ❌ Confirmed test fails before 'category' support is added
- ✅ Enabled sorting by `category` (A–Z or Z–A)
- ✅ Used flexible query in `sort_sweets()` with dynamic ORDER BY field
- ✅ All sorting options are now fully supported: name, price, quantity, category

**Step 8: Sort Input Validation — Red Step**
- 🔴 Added test: `test_sort_fails_with_invalid_field_or_order()` in `test_sort_sweets.py`
- 🔎 Purpose: Ensure sort_sweets() handles bad input for field (`by`) or sort order (`order`)
- ❌ Confirmed test fails before input validation is added
- ✅ Added input validation to `sort_sweets()`:
  - Rejects invalid field (`by`) or order (`asc/desc`)
  - Returns empty list instead of crashing
- ✅ Confirmed edge case tests pass successfully



### 🔹 Streamlit UI Summary

We built a complete web-based frontend using **Streamlit** to manage sweets interactively.  
Users can **add, view, delete, search, purchase**, and **restock** sweets through an intuitive form-driven interface.  
All backend validations (ID checks, stock limits, type safety) are reflected in the UI with clear feedback.  
The interface supports operations using both sweet **ID and name**, improving usability.  
Real-time updates are handled with `st.rerun()` for smooth workflows.  
The frontend was co-developed with the help of **AI (ChatGPT)** to accelerate design and modularity.  
This UI simplifies inventory tasks for vendors or admins, even without programming knowledge.


---

## 📚 References & Acknowledgments

This project was developed with the help of various tools, learning resources, and communities:

### 🤖 AI Assistance
- Portions of the Streamlit UI and validation logic were implemented with help from **OpenAI ChatGPT**
- AI guidance accelerated development, reduced bugs, and ensured better modularity

### 📖 Blogs & Documentation
- [Streamlit Documentation](https://docs.streamlit.io/)
- [SQLite Official Docs](https://www.sqlite.org/docs.html)
- [Python Dataclasses Guide – RealPython](https://realpython.com/python-data-classes/)
- [Test-Driven Development in Python – freeCodeCamp](https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/)

### 🎥 YouTube Resources
- [Streamlit Crash Course – Traversy Media](https://www.youtube.com/watch?v=JwSS70SZdyM)
- [TDD with Python – Tech With Tim](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

---

Thanks to the open-source community and educators for making knowledge accessible and project-building faster and more enjoyable 🚀
