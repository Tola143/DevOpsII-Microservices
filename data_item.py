import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_item.db")

def user_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category, price, instock
        FROM items 
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock': row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def username(name):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category, price, instock
        FROM items 
        WHERE name=?
    """
    val = (name,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()
    data.append(rows)
    conn.close()
    return data

# def find_username(name):
#     data = []
#     conn = sqlite3.connect(db_folder)
#     sql = """
#         SELECT name, category, price, instock
#         FROM items 
#         WHERE name=?
#     """
#     val = (name,)
#     cursor = conn.execute(sql,val)
#     rows = cursor.fetchone()

#     record = {
#         'name': rows[0],
#         'category': rows[1],
#         'price': rows[2],
#         'instock': rows[3]
#         }
#     data.append(record)
    
#     conn.close()
#     return data

def user_name_add(name, category, price, instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO items(name, category, price, instock)
        VALUES(?,?,?,?)
    """
    val = (name, category, price, instock)
    conn.execute(sql, val)
    conn.commit()  
    conn.close()
    return "Created successfully"

def update_name(name, category, price, instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE items
        SET name = ?, category = ?, price = ?, instock = ?
        WHERE name = ?
    """
    val = (name, category, price, instock, name)
    # cursor = conn.execute(sql, val)
    conn.execute(sql, val)
    conn.commit()  
    conn.close()
    return "Updated successfully"

def delete_user(name):
    conn = sqlite3.connect(db_folder)
    sql = f"""
        DELETE FROM items WHERE name = '{name}';
    """
    conn.execute(sql)
    conn.commit()  
    conn.close()
    return "Delete successfully"