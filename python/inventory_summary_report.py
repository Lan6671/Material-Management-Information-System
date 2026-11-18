import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

cursor.execute("""

SELECT

COUNT(*) AS total_materials

FROM materials

""")

total_materials = cursor.fetchone()[0]

cursor.execute("""

SELECT

IFNULL(
    SUM(quantity_received),
    0
)

FROM receiving

""")

total_received = cursor.fetchone()[0]

cursor.execute("""

SELECT

IFNULL(
    SUM(quantity_issued),
    0
)

FROM issuance

""")

total_issued = cursor.fetchone()[0]

current_stock = (
    total_received
    - total_issued
)

print("\nINVENTORY SUMMARY REPORT")
print("=" * 60)

print(
    f"Total Materials : {total_materials}"
)

print(
    f"Total Received  : {total_received}"
)

print(
    f"Total Issued    : {total_issued}"
)

print(
    f"Current Stock   : {current_stock}"
)

conn.close()