# Focus Highlight #

* Autor: Takuya Nishimoto
* Pobierz [wersja stabilna][2]
* Pobierz [wersja rozwojowa][1]

Ten dodatek umożliwia niedowidzącym użytkownikom,widzącym nauczycielom, lub
twórcom śledzenie położenia obiektu nawigatora i punktu uwagi NVDA poprzez
obrysowanie ich kolorowym prostokątem.

Poniższe 2 kolory są stosowane przez ten dodatek:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

Aby wyłączyć śledzenie obiektu, odinstaluj ten dodatek.

## Changes for 6.0 ##

* Nowe i odświeżone tłumaczenia.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Changes for 5.6 ##

* Nowe i odświeżone tłumaczenia.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* Nowe i odświeżone tłumaczenia.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* Nowe i odświeżone tłumaczenia.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* Nowe i odświeżone tłumaczenia.

## Changes for 5.1 ##

* Removed debug log output.

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
