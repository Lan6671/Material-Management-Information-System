import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS receiving (

    receiving_id INTEGER PRIMARY KEY,

    material_id INTEGER,

    po_number TEXT,

    date_received TEXT,

    quantity_received INTEGER

)
""")

conn.commit()

conn.close()

print("Receiving Table Created Successfully")