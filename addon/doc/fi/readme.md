# Aktiivisen kohdan korostus #

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

To disable object tracking, disable or uninstall the addon.

When Focus Highlight category of NVDA Settings dialog is available,
following items can be used.

* Make focus mode the default: This checkbox is enabled by default. When it
  is unchecked, this add-on behaves same as version 5.6 or previous
  versions, i.e., if browse mode is not available for an app, the focus is
  shown using the thick red rectangle.
* Focus in focus mode, Focus in browse mode, Navigator object: Each of these
  groups contains Color, Thickness, and Style.

    * Color: This edit field allows you to type the HTML color code, i.e.,
      six-character hexadecimal number. For example, "ffffff" is white,
      "ff0000" is red, and so on. Note that "000000" can not be used.
    * Thickness: This edit field allows you to type the thickness of the
      box. You can enter a value between 1 and 30.
    * Style: The choices are Solid, Dash, Dot, Dash dot, and Dash dot-dot.

* Restore defaults: This button allows you to reset your settings to their
  original defaults.

## Changes for 6.1 ##

* Käännöksiä päivitetty ja lisätty.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

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
