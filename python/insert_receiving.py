import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

receipts = [

    (
        1,
        1,
        "PO-1001",
        "2026-10-31",
        500
    ),

    (
        2,
        2,
        "PO-1002",
        "2026-10-31",
        200
    ),

    (
        3,
        3,
        "PO-1003",
        "2026-10-31",
        300
    )

]

cursor.executemany("""

INSERT INTO receiving
(
    receiving_id,
    material_id,
    po_number,
    date_received,
    quantity_received
)

VALUES (?, ?, ?, ?, ?)

""", receipts)

conn.commit()

conn.close()

print("Receiving Records Inserted Successfully")