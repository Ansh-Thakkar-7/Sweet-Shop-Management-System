import streamlit as st
from services.view_sweets import ViewSweetsService
from services.add_sweet import AddSweetService
from models.sweet import Sweet

# Initialize services
view_service = ViewSweetsService()
add_service = AddSweetService()

# UI Title
st.set_page_config(page_title="Sweet Shop", layout="wide")
st.title("🍬 Sweet Shop Management System")

# Form to add sweets
st.header("➕ Add New Sweet")
with st.form("add_sweet_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        sweet_id = st.number_input("ID", step=1)
        name = st.text_input("Name")
    with col2:
        category = st.selectbox("Category", ["Milk-Based", "Nut-Based", "Vegetable-Based", "Chocolate", "Candy", "Pastry"])
        price = st.number_input("Price", step=0.1, format="%.2f")
    with col3:
        quantity = st.number_input("Quantity", step=1)
    
    submit_btn = st.form_submit_button("Add Sweet")
    if submit_btn:
        sweet = Sweet(id=sweet_id, name=name, category=category, price=price, quantity=quantity)
        result = add_service.add_sweet(sweet)
        if result:
            st.success("✅ Sweet added successfully!")
        else:
            st.error("❌ Failed to add sweet. ID may already exist or input is invalid.")

# View sweets
st.header("📋 Current Inventory")
sweets = view_service.get_all_sweets()
if sweets:
    st.table([vars(s) for s in sweets])
else:
    st.warning("⚠️ No sweets found.")
