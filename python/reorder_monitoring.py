import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

cursor.execute("""

SELECT

m.material_code,

m.material_description,

m.reorder_level,

IFNULL(
    SUM(r.quantity_received),
    0
)

-

IFNULL(
    SUM(i.quantity_issued),
    0
)

AS current_stock

FROM materials m

LEFT JOIN receiving r
ON m.material_id = r.material_id

LEFT JOIN issuance i
ON m.material_id = i.material_id

GROUP BY

m.material_code,
m.material_description,
m.reorder_level

""")

rows = cursor.fetchall()

print("\nREORDER LEVEL MONITORING REPORT")
print("=" * 80)

for row in rows:

    current_stock = row[3]

    if current_stock <= row[2]:
        status = "REORDER REQUIRED"
    else:
        status = "SUFFICIENT STOCK"

    print(f"Material Code : {row[0]}")
    print(f"Description   : {row[1]}")
    print(f"Current Stock : {current_stock}")
    print(f"Reorder Level : {row[2]}")
    print(f"Status        : {status}")

    print("-" * 80)

conn.close()