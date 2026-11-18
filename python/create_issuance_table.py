import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS issuance (

    issuance_id INTEGER PRIMARY KEY,

    material_id INTEGER,

    issue_date TEXT,

    quantity_issued INTEGER,

    requestor TEXT,

    department TEXT

)
""")

conn.commit()

conn.close()

print("Issuance Table Created Successfully")