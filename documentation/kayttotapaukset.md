# Käyttötapaukset


## Etusivu

Sovelluksen etusivulla käyttäjä näkee kaksi yhteenvetokyselyä.

1) Lista käyttäjistä, joilla on 10 tai enemmän kasveja.
`("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Plant ON Plant.account_id = Account.id"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Plant.id) > 9")`

2) Lista kaikista niistä kasvilajeista jotka ovat sovelluksen (kaikkien!) käyttäjien hallussa.
`("SELECT Species.id, Species.name FROM Species"
                     " LEFT JOIN Plant ON Plant.species_id = Species.id"
                     " GROUP BY Species.id;")`



## Rekisteröityminen



## Sisäänkirjautuminen



## Oman kasvin tallentaminen



## Tuholaistartunnan tallentaminen



## Kasvilajin tallentaminen (ylläpitäjä)



## Tuholaisen tallentaminen (ylläpitäjä)



## Käyttäjän poistaminen (ylläpitäjä)

