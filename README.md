# Smart Expense Tracker 💰

A modern, user-friendly expense tracking web application built with Python, Streamlit, SQLite, Pandas, and Matplotlib.  
Track daily expenses, view monthly summaries, analyze spending with orange bar charts, and export data — all in a clean browser interface.

[Expense Tracker Demo: ([https://via.placeholder.com/800x400.png?text=Smart+Expense+Tracker+Screenshot](https://smart-expence-tracker.streamlit.app/))  


```mermaid
graph TD
    U[User] -->|Opens App| A[Streamlit App<br>app.py]
    A --> S[Sidebar Navigation<br>Dashboard | Add Expense | Summary | Charts | Export]
    S --> AE[Add Expense]
    AE --> DBF[database.py<br>add_expense()]
    DBF --> DB[(SQLite DB<br>expenses.db)]
    S --> VS[View Summary / Charts]
    DB --> EM[expense_manager.py<br>get_monthly_summary()]
    EM --> DF[Pandas DataFrame]
    DF --> CH[Streamlit Charts]
    S --> EX[Export Data]
    DF --> CSV[Pandas to_csv()<br>Download CSV]

```
## ✨ Features

- ➕ Add expenses with date, category, amount, and description
- 📊 Monthly summary with category-wise breakdown
- 📈 Interactive orange bar chart showing spending by category
- 📥 Export all expenses to CSV
- 🗄️ Persistent storage using SQLite (no external database needed)
- Clean, responsive Streamlit interface with sidebar navigation
- Month/year selector for historical analysis

## 🛠️ Tech Stack

| Layer            | Technology             |
|------------------|------------------------|
| Frontend         | Streamlit              |
| Backend / Logic  | Python                 |
| Database         | SQLite                 |
| Data Processing  | Pandas                 |
| Visualization    | Matplotlib + Streamlit native charts |
| Styling          | Streamlit built-in + custom colors |

