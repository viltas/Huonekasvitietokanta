# Huonekasvitietokanta

Ohjelma on laadittu Helsingin yliopiston tietokantasovellus-harjoitustyö -kurssia varten. Ohjelmaa on sittemmin jatkokehitetty.

## Sovellus Herokussa

[Heroku](https://huonekasvitietokanta.herokuapp.com)

Testitunnukset:
käyttäjänimi: `monstera`, salasana: `deliciosa`

Ylläpitäjätunnukset: käyttäjänimi:
`admin`, salasana: `123456789`

## Kuvaus

Yleinen ongelma huonekasviharrastajien piireissä on vaikeus pitää kirjaa siitä mitä kaikkia kasveja tarkalleen ottaen omistaa. Viimeistään sadannen ruukun kohdalla kasvien tieteelliset nimet alkavat valua korvista ulos, ja siksi olisikin näppärää olla olemassa jonkinlainen järjestelmä minkä kautta voisi pitää kirjaa omasta kasvikokoelmastaan. Tällainen järjestelmä toimisi myös oivana tapana etsiä uusia kasveja hankintalistalle, sillä huonekasveja ei luonnollisesti voi omistaa liian montaa.

Järjestelmään rekisteröidyttyään käyttäjä voi lisätä itselleen kasveja tietokantaan lisättyjen kasvilajien luettelosta. Järjestelmä antaa käyttäjälle mahdollisuuden nimetä kasvinsa (esim. "isomummon peikonlehti"). Kasviharrastuksen varjopuolena ovat erilaiset huonekasvituholaiset. Käyttäjä voi merkitä kasvinsa tarvittaessa saastuneeksi, ja tietokannasta voi etsiä kullekin kasvituholaiselle parhaiten sopivan torjuntakeinon.

Järjestelmässä voi selata siihen tallennettuja kasvilajeja. Niiden suomenkielisen ja tieteellisen nimen lisäksi tietokantaan on tallennettu tieto kunkin lajin veden ja valon tarpeesta.

Ylläpitäjä on ainoa joka voi lisätä järjestelmään uusia kasvilajeja tai tuholaisia. Ylläpitäjä voi myös muokata ja poistaa olemassaolevia lajeja ja tuholaisia. Käyttäjät voivat itse poistaa omia kasvejaan järjestelmästä siltä varalta, että tapahtuu vahinko ja isomummon peikonlehti kuolee.


## Toiminnot

- Kasvilajien lisääminen ja poistaminen järjestelmästä
- Kasvien tietojen muuttaminen (ylläpitäjä)
- Käyttäjän rekisteröityminen
- Kirjautuminen järjestelmään käyttäjänä tai ylläpitäjänä
- Oman kasvin lisääminen sekä nimeäminen
- Oman kasvin merkitseminen kasvituholaisten saastuttamaksi
- Etusivulla näkyvät tilastot (käyttäjät joilla ei ole vielä kasveja sekä yhteenveto kaikkien käyttäjien hallussa olevista lajeista)


## Dokumentaatio

- [Asennusohje](https://github.com/viltas/Huonekasvitietokanta/blob/master/documentation/asennusohje.md)
- [Käyttöohjeet](https://github.com/viltas/Huonekasvitietokanta/blob/master/documentation/kayttoohje.md)
- [Käyttötapaukset](https://github.com/viltas/Huonekasvitietokanta/blob/master/documentation/kayttotapaukset.md)
- [CREATE TABLE -lausekkeet](https://github.com/viltas/Huonekasvitietokanta/blob/master/documentation/createtablelausekkeet.md)


## Tietokantakaavio
![Tietokantakaavio](https://github.com/viltas/Huonekasvitietokanta/blob/master/documentation/kasvitietokanta_kaavio.png)

