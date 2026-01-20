import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Import your modules (adjust names if different)
from database import init_db, add_expense, get_all_expenses
from expense_manager import get_monthly_summary
from visuals import pie_chart_category   # we'll adapt it

# ────────────────────────────────────────
# Page config
st.set_page_config(
    page_title="Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# Initialize DB once
init_db()

# ────────────────────────────────────────
# Sidebar menu
st.sidebar.title("Smart Expense Tracker")
page = st.sidebar.radio(
    "Menu",
    ["🏠 Dashboard", "➕ Add Expense", "📊 Monthly Summary", "📈 Charts", "📥 Export"]
)

# ────────────────────────────────────────
if page == "🏠 Dashboard":
    st.title("💰 Welcome to Smart Expense Tracker")
    st.markdown("Track your expenses easily — powered by Python, SQLite & Streamlit")

    df = get_all_expenses()
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        total_spent = df['amount'].sum()
        st.metric("Total Expenses (All Time)", f"₹{total_spent:,.2f}")

        latest = df.iloc[0]
        st.info(f"Latest expense: {latest['category']} - ₹{latest['amount']} on {latest['date'].strftime('%d %b %Y')}")
    else:
        st.info("No expenses recorded yet. Add your first one!")

# ────────────────────────────────────────
elif page == "➕ Add Expense":
    st.header("Add New Expense")

    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Date", value=datetime.today())
    with col2:
        amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0, format="%.2f")

    category = st.selectbox(
        "Category",
        ["Food", "Transport", "Rent", "Utilities", "Entertainment", "Shopping", "Health", "Others"]
    )
    custom_cat = st.text_input("Custom category (optional)")
    if custom_cat.strip():
        category = custom_cat.strip()

    description = st.text_area("Description / Note", height=80)

    if st.button("Save Expense", type="primary"):
        if amount > 0:
            date_str = date.strftime("%Y-%m-%d")
            add_expense(date_str, category, description, amount)
            st.success(f"Added ₹{amount} in {category} on {date_str} ✅")
        else:
            st.error("Amount must be greater than 0")

# ────────────────────────────────────────
elif page == "📊 Monthly Summary":
    st.header("Monthly Summary")

    now = datetime.now()
    month = st.selectbox("Month", range(1, 13), index=now.month-1)
    year = st.number_input("Year", min_value=2020, max_value=now.year+1, value=now.year)

    result = get_monthly_summary(month, year)
    if result and not result['summary'].empty:
        st.subheader(f"Total this month: ₹{result['grand_total']:,.2f}")

        st.dataframe(
            result['summary'].style.format({"Total": "₹{:,.2f}"}),
            use_container_width=True
        )

        # Quick stats
        top_cat = result['summary'].loc[result['summary']['Total'].idxmax()]
        st.info(f"Biggest category: **{top_cat['Category']}** (₹{top_cat['Total']:,.2f})")
    else:
        st.info("No expenses found for selected month.")

# ────────────────────────────────────────
elif page == "📈 Charts":
    st.header("Visual Insights")

    result = get_monthly_summary()  # current month by default
    if result and not result['summary'].empty:
        tab1, tab2 = st.tabs(["Pie Chart – Category Breakdown", "Bar Chart"])

        with tab1:
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(
                result['summary']['Total'],
                labels=result['summary']['Category'],
                autopct='%1.1f%%',
                startangle=90,
                shadow=True
            )
            ax.set_title("Expense Breakdown by Category")
            st.pyplot(fig)

        with tab2:
            st.bar_chart(
                result['summary'].set_index('Category')['Total'],
                use_container_width=True
            )
    else:
        st.info("No data available to visualize yet.")

# ────────────────────────────────────────
elif page == "📥 Export":
    st.header("Export Data")

    df = get_all_expenses()
    if not df.empty:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download All Expenses as CSV",
            data=csv,
            file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
        st.dataframe(df)
    else:
        st.info("No data to export.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit • SQLite • Pandas • Matplotlib")