import pandas as pd
from datetime import datetime
from database import get_all_expenses

def get_monthly_summary(month=None, year=None):
    df = get_all_expenses()
    if df.empty:
        return None
    
    df['date'] = pd.to_datetime(df['date'])
    if month is None:
        month = datetime.now().month
    if year is None:
        year = datetime.now().year
    
    monthly = df[(df['date'].dt.month == month) & (df['date'].dt.year == year)]
    if monthly.empty:
        return None
    
    summary = monthly.groupby('category')['amount'].agg(['sum', 'count']).reset_index()
    summary.columns = ['Category', 'Total', 'Count']
    grand_total = monthly['amount'].sum()
    
    return {'summary': summary, 'grand_total': grand_total, 'df': monthly}