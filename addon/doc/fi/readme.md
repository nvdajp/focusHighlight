# Kohdistuksen korostus #

* Tekijä: Takuya Nishimoto
* Lataa [vakaa versio][2]
* Lataa [kehitysversio][1]

Tämä lisäosa piirtää näytölle värillisen suorakulmion, mikä mahdollistaa
osittain näkeville käyttäjille, näkeville opettajille tai kehittäjille
NVDA:n navigointiobjektin ja aktiivisen objektin/säätimen sijainnin
seuraamisen.

Seuraavia värejä käytetään:

* Vihreä, ohut, katko- ja pisteviivainen suorakulmio ilmaisee NVDA:n olevan
  selaustilassa sekä näyttää navigointiobjektin.
* Punainen, ohut suorakulmio, joka ilmaisee NVDA:n olevan selaustilassa sekä
  näyttää aktiivisen objektin/säätimen.
* Punainen, paksu suorakulmio, joka ilmaisee NVDA:n olevan selaustilassa
  sekä näyttää, että navigointiobjekti ja aktiivinen objekti ovat
  päällekkäin.
* Sininen, paksu pisteviivainen suorakulmio ilmaisee NVDA:n olevan
  vuorovaikutustilassa, ts. näppäinpainallukset välitetään nykyiselle
  säätimelle.

Poista objektin seuranta käytöstä poistamalla käytöstä tai poistamalla tämä
lisäosa.

Seuraavia asetuksia voidaan muuttaa, kun NVDA:n asetusvalintaikkunan
Kohdistuksen korostus -kategoria on käytettävissä.

* Käytä oletusarvoisesti vuorovaikutustilaa: Tämä valintaruutu on
  oletusarvoisesti valittuna. Kun sitä ei ole valittu, tämä lisäosa toimii
  kuten versio 5.6 tai sitä aiemmat, ts. jos selaustila ei ole käytettävissä
  sovelluksessa, kohdistuksen näyttämiseen käytetään paksua punaista
  suorakulmiota.
* Kohdistus vuorovaikutustilassa, Kohdistus selaustilassa,
  Navigointiobjekti: Näissä ryhmissä on seuraavat asetukset: Väri, Paksuus,
  ja Tyyli.

    * Väri: Tähän muokkauskenttään voidaan syöttää värin HTML-koodi,
      ts. 6-merkkinen heksadesimalinumero. Esim. "ffffff" on valkoinen,
      "ff0000" on punainen jne. Huom: Arvoa "000000" ei voi käyttää.
    * Paksuus: Tähän muokkauskenttään voidaan kirjoittaa laatikon
      paksuus. Arvot väliltä 1-30 ovat mahdollisia.
    * Tyyli: Valittavissa ovat vaihtoehdot Kiinteä, Viiva, Piste, Viiva ja
      piste sekä Viiva ja kaksi pistettä.

* Palauta oletukset: Tällä painikkeella voi palauttaa asetukset
  alkuperäisiin oletusarvoihinsa.

## Muutokset versiossa 6.1 ##

* Käännöksiä päivitetty ja lisätty.
* Korjaa [ongelman](https://github.com/nvdajp/focusHighlight/issues/14)
  viimeisimpien NVDA:n kehitysversioissa.
* NVDA:n asetusvalintaikkunan Kohdistuksen korostus -kategoria on nyt
  käytettävissä  NVDA 2018.3:ssa ja sitä uudemmissa versioissa.
* [Värien mukauttamiseen liittyvät
  keskustelut](https://github.com/nvdajp/focusHighlight/issues/3)
* [Vuorovaikutustilan oletusarvoiseen käyttämiseen liittyvät
  keskustelut](https://github.com/nvdajp/focusHighlight/issues/13)

## Muutokset versiossa 6.0 ##

* Käännöksiä päivitetty ja lisätty.
* Korjaa [ongelman](https://github.com/nvdajp/focusHighlight/issues/13),
  joka liittyy selaustilaan.
* Mikäli selaustila ei ole käytettävissä sovelluksessa, tästä
  lisäosaversiosta alkaen näytetään aina NVDA:n olevan vuorovaikutustilassa
  sen sijaan, että näytettäisiin paksu punainen suorakulmio.
* Vuorovaikutustilaa ilmaisevan viivan paksuutta on vähennetty puoleen
  aiemmasta.

## Muutokset versiossa 5.6 ##

* Käännöksiä päivitetty ja lisätty.
* Korjaa yhteensopivuusongelman NVDA:n alfa-kehitysversion 16682 kanssa.

## Muutokset versiossa 5.5 ##

* Korjaa NVDA 2018.4:n ja Firefox/Chrome-verkkoselainten kanssa olleen
  ongelman.

## Muutokset versiossa 5.4 ##

* Käännöksiä päivitetty ja lisätty.
* Korjaa [ongelman](https://github.com/nvdajp/focusHighlight/issues/11),
  joka liittyy versioyhteensopivuuteen.

## Muutokset versiossa 5.3 ##

* Käännöksiä päivitetty ja lisätty.
* Korjaa [ongelman](https://github.com/nvdajp/focusHighlight/issues/10),
  joka liittyy Chrome-selaimeen ja sovelluksen lepotilaan.

## Muutokset versiossa 5.2 ##

* Käännöksiä päivitetty ja lisätty.

## Muutokset versiossa 5.1 ##

* Poistettu virheenkorjauslokin tulostus.

## Muutokset versiossa 5.0 ##

* Navigointiobjektin ja vuorovaikutustilan ilmaisimia on muutettu.
* Useita näyttöjä tuetaan.
* Piirtämiseen käytetään nyt GDI Plus -teknologiaa.

## Muutokset versiossa 4.0 ##

* Suorakulmio piilotetaan, mikäli nykyinen sovellus on lepotilassa.

## Muutokset versiossa 3.0 ##

* Korjattu avatun yhdistelmäruudun ongelma.
* Korjattu Windowsin Tehtävienhallinnan kanssa ilmennyt ongelma.
* Mahdollisuus vuorovaikutustilan ilmaisemiseen.

## Muutokset versiossa 2.1 ##

* Käännöksiä päivitetty ja lisätty.

## Muutokset versiossa 2.0 ##

* Ohje on käytettävissä Lisäosien hallinnasta.

## Muutokset versiossa 1.1 ##

* Navigointiobjektia ilmaiseva suorakulmio muutettu epätasaiseksi viivaksi.
* Korjattu 'Lataa liitännäiset uudelleen' -toiminnon kanssa ilmennyt
  ongelma.

## Muutokset versiossa 1.0 ##

* Korjattu navigointiobjektin ongelma Internet Explorer 10:ssä ja Skypessä
  Windows 8:aa käytettäessä.
* Ensimmäinen versio.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
