# Käyttötapaukset


## Etusivu

Sovelluksen etusivulla käyttäjä näkee kaksi yhteenvetokyselyä.

1) Lista käyttäjistä, joilla on 10 tai enemmän kasveja.  
`SELECT Account.id, Account.name FROM Account  
                    LEFT JOIN Plant ON Plant.account_id = Account.id  
                    GROUP BY Account.id  
                    HAVING COUNT(Plant.id) > 9`

2) Lista kaikista niistä kasvilajeista jotka ovat sovelluksen (kaikkien!) käyttäjien hallussa.  
`"SELECT Species.id, Species.name  FROM Species"
                     " INNER JOIN Plant ON Plant.species_id = Species.id"
                     " GROUP BY Species.id;"`



## Rekisteröityminen

Käyttäjä voi luoda sovellukseen uuden käyttäjätunnuksen.

`INSERT INTO account (date_created, name, username, password) VALUES (CURRENT_TIMESTAMP, ?, ?, ?)`


## Sisäänkirjautuminen

Käyttäjä voi kirjautua sisään luomallaan käyttäjätunnuksella.

`SELECT account.id AS account_id, account.date_created AS account_date_created, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.username = ? AND account.password = ?
 LIMIT ? OFFSET ?`


## Oman kasvin tallentaminen

Käyttäjä voi tallentaa sovellukseen oman kasvinsa, ja valita sille nimen sekä lajin.

`SELECT plant.id AS plant_id, plant.name AS plant_name, plant.species_id AS plant_species_id, plant.account_id AS plant_account_id, plant.species_name AS plant_species_name 
FROM plant 
WHERE plant.account_id = ?`


## Tuholaistartunnan tallentaminen

Käyttäjä voi merkitä tuholaisten saastuttamasta kasvistaan tiedon sovellukseen. Tieto sisältää kasvin nimen sekä tuholaisen joka sen kimppuun on käynyt.

`SELECT plant_pest.id AS plant_pest_id, plant_pest.plant_id AS plant_pest_plant_id, plant_pest.pest_id AS plant_pest_pest_id, plant_pest.plant_name AS plant_pest_plant_name, plant_pest.pest_name AS plant_pest_pest_name, plant_pest.account_id AS plant_pest_account_id 
FROM plant_pest 
WHERE plant_pest.account_id = ?`


## Kasvilajin tallentaminen (ylläpitäjä)

Ylläpitäjä voi tallentaa sovellukseen uusia kasvilajeja tallentaen niiden tieteellisen nimen (kahdessa osassa), suomenkielisen nimen sekä veden ja valon tarpeen.

`SELECT species.id AS species_id, species.name AS species_name, species.genus AS species_genus, species.epithet AS species_epithet, species.water AS species_water, species.light AS species_light 
FROM species`


## Tuholaisen tallentaminen (ylläpitäjä)

Ylläpitäjä voi tallentaa sovellukseen tietoja tuholaisista. Tiedot koostuvat tuholaisten nimistä, kuvauksesta ja torjuntatavasta.

`SELECT pest.id AS pest_id, pest.name AS pest_name, pest.description AS pest_description, pest.control AS pest_control 
FROM pest`


## Käyttäjän poistaminen (ylläpitäjä)

Ylläpitäjä voi poistaa muiden käyttäjien tunnuksia sovelluksesta.

`SELECT account.id AS account_id, account.date_created AS account_date_created, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.id != ?`


