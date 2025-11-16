import streamlit as st
import sqlite3

# ===============================================================
# DATABASE SETUP
# ===============================================================

conn = sqlite3.connect("ecommerce.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
""")
conn.commit()


# ===============================================================
# PRODUCT CLASS (OOP)
# ===============================================================

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def save_to_db(self):
        cursor.execute(
            "INSERT INTO products(name, category, price, quantity) VALUES (?, ?, ?, ?)",
            (self.name, self.category, self.price, self.quantity)
        )
        conn.commit()


# ===============================================================
# UTILITY FUNCTIONS
# ===============================================================

def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def search_product(keyword):
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{keyword}%",))
    return cursor.fetchall()

def update_product(product_id, name, category, price, quantity):
    cursor.execute("""
        UPDATE products 
        SET name=?, category=?, price=?, quantity=?
        WHERE id=?
    """, (name, category, price, quantity, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()


# ===============================================================
# PAGE SETUP
# ===============================================================

st.set_page_config(
    page_title="Ecommerce Product Management",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark theme styling
st.markdown("""
    <style>
        .css-18e3th9 { background-color: #0d1117 !important; color: white !important; }
        .css-1d391kg { background-color: #0d1117 !important; }
        .stButton>button { background-color: #30363d; color: white; border-radius: 8px; }
        .stTextInput>div>div>input { background-color: #161b22; color: white; }
    </style>
""", unsafe_allow_html=True)


# ===============================================================
# SIDEBAR
# ===============================================================

st.sidebar.title("🛍️ Ecommerce Dashboard")

st.sidebar.subheader("👩‍💻 Developer Information")
st.sidebar.write("**Hamna Munir**")

st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/hamna-munir-6891a72a0/)")
st.sidebar.markdown("💻 [GitHub](https://github.com/Hamna-Munir)")
st.sidebar.markdown("📦 [OOP Repository](https://github.com/Hamna-Munir/OOP_In_Python)")

st.sidebar.write("---")

menu = st.sidebar.radio(
    "📌 Navigation",
    ["Add Product", "View Products", "Search Product", "Update Product", "Delete Product"]
)


# ===============================================================
# MAIN UI
# ===============================================================

st.markdown("""
    <h1 style='text-align:center;'>🛒 Ecommerce Product Management System</h1>
    <p style='text-align:center;'>Built using <b>Python OOP</b>, <b>SQLite</b>, and <b>Streamlit</b>.</p>
    <hr>
""", unsafe_allow_html=True)


# --------------------------- ADD PRODUCT ---------------------------
if menu == "Add Product":
    st.header("➕ Add New Product")

    name = st.text_input("Product Name")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0.0, step=0.1)
    quantity = st.number_input("Quantity", min_value=0)

    if st.button("Add Product"):
        if name and category:
            p = Product(name, category, price, quantity)
            p.save_to_db()
            st.success("Product added successfully!")
        else:
            st.error("Please fill all fields.")


# --------------------------- VIEW PRODUCTS ---------------------------
elif menu == "View Products":
    st.header("📦 All Products")

    products = get_all_products()

    if products:
        import pandas as pd

        # convert list of tuples to DataFrame
        df = pd.DataFrame(products, columns=["ID", "Name", "Category", "Price", "Stock"])

        # format price:
        # - if value is an integer-like float -> show as "50,000"
        # - otherwise show with two decimals and commas -> "1,234.56"
        def format_price(x):
            try:
                val = float(x)
                if val.is_integer():
                    return f"{int(val):,}"
                return f"{val:,.2f}"
            except Exception:
                return x  # leave as-is if formatting fails

        df["Price"] = df["Price"].apply(format_price)

        # display the table
        st.table(df)
    else:
        st.info("No products available.")


# --------------------------- SEARCH PRODUCT ---------------------------
elif menu == "Search Product":
    st.header("🔍 Search Product")

    keyword = st.text_input("Enter product name")

    if keyword:
        results = search_product(keyword)

        if results:
            st.subheader("Results:")

            for r in results:
                st.write(f"**ID:** {r[0]}")
                st.write(f"**Name:** {r[1]}")
                st.write(f"**Category:** {r[2]}")
                st.write(f"**Price:** {r[3]}")
                st.write(f"**Quantity:** {r[4]}")
                st.write("---")
        else:
            st.warning("No product found.")


# --------------------------- UPDATE PRODUCT ---------------------------
elif menu == "Update Product":
    st.header("✏️ Update Product")

    products = get_all_products()

    if products:
        product_ids = [p[0] for p in products]
        selected_id = st.selectbox("Select Product ID", product_ids)

        cursor.execute("SELECT * FROM products WHERE id=?", (selected_id,))
        product = cursor.fetchone()

        new_name = st.text_input("Product Name", product[1])
        new_category = st.text_input("Category", product[2])
        new_price = st.number_input("Price", value=product[3])
        new_quantity = st.number_input("Quantity", value=product[4])

        if st.button("Update"):
            update_product(selected_id, new_name, new_category, new_price, new_quantity)
            st.success("Product updated successfully!")
    else:
        st.info("No products available.")


# --------------------------- DELETE PRODUCT ---------------------------
elif menu == "Delete Product":
    st.header("🗑️ Delete Product")

    products = get_all_products()

    if products:
        product_ids = [p[0] for p in products]
        selected_id = st.selectbox("Select Product ID", product_ids)

        if st.button("Delete"):
            delete_product(selected_id)
            st.error("Product deleted!")
    else:
        st.info("No products available.")


