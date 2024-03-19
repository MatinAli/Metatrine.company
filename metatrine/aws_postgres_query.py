import psycopg2

conn = psycopg2.connect(
    user="superuser",
    password="WodCQk~f$z(U-{k",
    host="metatrine-db.c1iok0oywft2.eu-north-1.rds.amazonaws.com",
    port="5432",
    database="metatrine_db",
)

cursor = conn.cursor()
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE'")
# table_name = '"portfolio_portfoliocategory"'
# cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")
# creation = """
# CREATE TABLE portfolio_portfoliocategory (
#     id BIGSERIAL PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     slug VARCHAR(255) NOT NULL DEFAULT 'corporate',
#     UNIQUE (slug)
# )
# """
# cursor.execute(creation)
# conn.commit()
tables = cursor.fetchall()
table_names = [table[0] for table in tables]
for table_name in table_names:
    print(table_name)
cursor.close()
conn.close()



