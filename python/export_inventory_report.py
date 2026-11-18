import sqlite3
import pandas as pd

conn = sqlite3.connect("../material_management.db")

query = """

SELECT

m.material_code,

m.material_description,

IFNULL(
    SUM(r.quantity_received),
    0
) AS total_received,

IFNULL(
    SUM(i.quantity_issued),
    0
) AS total_issued,

IFNULL(
    SUM(r.quantity_received),
    0
)

-

IFNULL(
    SUM(i.quantity_issued),
    0
)

AS current_stock,

m.reorder_level

FROM materials m

LEFT JOIN receiving r
ON m.material_id = r.material_id

LEFT JOIN issuance i
ON m.material_id = i.material_id

GROUP BY

m.material_code,
m.material_description,
m.reorder_level

"""

df = pd.read_sql_query(
    query,
    conn
)

df.to_excel(
    "../inventory_report.xlsx",
    index=False
)

conn.close()

print(
    "Inventory Report Exported Successfully"
)