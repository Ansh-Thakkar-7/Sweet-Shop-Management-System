from dataclasses import dataclass

@dataclass
class Sweet:
    id: int
    name: str
    category: str
    price: float
    quantity: int


VALID_CATEGORIES = [
    "Chocolate",
    "Candy",
    "Pastry",
    "Milk-Based",
    "Nut-Based",
    "Vegetable-Based"
]