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
