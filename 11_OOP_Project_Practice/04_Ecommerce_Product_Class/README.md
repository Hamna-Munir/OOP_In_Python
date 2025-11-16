# 🛒 Ecommerce Product Management System  
A simple and efficient **Ecommerce Product Dashboard** built using **Python OOP**, **SQLite**, and **Streamlit**.  
This project allows users to **add, view, search, update, and delete products** using an interactive UI with full database support.

## 🚀 Features

### ✅ 1. Add Product  
Easily add new products including:
- Product Name  
- Category  
- Price  
- Quantity  

All data is saved in an **SQLite database**.

### ✅ 2. View All Products  
Displays a clean table of all products:
- ID  
- Name  
- Category  
- Price  
- Quantity  

### ✅ 3. Search Product  
Search a product using:
- Product ID  
- Product Name  

### ✅ 4. Update Product  
Modify:
- Name  
- Category  
- Price  
- Quantity  

Updates are saved directly to the database.

### ✅ 5. Delete Product  
Remove any product using its **Product ID**.

## 🏗️ Technologies Used
- **Python**
- **Object-Oriented Programming (OOP)**
- **SQLite Database**
- **Streamlit (UI Framework)**

## 📂 Project Structure
```
Ecommerce_Dashboard/
│
├── 04_Ecommerce_Product_Class.py   # Main Streamlit App
├── ecommerce.db                    # SQLite database
└── README.md                       # Documentation
```

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
streamlit run 04_Ecommerce_Product_Class.py
```

## 📝 How to Use the Dashboard

### 🌟 Add Product
Enter product details and click **Add Product**.

### 🌟 View Products
Displays all products stored in the database.

### 🌟 Search Product
Search using product ID or name.

### 🌟 Update Product
Fetch product → edit details → update.

### 🌟 Delete Product
Enter product ID → delete.

## 👨‍💻 Developer
**Hamna Munir**  
- 🔗 LinkedIn  
- 💻 GitHub  
- 📘 OOP Repository  

## ⭐ Future Enhancements
- Add product images  
- Add category management  
- Export products to Excel  
- Add user authentication  

## 📜 License
This project is open-source and free to use for learning purposes.
