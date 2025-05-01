import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
        SELECT 
            l.line_item_id, 
            l.quantity, 
            l.product_id, 
            p.product_name, 
            p.price
        FROM line_items l
        JOIN products p ON l.product_id = p.product_id
    """
    df = pd.read_sql_query(sql_statement, conn)
    print("First 5 rows:")
    print(df.head())
    
    df['total'] = df['quantity'] * df['price']
    print("\nFirst 5 rows after adding 'total':")
    print(df.head())
    
    grouped_df = df.groupby('product_id').agg({
                'line_item_id': 'count',
                'total': 'sum',
                'product_name': 'first'
    })
    grouped_df.rename(columns={'line_item_id': 'order_count','total': 'total_revenue'}, inplace=True)
    
    print("\nGroup by product_id with aggregation:")
    print(grouped_df.head())
    
    sorted_df = grouped_df.sort_values(by='product_name')
    print("\nSort by product_name:")
    print(sorted_df.head())
    
    sorted_df.to_csv("order_summary.csv")
    