import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

cursor.execute("""

SELECT

m.material_code,

m.material_description,

IFNULL(
    r.quantity_received,
    0
),

IFNULL(
    i.quantity_issued,
    0
),

IFNULL(
    r.quantity_received,
    0
)
-
IFNULL(
    i.quantity_issued,
    0
)

FROM materials m

LEFT JOIN receiving r
ON m.material_id = r.material_id

LEFT JOIN issuance i
ON m.material_id = i.material_id

""")

rows = cursor.fetchall()

print("\nSTOCK CARD REPORT")
print("=" * 80)

for row in rows:

    print(f"Material Code : {row[0]}")
    print(f"Description   : {row[1]}")
    print(f"Received      : {row[2]}")
    print(f"Issued        : {row[3]}")
    print(f"Balance       : {row[4]}")

    print("-" * 80)

conn.close()