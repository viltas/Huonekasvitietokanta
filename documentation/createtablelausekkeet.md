# Tietokannan CREATE TABLE -lausekkeet


## Käyttäjä-taulu
CREATE TABLE account ( \
	id INTEGER NOT NULL,  \
	date_created DATETIME,  \
	name VARCHAR(144) NOT NULL,  \
	username VARCHAR(144) NOT NULL,  \
	password VARCHAR(144) NOT NULL, \
	PRIMARY KEY (id),  \
	UNIQUE (username) \
)

## Kasvi-taulu
CREATE TABLE plant ( \
	id INTEGER NOT NULL,  \
	name VARCHAR(144) NOT NULL,  \
	species_id INTEGER,  \
	account_id INTEGER NOT NULL,  \
	species_name VARCHAR(144),  \
	PRIMARY KEY (id),  \
	FOREIGN KEY(species_id) REFERENCES species (id),  \
	FOREIGN KEY(account_id) REFERENCES account (id) \
)
)

## Laji-taulu
CREATE TABLE species (  \
	id INTEGER NOT NULL,   \
	name VARCHAR(144) NOT NULL,  \ 
	genus VARCHAR(144) NOT NULL,  \ 
	epithet VARCHAR(144) NOT NULL, \  
	water VARCHAR(144) NOT NULL, \  
	light VARCHAR(144) NOT NULL,   \
	PRIMARY KEY (id)  \
)

## Tuholaiset-taulu
CREATE TABLE pest ( \
	id INTEGER NOT NULL,  \
	name VARCHAR(144) NOT NULL,  \
	description VARCHAR(400) NOT NULL,  \
	control VARCHAR(400) NOT NULL,  \
	PRIMARY KEY (id)
)

## KasviTuholaiset-taulu
CREATE TABLE plant_pest (   \
	id INTEGER NOT NULL,    \
	plant_id INTEGER,  \
	pest_id INTEGER,  \
	plant_name VARCHAR(144),  \
	pest_name VARCHAR(144),  \
	account_id INTEGER NOT NULL,  \
	PRIMARY KEY (id),  \
	FOREIGN KEY(plant_id) REFERENCES plant (id),  \
	FOREIGN KEY(pest_id) REFERENCES pest (id),  \
	FOREIGN KEY(account_id) REFERENCES account (id) \
)
