# Käyttöohjeet

Sovellusta käytetään yläpalkin (kirjautuminen) ja pudotusvalikon (yläpalkin oikea reuna) avulla. Sovelluksen etusivulla on tervetuloa-tekstin lisäksi kaksi automaattista yhteenvetokyselyä. Ensimmäinen niistä listaa käyttäjät, joilla on 10 tai enemmän omaa kasvia. Jälkimmäinen taas koostaa yhteenvedon kaikista käyttäjien hallussa olevista kasvilajeista.

## Normaalikäyttäjän toiminnot

#### Tunnuksen luominen ja kirjautuminen
Uusi käyttäjä luodaan sovelluksen yläpalkin `Luo tunnus` -linkkiä painamalla. Käyttäjää luodessa valitaan käyttäjän nimi, käyttäjätunnus sekä salasana. Käyttäjätunnusta ja salasanaa käytetään kirjautumiseen, ja sama käyttäjätunnus ei voi esiintyä sovelluksessa kahdesti. Käyttäjän nimen tulee olla 3-30 merkkiä pitkä, käyttäjätunnuksen 3-10 merkkiä pitkä ja salasanan 10-30 merkkiä pitkä.

Kirjautuminen tapahtuu `Kirjaudu sisään` -linkin takaa. Linkkiä painamalla aukeaa lomake, johon syötetään käyttäjätunnus ja salasana. Sisäänkirjautumisen jälkeen päästään takaisin sovelluksen etusivulle.

Uloskirjautuminen tapahtuu samasta paikasta. Sisäänkirjautumisen jälkeen yläpalkkiin ilmestyy teksti `Hei Käyttäjän Nimi -- Kirjaudu ulos`, ja tämä teksti toimii uloskirjautumislinkkinä.


#### Omien kasvien lisääminen
Pudotusvalikosta löytyvän `Lisää oma kasvi` -linkin takaa aukeaa lomake, johon syötetään oman kasvin tiedot. Kasvin laji valitaan lomakkeen pudotusvalikosta, ja sen jälkeen kasville annetaan nimi. Nimen tulee olla 3-30 merkkiä pitkä. `Lisää uusi kasvi` -nappi tallentaa kasvin tietokantaan.

Tietokannassa tulee olla tallennettuna ainakin yksi laji, jotta käyttäjä voi tallentaa omia kasvejaan. Jos sopivaa lajia ei löydy, tulee ylläpitäjän lisätä sellainen tietokantaan.

#### Omien kasvien selaaminen, muokkaus ja poistaminen
`Listaa omat kasvit` -linkin takaa aukeaa lista jossa käyttäjä näkee yhteenvedon omista kasveistaan (kasvien nimet sekä lajit). `Poista` -nappi poistaa kasvin tietokannasta. Jos tietokantaan on tallennettu kyseiseen kasviin liittyviä tuholaistartuntoja, myös ne poistuvat. `Muokkaa` -napin takaa aukeaa samanlainen lomake kuin kasvia lisätessä, ja sen kautta voi päivittää kasvin nimen ja lajin.


#### Oman kasvin merkitseminen saastuneeksi
Tuholaistartunnat lisätään `Lisää tartunta` -linkin takaa avautuvalla lomakkeella, jossa on kaksi pudotusvalikkoa. Ensimmäisestä valikosta valitaan tartunnan saanut kasvi ja toisesta kasviin iskenyt tuholainen. Tartunta tallennetaan `Lisää uusi tartunta` -painikkeen kautta. 


#### Tartuntojen selaaminen ja poistaminen
`Listaa tartunnat` -linkkiä painamalla päästään yhteenvetonäkymään, jossa nähdään tartunnan saaneet kasvit ja niihin iskeneet tuholaiset. Kunkin rivin vieressä on `Poista tartunta` -nappi, josta tartunnan voi poistaa.


#### Lajien selaaminen
Pudotusvalikon `Listaa lajit` -linkin takaa löytyy Kasvilajit-lista. Siinä nähdään tietokantaan tallennettujen kasvilajien koko tieteellinen nimi (suku + epiteetti), suomenkielinen nimi sekä kasvin veden tarve ja valon tarve. Veden tarve ilmoitetaan akselilla vähäinen - kohtalainen - tasainen kosteus. Valon tarve taas varjo - puolivarjo - hajavalo - runsas valo.

#### Tuholaisten selaaminen
`Listaa tuholaiset` -linkistä päästään tuholaisyhteenvetoon josta löytyy tuholaisten nimien lisäksi niiden tuntomerkit sekä torjuntaohjeet.


## Ylläpitäjän toiminnot

Seuraavat ominaisuudet ovat saatavilla vain ylläpitotunnuksilla kirjautuessa.

#### Lajien lisääminen
`Lisää laji` -linkin takaa löytyy lomake jonka kautta ylläpitäjä voi lisätä tietokantaan uusia kasveja. Lomakkeen kautta kasville annetaan suku, epiteetti ja nimi, sekä valitaan sitä kuvaavat valon ja veden tarve.

#### Lajien muokkaus ja poistaminen
Lajien poistaminen tapahtuu saman linkin takaa kuin niiden listanäkymän tarkastelu. Ylläpitäjälle kunkin lajin vieressä näkyvät `Poista` sekä `Muokkaa` -napit, jotka toimivat nimiensä mukaisesti. Muokkausnäkymä on samanlainen kuin uuden lajin lisäysnäkymä, ja se luonnollisesti päivittää muokattavan kasvin tiedot.

#### Tuholaisten lisääminen
Tuholaisten lisääminen tapahtuu `Lisää tuholainen` -linkin takaa. Ylläpitäjän tulee antaa tuholaiselle nimi, tuntomerkit sekä lyhyt kuvaus tuholaista koskevista torjuntamenetelmistä.

#### Tuholaisten muokkaus ja poistaminen
Tuholaisia koskevan listanäkymän vieressä näkyvät ylläpitäjälle työkalut muokkaamiseen ja poistamiseen samaan tapaan kuin kasvilajien kohdalla. 

#### Käyttäjien hallinta
Ylläpitäjä pääsee käsiksi `Hallitse käyttäjiä`-linkkiin, jonka takaa löytyy käyttäjien tiedot listana. Ylläpitäjä näkee käyttäjien id-tunnuksen, nimen, käyttäjätunnuksen ja tunnuksen luontiajankohdan. Kunkin käyttäjän vieressä on `Poista käyttäjä` -nappi jonka kautta käyttäjän voi poistaa. Lista näyttää vain normaalit käyttäjät, jotta ylläpitäjä ei epähuomiossa tule poistaneeksi itseään.