# Smart Expense Tracker 💰

A modern, user-friendly expense tracking web application built with Python, Streamlit, SQLite, Pandas, and Matplotlib.  
Track daily expenses, view monthly summaries, analyze spending with orange bar charts, and export data in a clean browser interface.

🔗 Live Demo: https://smart-expence-tracker.streamlit.app/

---

## 🏗️ Architecture Diagram

```mermaid
graph TD
    U[User] --> A[Streamlit App]

    A --> S[Sidebar Navigation]
    S --> AE[Add Expense]
    S --> VS[View Summary and Charts]
    S --> EX[Export Data]

    AE --> DBF[database.py add_expense]
    DBF --> DB[SQLite Database]

    DB --> EM[expense_manager.py get_monthly_summary]
    EM --> DF[Pandas DataFrame]
```

    DF --> CH[Charts]
    DF --> CSV[CSV Export]
