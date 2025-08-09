import sqlite3
import pandas as pd

def get_db_connection(db_path=':memory:'):
    """Create and return a database connection to the given SQLite DB path."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def q(conn, sql, params=None):
    """Run a SQL query and return the results as a pandas DataFrame."""
    params = params or []
    return pd.read_sql_query(sql, conn, params=params)

def find_potential_vips(conn, min_products=3, max_avg_days=30):
    """Identifies 'Engaged' customers who show signs of becoming VIPs.

    Args:
        conn: SQLite connection object.
        min_products: Minimum number of unique products purchased.
        max_avg_days: Maximum average days between purchases.
    """
    sql = """
        WITH ordered_purchases AS (
            SELECT
                customer_id,
                purchase_ts,
                LAG(purchase_ts) OVER (
                    PARTITION BY customer_id
                    ORDER BY purchase_ts
                ) AS prev_ts
            FROM purchases
        ),
        purchase_behavior AS (
            SELECT
                customer_id,
                COUNT(DISTINCT product_id) AS unique_products,
                AVG(julianday(purchase_ts) - julianday(prev_ts)) AS avg_days_between
            FROM ordered_purchases
            WHERE prev_ts IS NOT NULL
            GROUP BY customer_id
        )
        SELECT
            c.id AS customer_id,
            c.name,
            c.best_email,
            pb.unique_products,
            ROUND(pb.avg_days_between, 1) AS avg_days_between
        FROM customers c
        JOIN purchase_behavior pb ON pb.customer_id = c.id
        WHERE pb.unique_products >= ?
          AND pb.avg_days_between < ?
        ORDER BY pb.unique_products DESC, pb.avg_days_between ASC;
    """
    return q(conn, sql, params=[min_products, max_avg_days])
