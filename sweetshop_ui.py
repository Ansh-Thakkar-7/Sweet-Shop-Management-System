import streamlit as st
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.view_sweets import ViewSweetsService
from services.delete_sweet import DeleteSweetService
from services.purchase_sweet import PurchaseSweetService
from services.restock_sweet import RestockSweetService
from services.search_sweets import SearchSweetService
from services.sort_sweets import SortSweetsService

add_service = AddSweetService()
view_service = ViewSweetsService()
delete_service = DeleteSweetService()
purchase_service = PurchaseSweetService()
restock_service = RestockSweetService()
search_service = SearchSweetService()
sort_service = SortSweetsService()

st.set_page_config(page_title="Sweet Shop", layout="wide")
st.title("🍬 Sweet Shop Management System")

# Sidebar navigation
page = st.sidebar.selectbox("📂 Select Operation", [
    "View & Manage Inventory",
    "Add New Sweet",
    "Search Sweets",
    "Purchase Sweet",
    "Restock Sweet"
])

# -------------------------
# 📋 View All + Delete + Sort
# -------------------------
if page == "View & Manage Inventory":
    st.header("📋 All Sweets (with Delete & Sort)")

    sort_by = st.selectbox("Sort By", ["id", "name", "price", "quantity", "category"], index=1)
    sort_order = st.radio("Order", ["asc", "desc"], horizontal=True)

    sweets = sort_service.sort_sweets(by=sort_by, order=sort_order)
    if sweets:
        for sweet in sweets:
            cols = st.columns([1, 2, 2, 1, 1, 1])
            cols[0].write(sweet.id)
            cols[1].write(sweet.name)
            cols[2].write(sweet.category)
            cols[3].write(f"₹{sweet.price:.2f}")
            cols[4].write(sweet.quantity)
            if cols[5].button("🗑️ Delete", key=f"del_{sweet.id}"):
                deleted = delete_service.delete_sweet(sweet.id)
                if deleted:
                    st.success(f"Sweet ID {sweet.id} deleted.")
                    st.rerun()
    else:
        st.info("No sweets in inventory.")

# -------------------------
# ➕ Add Sweet
# -------------------------
elif page == "Add New Sweet":
    st.header("➕ Add a New Sweet")

    with st.form("add_sweet_form"):
        id = st.number_input("ID", step=1)
        name = st.text_input("Name")
        category = st.selectbox("Category", ["Milk-Based", "Nut-Based", "Vegetable-Based", "Chocolate", "Candy", "Pastry"])
        price = st.number_input("Price", step=0.5, format="%.2f")
        quantity = st.number_input("Quantity", step=1)
        submit = st.form_submit_button("Add Sweet")

        if submit:
            sweet = Sweet(id=id, name=name, category=category, price=price, quantity=quantity)
            result = add_service.add_sweet(sweet)

            if result is True:
                st.success("✅ Sweet added successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to add sweet. Check for duplicate ID or validation issues.")

# -------------------------
# 🔍 Search
# -------------------------
elif page == "Search Sweets":
    st.header("🔍 Search Sweets")
    with st.form("search_form"):
        name = st.text_input("Name (partial or full)", "")
        category = st.selectbox("Category", ["", "Milk-Based", "Nut-Based", "Vegetable-Based", "Chocolate", "Candy", "Pastry"])
        min_price = st.number_input("Min Price", step=0.5, value=0.0)
        max_price = st.number_input("Max Price", step=0.5, value=100.0)
        go = st.form_submit_button("Search")

        if go:
            results = search_service.search_sweets(name=name.strip(), category=category.strip(), min_price=min_price, max_price=max_price)
            if results:
                st.success(f"🔎 Found {len(results)} sweet(s)")
                st.table([vars(s) for s in results])
            else:
                st.warning("No matching sweets found.")

# -------------------------
# 📦 Purchase
# -------------------------
elif page == "Purchase Sweet":
    st.header("📦 Purchase Sweet")

    with st.form("purchase_form"):
        sweet_input = st.text_input("Sweet ID or Name")  # <--- string input
        qty = st.number_input("Quantity to Purchase", step=1, min_value=1)
        buy = st.form_submit_button("Purchase")

        if buy:
            try:
                # Try convert input to int, else treat as name
                sweet_id_or_name = int(sweet_input) if sweet_input.strip().isdigit() else sweet_input.strip()

                result = purchase_service.purchase_sweet(sweet_id_or_name, qty)

                if result:
                    st.success(f"✅ Purchased {qty} unit(s) of sweet '{sweet_input}'")
                    st.rerun()
                else:
                    st.error("❌ Purchase failed. Invalid sweet or quantity.")

            except Exception as e:
                st.error(f"❌ Purchase failed: {e}")

# -------------------------
# ♻️ Restock
# -------------------------
elif page == "Restock Sweet":
    st.header("♻️ Restock Sweet")

    with st.form("restock_form"):
        sweet_input = st.text_input("Sweet ID or Name")  # ← Accept both
        qty = st.number_input("Quantity to Add", step=1, min_value=1)
        restock = st.form_submit_button("Restock")

        if restock:
            try:
                sweet_id_or_name = int(sweet_input) if sweet_input.strip().isdigit() else sweet_input.strip()

                result = restock_service.restock_sweet(sweet_id_or_name, qty)

                if result:
                    st.success(f"✅ Restocked sweet '{sweet_input}' by {qty} units")
                    st.rerun()
                else:
                    st.error("❌ Restock failed. Invalid sweet or quantity.")
            except Exception as e:
                st.error(f"❌ Restock failed: {e}")
