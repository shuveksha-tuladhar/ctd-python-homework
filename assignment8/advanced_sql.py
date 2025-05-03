import sqlite3

def print_result(result, message):
    print(message)
    for row in result:
        print(row)
        
with sqlite3.connect("../db/lesson.db") as conn:
    try:
        conn.execute("PRAGMA foreign_keys = 1")

        cursor = conn.cursor()

        # Task 1: Complex JOINs with Aggregation
        sql_statement = """ SELECT o.order_id,
            SUM(l.quantity * p.price) AS total_price
            FROM orders o
            JOIN line_items l ON o.order_id = l.order_id
            JOIN products p ON l.product_id = p.product_id
            GROUP BY o.order_id
            ORDER BY o.order_id
            LIMIT 5;
        """
        cursor.execute(sql_statement)
        print_result(cursor.fetchall(), "Task 1: Complex JOINs with Aggregation")
        
        # Task 2: Understanding Subqueries
        sql_avg_query = """ SELECT c.customer_name,
            AVG(sub.total_price) AS average_total_price
            FROM customers c
            LEFT JOIN (
                SELECT o.customer_id AS customer_id_b,
                    SUM(l.quantity * p.price) AS total_price
                FROM orders o
                JOIN line_items l ON o.order_id = l.order_id
                JOIN products p ON l.product_id = p.product_id
                GROUP BY o.order_id
            ) AS sub ON c.customer_id = sub.customer_id_b
            GROUP BY c.customer_id
            LIMIT 5;
            """

        cursor.execute(sql_avg_query)
        print_result(cursor.fetchall(), "Task 2: Understanding Subqueries")
        
        # Task 3: An Insert Transaction Based on Data
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
        customer_id = cursor.fetchone()[0]
        
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
        employee_id = cursor.fetchone()[0]
        
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_ids = [row[0] for row in cursor.fetchall()]
        
        print("Inserting data into orders")
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]
        
        print("Inserting data into line_items")
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, 10)
            """, (order_id, product_id))

        sql_insert_statement = """
            SELECT o.order_id, l.line_item_id, l.quantity, p.product_name
            FROM products p
            JOIN line_items l ON l.product_id = p.product_id
            JOIN orders o ON o.order_id = l.order_id
            WHERE o.order_id = ?;
        """
        conn.commit()
        
        cursor.execute(sql_insert_statement, (order_id,))
        print_result(cursor.fetchall(), "Task 3: An Insert Transaction Based on Data")
        
        cursor.execute("DELETE FROM line_items WHERE order_id = ?", (order_id,))
        cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
        conn.commit()
        
        # Task 4: Aggregation with HAVING
        sql_query = """SELECT 
                e.employee_id, 
                e.first_name, 
                e.last_name, 
                COUNT(o.order_id) AS order_count
            FROM employees e
            JOIN orders o ON e.employee_id = o.employee_id
            GROUP BY e.employee_id
            HAVING COUNT(o.order_id) > 5
        """
        cursor.execute(sql_query)
        print_result(cursor.fetchall(), "Task 4: Aggregation with HAVING")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
