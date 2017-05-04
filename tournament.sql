-- Table definitions for the tournament project.

--Dropping existing database
DROP DATABASE IF EXISTS tournament;

--creating database
CREATE DATABASE tournament;



--connect database
\c tournament;



CREATE TABLE Player ( p_id SERIAL PRIMARY KEY, name TEXT);


CREATE TABLE match (m_id SERIAL PRIMARY KEY,
                     w_id INTEGER REFERENCES Player(p_id),
                      l_id INTEGER REFERENCES Player(p_id));
