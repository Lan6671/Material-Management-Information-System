import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    material_code,
    material_description,
    unit_of_measure,
    category,
    reorder_level
FROM materials
""")

rows = cursor.fetchall()

print("\nMATERIAL MASTER FILE")
print("=" * 70)

for row in rows:

    print(f"Material Code : {row[0]}")
    print(f"Description   : {row[1]}")
    print(f"Unit          : {row[2]}")
    print(f"Category      : {row[3]}")
    print(f"Reorder Level : {row[4]}")

    print("-" * 70)

conn.close()