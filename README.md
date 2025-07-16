# Sweet Shop Management System

## ✅ Setup

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
**Step 22: Write Initial Failing Test**
- Created test: `test_search_by_name()` in `tests/test_search_sweets.py`
- Purpose: Allow users to search sweets by partial name match (case-insensitive)
- ❌ Confirmed test fails before implementation
- ✅ Implemented minimal `search_sweets()` logic to support name-based searching
- ✅ Confirmed test passes by only filtering on lowercase name
- ✅ Will expand support to category and price in next steps

**Step 24: Filter – Search by Category**
- Added test: `test_search_by_category()` in `tests/test_search_sweets.py`
- Purpose: Allow users to filter sweets by exact category match
- ❌ Confirmed test fails before adding category logic
- ✅ Implemented category filter in `search_sweets()`
- ✅ Allows searching by exact category
- ✅ Confirmed test passes after update
