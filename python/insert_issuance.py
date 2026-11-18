import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

issues = [

    (
        1,
        1,
        "2026-10-31",
        150,
        "Warehouse Supervisor",
        "Construction"
    ),

    (
        2,
        2,
        "2026-10-31",
        50,
        "Maintenance Engineer",
        "Maintenance"
    ),

    (
        3,
        3,
        "2026-10-31",
        75,
        "Project Engineer",
        "Operations"
    )

]

cursor.executemany("""

INSERT INTO issuance
(
    issuance_id,
    material_id,
    issue_date,
    quantity_issued,
    requestor,
    department
)

VALUES (?, ?, ?, ?, ?, ?)

""", issues)

conn.commit()

conn.close()

print("Issuance Records Inserted Successfully")