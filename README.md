# Smart Expense Tracker 💰

A modern, user-friendly expense tracking web application built with **Python, Streamlit, SQLite, Pandas, and Matplotlib**.  
Track daily expenses, view monthly summaries, analyze spending with orange bar charts, and export data — all in a clean browser interface.

🔗 **Live Demo:** https://smart-expence-tracker.streamlit.app/


## 🏗️ Architecture Diagram

```mermaid
graph TD
    U[User] --> A[Streamlit App<br/>app.py]

    A --> S[Sidebar Navigation<br/>Dashboard<br/>Add Expense<br/>Summary<br/>Charts<br/>Export]

    S --> AE[Add Expense]
    AE --> DBF[database.py<br/>add_expense()]
    DBF --> DB[(SQLite DB<br/>expenses.db)]

    S --> VS[View Summary & Charts]
    DB --> EM[expense_manager.py<br/>get_monthly_summary()]
    EM --> DF[Pandas DataFrame]
    DF --> CH[Streamlit Charts]

    S --> EX[Export Data]
    DF --> CSV[Pandas to_csv()<br/>Download CSV]
```
