'''
If you are running this code first time, and you don't have streamlit installed, then follow this instruction:
1. open a terminal
2. enter this command
    pip install streamlit
'''

import streamlit as st
import oracledb

# --- DATABASE SETUP ---
LIB_DIR = r""
DB_USER = ""
DB_PASS = ""
DB_DSN = ""

@st.cache_resource
def init_db():
    if LIB_DIR:
        try:
            oracledb.init_oracle_client(lib_dir=LIB_DIR)
        except Exception as e:
            st.error(f"Error initializing Oracle Client: {e}")

init_db()

def get_connection():
    return oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)

# --- STREAMLIT UI ---
st.title("Content Management System")
st.subheader("Database Search & Analysis")

menu = [
    "Search by Title", 
    "Search by Genre", 
    "Search by Country", 
    "Search Cast & Crew", 
    "Search Date Info"
]
choice = st.sidebar.selectbox("Navigation", menu)

# Search by title
if choice == "Search by Title":
    st.write("### Content Details")
    title_input = st.text_input("Enter Content Title")
    
    if st.button("Search"):
        try:
            conn = get_connection()
            cur = conn.cursor()
            query = "SELECT * FROM Content WHERE title = :1"
            cur.execute(query, [title_input])
            res = cur.fetchone()
            
            if res:
                # Displaying columns based on ERD: show_id, type, title, rating
                st.write(f"**Show ID:** {res[0]}")
                st.write(f"**Type:** {res[1]}")
                st.write(f"**Title:** {res[2]}")
                st.write(f"**Rating:** {res[3]}")
            else:
                st.warning("No content found with that title.")
            cur.close()
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

# Search by genre
elif choice == "Search by Genre":
    st.write("### Find Content by Genre")
    genre_input = st.text_input("Enter Genre (e.g., Sci-Fi)")
    
    if st.button("Find Content"):
        try:
            conn = get_connection()
            cur = conn.cursor()
            query = """
                SELECT c.title FROM Content c
                JOIN Content_Genre cg ON c.show_id = cg.show_id
                WHERE cg.genre_name = :1
            """
            cur.execute(query, [genre_input])
            data = cur.fetchall()
            if data:
                st.table(data)
            else:
                st.info("No content found for this genre.")
            cur.close()
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

# Search by Country
elif choice == "Search by Country":
    st.write("### Find Content by Country")
    country_input = st.text_input("Enter Country Name")
    
    if st.button("Search"):
        try:
            conn = get_connection()
            cur = conn.cursor()
            query = """
                SELECT c.title FROM Content c
                JOIN Content_Country cc ON c.show_id = cc.show_id
                WHERE cc.country_name = :1
            """
            cur.execute(query, [country_input])
            data = cur.fetchall()
            if data:
                st.table(data)
            else:
                st.info("No records found for that country.")
            cur.close()
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

# Search by People/Roless
elif choice == "Search Cast & Crew":
    st.write("### Associated People and Roles")
    title_input = st.text_input("Enter Content Title for Personnel")
    
    if st.button("Get Credits"):
        try:
            conn = get_connection()
            cur = conn.cursor()
            query = """
                SELECT cp.person_name, cp.role_type
                FROM Content_Person cp
                JOIN Content c ON cp.show_id = c.show_id
                WHERE c.title = :1
            """
            cur.execute(query, [title_input])
            data = cur.fetchall()
            if data:
                st.table(data)
            else:
                st.warning("No people data found for this title.")
            cur.close()
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

# Search by Title
elif choice == "Search Date Info":
    st.write("### Content Release & History")
    title_input = st.text_input("Enter Title for Date Info")
    
    if st.button("Get Dates"):
        try:
            conn = get_connection()
            cur = conn.cursor()
            query = """
                SELECT cd.release_year, cd.date_added
                FROM Content_Dates cd
                JOIN Content c ON cd.show_id = c.show_id
                WHERE c.title = :1
            """
            cur.execute(query, [title_input])
            res = cur.fetchone()
            if res:
                st.write(f"**Release Year:** {res[0]}")
                st.write(f"**Date Added to Platform:** {res[1]}")
            else:
                st.info("No date information available for this title.")
            cur.close()
            conn.close()
        except Exception as e:
            st.error(f"Error: {e}")

# run using: streamlit run app.py