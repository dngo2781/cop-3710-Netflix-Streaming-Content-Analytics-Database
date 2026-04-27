# cop-3710-Netflix-Streaming-Content-Analytics-Database

### Project Scope

A database for analysis of streamed content sourced from a Netflix database. Includes analyzing shows/movies, their genres, country, ratings, dates, summary, with materialized views for genre popularity, country-based partitions, and stored procedures for content ranking. Done with Oracle SQL.

### Users

Data analysts, researchers, students, and those interested in looking at streamed content and their trends.

### Data Source
https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download
<br>Attributes: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

<img width="1273" height="582" alt="image" src="https://github.com/user-attachments/assets/115cd45e-7fca-4f25-90df-d6ceccb5172e" />


### How to Use

1. Set up an empty Oracle SQL database.
2. Create the database tables using the create_db.sql.
3. Run dataload.py (after entering the database connection credentials) to insert the data into the database.
4. Install streamlit (`python -m pip install streamlit`) if not already installed.
5. Run app.py (after entering the database connection credentials) using streamlit (`python -m streamlit run app.py`) to search the database.
<img width="1905" height="835" alt="image" src="https://github.com/user-attachments/assets/810ceaed-af6c-4d9f-8a85-4533ea4c6500" />
