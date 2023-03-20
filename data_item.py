import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_items.db")

def items():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, price, instock
        FROM items
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'price': row[1],
            'instock': row[2]
            }
        data.append(record)
    
    conn.close()
    return data

def item(category):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, price , instock
        FROM items 
        WHERE category=?
    """
    val = (category,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()
    data.append(rows[0])
    conn.close()
    return data

def find_item(category):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, price , instock
        FROM items
        WHERE category=?
    """
    val = (category,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'name': rows[0],
        'price': rows[1],
        'category': rows[2]
        }
    data.append(record)
    
    conn.close()
    return data

def add_item(name, price, instock, category):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO username(name, price, instock, category)
        VALUES(?,?,?)
    """
    val = (name, price, instock, category)
    # cursor = conn.execute(sql, val)
    conn.execute(sql, val)
    conn.commit()  
    conn.close()
    return "Created successfully"

def update_item(name, price, instock, category):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE items
        SET name = ?, price =?, instock = ?
        WHERE category = ?
    """
    val = (name, price, instock, category)
    # cursor = conn.execute(sql, val)
    conn.execute(sql, val)
    conn.commit()  
    conn.close()
    return "Updated successfully"

def delete_item(category):
    conn = sqlite3.connect(db_folder)
    sql = f"""
        DELETE FROM items WHERE category = '{category}';
    """
    conn.execute(sql)
    conn.commit()  
    conn.close()
    return "Delete successfully"