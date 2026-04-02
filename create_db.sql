CREATE TABLE Content (
    show_id VARCHAR2(20) PRIMARY KEY,
    type VARCHAR2(20),
    title VARCHAR2(100),
    rating VARCHAR2(10)
);

CREATE TABLE Content_Dates (
    show_id VARCHAR2(20) PRIMARY KEY,
    release_year NUMBER,
    date_added VARCHAR2(50),
    FOREIGN KEY (show_id) REFERENCES Content(show_id)
);

CREATE TABLE Genre (
    genre_name VARCHAR2(100) PRIMARY KEY
);

CREATE TABLE Country (
    country_name VARCHAR2(100) PRIMARY KEY
);

CREATE TABLE Person (
    person_name VARCHAR2(100) PRIMARY KEY
);

CREATE TABLE Content_Genre (
    show_id VARCHAR2(20),
    genre_name VARCHAR2(100),
    PRIMARY KEY (show_id, genre_name),
    FOREIGN KEY (show_id) REFERENCES Content(show_id),
    FOREIGN KEY (genre_name) REFERENCES Genre(genre_name)
);

CREATE TABLE Content_Country (
    show_id VARCHAR2(20),
    country_name VARCHAR2(100),
    PRIMARY KEY (show_id, country_name),
    FOREIGN KEY (show_id) REFERENCES Content(show_id),
    FOREIGN KEY (country_name) REFERENCES Country(country_name)
);

CREATE TABLE Content_Person (
    show_id VARCHAR2(20),
    person_name VARCHAR2(100),
    role_type VARCHAR2(20),
    PRIMARY KEY (show_id, person_name, role_type),
    FOREIGN KEY (show_id) REFERENCES Content(show_id),
    FOREIGN KEY (person_name) REFERENCES Person(person_name)
);

CREATE TABLE Season (
    show_id VARCHAR2(20),
    episode_number NUMBER,
    PRIMARY KEY (show_id, episode_number),
    FOREIGN KEY (show_id) REFERENCES Content(show_id)
);