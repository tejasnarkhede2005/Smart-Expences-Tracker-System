import matplotlib.pyplot as plt

def pie_chart_category(summary_df):
    plt.figure(figsize=(8, 8))
    plt.pie(summary_df['Total'], labels=summary_df['Category'], autopct='%1.1f%%', startangle=90)
    plt.title('Expense Breakdown by Category')
    plt.axis('equal')
    plt.show()

def bar_chart_monthly_trend():
    # Group by month-year, etc.
    pass  # implement if tracking multiple months