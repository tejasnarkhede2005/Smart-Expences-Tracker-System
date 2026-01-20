# Smart-Exapence-Tracker


graph TD
    U[User] -->|Opens App| A[Streamlit App<br>app.py]

    A --> S[Sidebar Navigation<br>Dashboard | Add Expense | Summary | Charts | Export]

    subgraph Data_Flow
        S --> AE[Add Expense]
        AE --> DBF[database.py<br>add_expense()]
        DBF --> DB[(SQLite DB<br>expenses.db)]

        S --> VS[View Summary / Charts]
        DB --> EM[expense_manager.py<br>get_monthly_summary()]
        EM --> DF[Pandas DataFrame]
        DF --> CH[Streamlit Charts<br>Bar / Pie]

        S --> EX[Export Data]
        DF --> CSV[Pandas to_csv()<br>Download CSV]
    end

    style A fill:#1e3a8a,color:#ffffff,stroke:#ffffff
    style DB fill:#065f46,color:#ffffff,stroke:#ffffff

