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
