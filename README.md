# Smart-Exapence-Tracker


### 2. Mermaid Chart Code (Architecture Flow)

```mermaid
graph TD
    A[User] -->|Opens browser| B[Streamlit App<br>app.py]

    B --> C[Sidebar Menu<br>Dashboard • Add • Summary • Charts • Export]

    subgraph "Data Flow"
        C --> D[Add Expense]
        D --> E[database.py<br>→ add_expense() → SQLite expenses.db]

        C --> F[View Summary / Charts]
        F --> G[expense_manager.py<br>→ get_monthly_summary() → Pandas DataFrame]

        G --> H[visuals / Streamlit<br>→ Orange Bar Chart<br>st.bar_chart(color='#FF8C00')]

        C --> I[Export CSV]
        I --> J[Pandas → to_csv() → Download button]
    end

    E -->|Persistent storage| K[(SQLite Database<br>expenses table)]
    K -->|SELECT queries| G

    style B fill:#1e3a8a,stroke:#fff,stroke-width:2px,color:#fff
    style K fill:#065f46,stroke:#fff,color:#fff

```



