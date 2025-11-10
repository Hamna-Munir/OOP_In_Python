import streamlit as st

# ---------------------------
#  Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Bank Account System | Hamna Munir",
    page_icon="💰",
    layout="centered"
)

# ---------------------------
#  Header Section
# ---------------------------
st.title("💳 Bank Account Management System")
st.markdown("""
### Developed by [**Hamna Munir**](https://github.com/Hamna-Munir)
Welcome to a professional, interactive simulation of a **Bank Account System** built in Python using OOP concepts.
""")

# GitHub Repository Link Button
st.markdown(
    """
    <div style="text-align: right;">
        <a href="https://github.com/Hamna-Munir/OOP_In_Python/tree/main/11_OOP_Project_Practice" target="_blank">
            <button style="background-color:#4CAF50;border:none;color:white;padding:8px 16px;
            text-align:center;text-decoration:none;display:inline-block;font-size:14px;
            margin:4px 2px;border-radius:10px;cursor:pointer;">🌐 View on GitHub</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# 🏦 Bank Account Class
# ---------------------------
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"✅ Deposited Rs.{amount}. New Balance: Rs.{self.balance}"
        else:
            return "❌ Invalid amount!"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"✅ Withdrawn Rs.{amount}. Remaining Balance: Rs.{self.balance}"
        else:
            return "❌ Insufficient funds or invalid amount!"

    def display(self):
        return f"👤 Account Holder: {self.name} | 💵 Balance: Rs.{self.balance}"


# ---------------------------
#  Sidebar Navigation
# ---------------------------
st.sidebar.title("🏦 Bank Menu")
menu = st.sidebar.radio("Choose an Option:", ["Create Account", "Deposit", "Withdraw", "View Details", "About Developer"])

# Initialize session state
if 'account' not in st.session_state:
    st.session_state.account = None

# ---------------------------
#  Functional Sections
# ---------------------------
if menu == "Create Account":
    st.header("🧍 Create New Account")
    name = st.text_input("Enter Account Holder Name:")
    balance = st.number_input("Enter Initial Deposit:", min_value=0, value=0)
    if st.button("Create Account"):
        st.session_state.account = BankAccount(name, balance)
        st.success(f"🎉 Account Created for {name} with Rs.{balance} initial deposit.")

elif menu == "Deposit":
    st.header("💰 Deposit Money")
    if st.session_state.account:
        amount = st.number_input("Enter amount to deposit:", min_value=1)
        if st.button("Deposit"):
            st.info(st.session_state.account.deposit(amount))
    else:
        st.warning("⚠️ Please create an account first!")

elif menu == "Withdraw":
    st.header("🏧 Withdraw Money")
    if st.session_state.account:
        amount = st.number_input("Enter amount to withdraw:", min_value=1)
        if st.button("Withdraw"):
            st.info(st.session_state.account.withdraw(amount))
    else:
        st.warning("⚠️ Please create an account first!")

elif menu == "View Details":
    st.header("📄 Account Details")
    if st.session_state.account:
        st.success(st.session_state.account.display())
    else:
        st.warning("⚠️ No account found. Please create one first.")

elif menu == "About Developer":
    st.header("👩‍💻 About Developer")
    st.markdown("""
    **Hamna Munir**  
    💡 *Python | Machine Learning | OOP Enthusiast*  
    🔗 [GitHub Profile](https://github.com/Hamna-Munir)  
    📧 hamnamunir@example.com  
    """)

    st.info("This Streamlit app demonstrates the power of Object-Oriented Programming (OOP) in an interactive way.")

# ---------------------------
#  Footer
# ---------------------------
st.markdown("---")
st.caption("© 2025 | Built with ❤️ by Hamna Munir | Powered by Streamlit")


