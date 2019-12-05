# Huonekasvitietokanta (TSOHA harjoitustyö)

[Heroku](https://huonekasvitietokanta.herokuapp.com)

[User storyt](https://github.com/viltas/Huonekasvitietokanta/blob/master/documentation/userstoryt.md#user-storyt) 

Testitunnukset: käyttäjänimi: monstera, salasana: deliciosa

## Kuvaus

Yleinen ongelma huonekasviharrastajien piireissä on vaikeus pitää kirjaa siitä mitä kaikkia kasveja tarkalleen ottaen omistaa. Viimeistään sadannen ruukun kohdalla kasvien tieteelliset nimet alkavat valua korvista ulos, ja siksi olisikin näppärää olla olemassa jonkinlainen järjestelmä minkä kautta voisi pitää kirjaa omasta kasvikokoelmastaan. Tällainen järjestelmä toimisi myös oivana tapana etsiä uusia kasveja hankintalistalle, sillä huonekasveja ei luonnollisesti voi omistaa liian montaa.

Järjestelmään rekisteröidyttyään käyttäjä voi lisätä itselleen kasveja tietokantaan lisättyjen kasvilajien luettelosta. Käyttäjä voi myös etsiä itselleen sopivia kasveja käyttäen hakukriteereinä kullekin lajille määriteltyä veden ja valon tarvetta. Järjestelmä antaa käyttäjälle mahdollisuuden nimetä kasvinsa (esim. "isomummon peikonlehti"). Kasville voi myös valita omistamistaan kasveista emokasvin tapauksessa jossa kyseinen kasvi on pistokas toisesta kasvista. Kasvin omistajuuden voi myös luovuttaa järjestelmässä eteenpäin, sillä pistokkailla käytävä vaihtokauppa on hyvin tyypillistä kasviharrastajapiireissä.

Kasviharrastuksen varjopuolena ovat erilaiset huonekasvituholaiset. Käyttäjä voi merkitä kasvinsa tarvittaessa saastuneeksi, ja tietokanta tarjoaa kullekin kasvituholaiselle parhaiten sopivan torjuntakeinon.

Ylläpitäjä on ainoa joka voi lisätä järjestelmään uusia kasvilajeja tai tuholaisia. Ylläpitäjä voi myös muokata ja poistaa olemassaolevia lajeja ja tuholaisia, sekä käyttäjien kasveja. Käyttäjät voivat myös itse poistaa kasvejaan järjestelmästä siltä varalta, että tapahtuu vahinko ja isomummon peikonlehti kuolee.


## Toiminnot

- Kasvilajien lisääminen, muokkaus ja poistaminen järjestelmästä
- Kasvien tietojen muuttaminen (toteuttamatta)
- Kasvien hakeminen eri hakukriteereillä (toteuttamatta)
- Käyttäjän rekisteröityminen
- Kirjautuminen järjestelmään käyttäjänä tai ylläpitäjänä (ylläpito-oikeudet toteuttamatta)
- Oman kasvin lisääminen sekä nimeäminen
- Oman kasvin merkitseminen kasvituholaisten saastuttamaksi
- Etusivulla näkyvät käyttäjät joilla ei ole vielä kasveja


## Asentaminen

Käyttäjä voi ladata ohjelman omalle koneelleen ja käyttää sitä seuraavasti:

1. Lataa projekti zip-tiedostona sivun yläreunasta
2. Pura kansio ja hakeudu kansioon terminaalissa
3. Suorita seuraavat komennot:
- ```python3 -m venv venv```
- ```source venv/bin/activate```
- ```pip install -r requirements.txt```
- ```python run.py```
Sovellus löytyy nyt käyttäjän selaimesta osoitteesta 



## Tietokantakaavio
![Tietokantakaavio](https://raw.githubusercontent.com/viltas/Huonekasvitietokanta/master/documentation/kasvitietokanta-kaavio.png)

