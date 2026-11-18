import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS materials (

    material_id INTEGER PRIMARY KEY,

    material_code TEXT,

    material_description TEXT,

    unit_of_measure TEXT,

    category TEXT,

    reorder_level INTEGER

)
""")

conn.commit()

conn.close()

print("Material Management Database Created Successfully")