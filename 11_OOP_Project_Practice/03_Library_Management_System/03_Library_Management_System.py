# 03_Library_Management_System.py
import streamlit as st
import sqlite3
import pandas as pd
from typing import List, Tuple

# ----------------------------
#  CONFIG / DARK THEME CSS
# ----------------------------
st.set_page_config(page_title="Library Management System", layout="wide")

st.markdown(
    """
    <style>
        /* app background and text */
        .stApp {
            background-color: #0e1117;
            color: #e6eef8;
        }
        /* header fonts */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }
        /* inputs/cards */
        .stTextInput>div>div>input, .stNumberInput>div>div>input, .st-selectbox>div>div>div {
            background-color:#0f1720 !important;
            color:#e6eef8 !important;
            border: 1px solid #222628 !important;
        }
        /* sidebar */
        .css-1d391kg { background-color: #111418; }
        /* buttons */
        .stButton>button {
            background-color:#0b7285;
            color: white;
        }
        /* dataframe header style (approx) */
        .stDataFrame table thead th {
            background-color: #0f1720;
            color: #e6eef8;
        }
        /* hr style */
        hr { border: 0.5px solid #2b2f36; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
#  DATABASE (SQLite) HELPERS
# ----------------------------
DB_PATH = "library.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_book_db(book_id: str, title: str, author: str, quantity: int) -> bool:
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO books (book_id, title, author, quantity) VALUES (?, ?, ?, ?)",
            (book_id, title, author, quantity)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # primary key exists
        return False
    except Exception:
        return False

def get_books_db() -> List[Tuple]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT book_id, title, author, quantity FROM books ORDER BY title")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_book_db(keyword: str) -> List[Tuple]:
    conn = get_connection()
    cur = conn.cursor()
    q = f"%{keyword}%"
    cur.execute("""
        SELECT book_id, title, author, quantity FROM books
        WHERE book_id LIKE ? OR title LIKE ? OR author LIKE ?
        ORDER BY title
    """, (q, q, q))
    rows = cur.fetchall()
    conn.close()
    return rows

def update_book_db(book_id: str, title: str, author: str, quantity: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE books
        SET title = ?, author = ?, quantity = ?
        WHERE book_id = ?
    """, (title, author, quantity, book_id))
    conn.commit()
    conn.close()

