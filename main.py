from database import init_db, add_expense, get_all_expenses
from expense_manager import get_monthly_summary
from visuals import pie_chart_category
import pandas as pd
from datetime import datetime

def main():
    init_db()
    while True:
        print("\n=== Smart Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Show Category Pie Chart")
        print("5. Export to CSV")
        print("0. Exit")
        
        choice = input("Choose: ")
        
        if choice == '1':
            date = datetime.now().strftime('%Y-%m-%d')  # or input
            category = input("Category (Food/Transport/etc): ")
            desc = input("Description: ")
            try:
                amount = float(input("Amount: "))
                add_expense(date, category, desc, amount)
                print("Expense added!")
            except ValueError:
                print("Invalid amount!")
        
        elif choice == '2':
            df = get_all_expenses()
            if not df.empty:
                print(df.to_string(index=False))
            else:
                print("No expenses yet.")
        
        elif choice == '3':
            result = get_monthly_summary()
            if result:
                print(f"\nMonthly Total: ₹{result['grand_total']:.2f}")
                print(result['summary'].to_string(index=False))
            else:
                print("No expenses this month.")
        
        elif choice == '4':
            result = get_monthly_summary()
            if result and not result['summary'].empty:
                pie_chart_category(result['summary'])
            else:
                print("No data to plot.")
        
        elif choice == '5':
            df = get_all_expenses()
            if not df.empty:
                df.to_csv('expenses_export.csv', index=False)
                print("Exported to expenses_export.csv")
            else:
                print("Nothing to export.")
        
        elif choice == '0':
            break

if __name__ == "__main__":
    main()