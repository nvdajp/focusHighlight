# podświetlanie punktu uwagi / Focus Highlight #

* Autor: Takuya Nishimoto
* Pobierz [wersja stabilna][2]
* Pobierz [wersja rozwojowa][1]

Ten dodatek umożliwia niedowidzącym użytkownikom,widzącym nauczycielom, lub
twórcom śledzenie położenia obiektu nawigatora i punktu uwagi NVDA poprzez
obrysowanie ich kolorowym prostokątem.

Poniższe 2 kolory są stosowane przez ten dodatek:

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* Czerwony cienki prostokąt oznacza obiekt/kontrolkę  w punkcie uwagi.
* Czerwony gruby prostokąt oznacza, że obiekt nawigatora i obiekt/kontrolka
  w punkcie uwagi zachodzą na siebie.
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

Aby wyłączyć śledzenie obiektu, odinstaluj ten dodatek.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Zmiany dla 4.0 ##

* Hide rectangle if current application is in sleep mode.

## Zmiany dla 3.0 ##

* Fixed issue regarding expanded combo box.
* Poprawiony problem z 'menedżerzem zadań'.
* Ability to indicate the focus mode.

## Zmiany dla 2.1 ##

* Nowe i odświeżone tłumaczenia.

## Zmiany dla 2.0 ##

* Pomoc dodatku dostępna w managerze dodatków.

## Zmiany dla 1.1 ##

* Zmieniono prostokąt obiektu nawigatora na linię przerywaną.
* Poprawiony problem z 'Przeładuj wtyczki'.

## Zmiany dla 1.0 ##

* W Internet Explorer 10 i Skype dla Windows 8, poprawiony problem z
  obiektem nawigatora.
* Pierwsza wersja.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
