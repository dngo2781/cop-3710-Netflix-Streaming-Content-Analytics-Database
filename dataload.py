
import oracledb

LIB_DIR = r""


DB_USER = ""
DB_PASS = ""
DB_DSN  = ""

if LIB_DIR:
    oracledb.init_oracle_client(lib_dir=LIB_DIR)
else: oracledb.enable_thin_mode()

conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
cursor = conn.cursor()
print("Connected to Oracle Database")



import csv

def load_csv_to_table(file_path, table_name, columns):
    print(f"Loading {table_name}...")

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        rows = list(reader)

        placeholders = ",".join([f":{i+1}" for i in range(len(columns))])
        sql = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"

        cursor.executemany(sql, rows)

    conn.commit()
    print(f"{table_name} loaded. Rows: {len(rows)}")


load_csv_to_table("data/content.csv","Content",["show_id","type","title","rating"])

load_csv_to_table("data/genre.csv","Genre",["genre_name"])

load_csv_to_table("data/country.csv","Country",["country_name"])

load_csv_to_table("data/person.csv","Person",["person_name"])


load_csv_to_table("data/content_dates.csv","Content_Dates",["show_id","release_year","date_added"])


load_csv_to_table("data/content_genre.csv","Content_Genre",["show_id","genre_name"])

load_csv_to_table("data/content_country.csv","Content_Country",["show_id","country_name"])

load_csv_to_table("data/content_person.csv","Content_Person",["show_id","person_name","role_type"])

load_csv_to_table("data/season.csv","Season",["show_id","episode_number"])



cursor.close()
conn.close()
print("Oracle connection closed.")