def delete_book_db(book_id: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()

# initialize DB
init_db()

# ----------------------------
#  SIDEBAR: Developer + Navigation
# ----------------------------
st.sidebar.markdown("## 👩‍💻 Developer")
st.sidebar.markdown(
    """
**Hamna Munir**

[🔗 LinkedIn](https://www.linkedin.com/in/hamna-munir-6891a72a0/)  
[💻 GitHub](https://github.com/Hamna-Munir)  
[📚 OOP Repository](https://github.com/Hamna-Munir/OOP_In_Python/tree/main/11_OOP_Project_Practice/03_Library_Management_System)
"""
)

st.sidebar.markdown("---")
st.sidebar.markdown("## 📌 Navigation")

menu = st.sidebar.radio(
    "",
    [
        "➕ Add Book",
        "📊 View Books (Table)",
        "🔍 Search Book",
        "📝 Update Book",
        "📕 Borrow Book",
        "📘 Return Book",
        "🗑 Delete Book"
    ]
)

# ----------------------------
#  MAIN HEADER (clean)
# ----------------------------
st.markdown(
    """
    <div style="display:flex; align-items:center; gap:12px; justify-content:center;">
        <div style="font-size:40px;">📚</div>
        <h1 style="margin:0; font-size:34px;">Library Management System</h1>
    </div>
    <p style="text-align:center; color:#9aa1a8; margin-top:6px; margin-bottom:14px;">
        Built using <b>Python OOP</b>, <b>SQLite</b>, and <b>Streamlit</b>.
    </p>
    <hr style='border: 1px solid #2b2f36; margin-bottom:18px;'>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
#  MENU: Add Book
# ----------------------------
if menu == "➕ Add Book":
    st.header("➕ Add New Book")
    col1, col2 = st.columns([2, 3])

    with col1:
        book_id = st.text_input("Book ID", help="Unique ID (e.g., B001)")
        quantity = st.number_input("Quantity", min_value=0, step=1, value=1)

    with col2:
        title = st.text_input("Title")
        author = st.text_input("Author")

    if st.button("Add Book"):
        if not (book_id and title and author):
            st.error("Please provide Book ID, Title and Author.")
        else:
            ok = add_book_db(book_id.strip(), title.strip(), author.strip(), int(quantity))
            if ok:
                st.success(f"Book '{title}' added.")
            else:
                st.error("Book ID already exists or an error occurred.")

# ----------------------------
#  MENU: View Books (Table)
# ----------------------------
elif menu == "📊 View Books (Table)":
    st.header("📖 All Books (Table View)")
    books = get_books_db()

    if not books:
        st.info("No books found in the library.")
    else:
        df = pd.DataFrame(books, columns=["Book ID", "Title", "Author", "Quantity"])
        # Use container width so it looks good in wide layout
        st.dataframe(df, use_container_width=True)

# ----------------------------
#  MENU: Search Book
# ----------------------------
elif menu == "🔍 Search Book":
    st.header("🔍 Search Books")
    keyword = st.text_input("Enter Book ID / Title / Author")
    if st.button("Search"):
        if not keyword:
            st.warning("Please enter a keyword to search.")
        else:
            results = search_book_db(keyword)
            if not results:
                st.info("No matching books.")
            else:
                df = pd.DataFrame(results, columns=["Book ID", "Title", "Author", "Quantity"])
                st.dataframe(df, use_container_width=True)

# ----------------------------
#  MENU: Update Book
# ----------------------------
elif menu == "📝 Update Book":
    st.header("📝 Update Book Details")
    book_id = st.text_input("Enter Book ID to fetch")
    if st.button("Fetch"):
        if not book_id:
            st.error("Please enter a Book ID.")
        else:
            rows = search_book_db(book_id.strip())
            if not rows:
                st.error("Book not found.")
            else:
                # prefer exact id match
                row = None
                for r in rows:
                    if r[0] == book_id.strip():
                        row = r
                        break
                if row is None:
                    row = rows[0]
                _, cur_title, cur_author, cur_qty = row

                new_title = st.text_input("Title", value=cur_title)
                new_author = st.text_input("Author", value=cur_author)
                new_qty = st.number_input("Quantity", min_value=0, step=1, value=cur_qty)

                if st.button("Update Now"):
                    update_book_db(book_id.strip(), new_title.strip(), new_author.strip(), int(new_qty))
                    st.success("Book updated successfully.")

# ----------------------------
#  MENU: Borrow Book
# ----------------------------
elif menu == "📕 Borrow Book":
    st.header("📕 Borrow Book")
    book_id = st.text_input("Book ID to borrow")
    if st.button("Borrow"):
        if not book_id:
            st.error("Please enter a Book ID.")
        else:
            rows = search_book_db(book_id.strip())
            if not rows:
                st.error("Book not found.")
            else:
                # pick exact id match if exists else first
                row = None
                for r in rows:
                    if r[0] == book_id.strip():
                        row = r
                        break
                if row is None:
                    row = rows[0]
                bid, title, author, qty = row
                if qty > 0:
                    update_book_db(bid, title, author, qty - 1)
                    st.success(f"You borrowed '{title}'.")
                else:
                    st.warning("No copies available to borrow.")

# ----------------------------
#  MENU: Return Book
# ----------------------------
elif menu == "📘 Return Book":
    st.header("📘 Return Book")
    book_id = st.text_input("Book ID to return")
    if st.button("Return"):
        if not book_id:
            st.error("Please enter a Book ID.")
        else:
            rows = search_book_db(book_id.strip())
            if not rows:
                st.error("Book not found.")
            else:
                row = None
                for r in rows:
                    if r[0] == book_id.strip():
                        row = r
                        break
                if row is None:
                    row = rows[0]
                bid, title, author, qty = row
                update_book_db(bid, title, author, qty + 1)
                st.success(f"Returned '{title}' successfully.")

# ----------------------------
#  MENU: Delete Book
# ----------------------------
elif menu == "🗑 Delete Book":
    st.header("🗑 Delete Book")
    book_id = st.text_input("Enter Book ID to Delete")
    if st.button("Delete"):
        if not book_id:
            st.error("Please enter a Book ID.")
        else:
            rows = search_book_db(book_id.strip())
            if not rows:
                st.error("Book not found.")
            else:
                delete_book_db(book_id.strip())
                st.success("Book deleted successfully.")
