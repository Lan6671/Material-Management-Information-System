import sqlite3

conn = sqlite3.connect("../material_management.db")

cursor = conn.cursor()

materials = [

    (
        1,
        "MAT-001",
        "Steel Plate",
        "PCS",
        "Steel Materials",
        100
    ),

    (
        2,
        "MAT-002",
        "Welding Rod",
        "BOX",
        "Consumables",
        50
    ),

    (
        3,
        "MAT-003",
        "Industrial Pipe",
        "PCS",
        "Piping Materials",
        75
    )

]

cursor.executemany("""

INSERT INTO materials
(
    material_id,
    material_code,
    material_description,
    unit_of_measure,
    category,
    reorder_level
)

VALUES (?, ?, ?, ?, ?, ?)

""", materials)

conn.commit()

conn.close()

print("Material Master Records Inserted Successfully")