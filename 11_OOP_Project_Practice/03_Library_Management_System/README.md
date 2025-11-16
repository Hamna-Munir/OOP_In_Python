# 📚 Library Management System  
A modern and efficient **Library Management System** built using **Python OOP**, **SQLite database**, and **Streamlit** with a clean **dark UI**.

This system allows users to **add, view, search, update, borrow, return, and delete books** with persistent database storage.

---

## 🚀 Features

### ✅ 1. Add New Book  
Add book details including:
- Title  
- Author  
- Available Quantity  

### ✅ 2. View All Books  
View all books stored in the SQLite database in a clean tabular format.

### ✅ 3. Search Books  
Search books by:
- Name  
- Author  
- Book ID  

### ✅ 4. Update Book Information  
Edit book details:
- Title  
- Author  
- Quantity  

### ✅ 5. Borrow Book  
Decreases available quantity by 1 (only if stock is available).

### ✅ 6. Return Book  
Increases available quantity by 1.

### ✅ 7. Delete Book  
Delete a book using its **Book ID**.

---

## 🏗️ Technologies Used
- **Python**
- **Object-Oriented Programming (OOP)**
- **SQLite Database**
- **Streamlit UI Framework**
- **Dark Mode UI**

---

## 📂 Project Structure
```
Library_Management_System/
│
├── 03_Library_Management_System.py   # Main Streamlit App
├── library.db                        # SQLite database
└── README.md                         # Documentation
```

---

## ▶️ How to Run the Project

### **1. Create Virtual Environment (optional)**
```
python -m venv .venv
```

### **2. Activate Virtual Environment (Windows PowerShell)**
```
.\.venv\Scripts\Activate
```

### **3. Install Required Packages**
```
pip install streamlit
```

### **4. Run the Streamlit App**
```
streamlit run 03_Library_Management_System.py
```

---

## 📝 How to Use the System

### 📘 Add Book
Enter book information → click **Add Book**.

### 📗 View Books  
Displays a complete list of all stored books.

### 🔍 Search Book  
Search by ID, title, or author.

### 📝 Update Book  
Select a book → update any information.

### 📕 Borrow Book  
Automatically decreases available quantity.

### 📙 Return Book  
Restocks the returned book.

### 🗑️ Delete Book  
Remove a book from the database using its ID.

---

## 👩‍💻 Developer  
**Hamna Munir**  
- 🔗 LinkedIn  
- 💻 GitHub  
- 📘 OOP Repository  

---

## ⭐ Future Enhancements  
- Add book category support  
- Add borrower records & history  
- Add admin login  
- Add PDF export for reports  

---

## 📜 License  
This project is open-source and free to use for learning purposes.
