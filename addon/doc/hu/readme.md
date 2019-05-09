# Fókuszkiemelő #

* Készítők: Takuya Nishimoto
* Letöltés [stabil verzió][2]
* Letöltés [fejlesztői verzió][1]

Egy megjelenő színes téglalap segítségével a gyengénlátó felhasználók, látó
fejlesztők vagy oktatók nyomon követhetik a navigátor kurzort és a fókuszban
lévő elemet.

A következő színeket  jeleníti meg a kiegészítő:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

Az elemkövetés kikapcsolásához függessze fel vagy távolítsa el ezt a
kiegészítőt.

## Changes for 6.0 ##

* Új és frissített fordítások
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Changes for 5.6 ##

* Új és frissített fordítások
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* Új és frissített fordítások
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* Új és frissített fordítások
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* Új és frissített fordítások

## Changes for 5.1 ##

* Removed debug log output.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Changes for 4.0 ##

* Hide rectangle if current application is in sleep mode.

## A 3.0 verzió változásai ##

* Fixed issue regarding expanded combo box.
* Javítva egy, a Windows feladatkezelőben előjövő hiba
* A fókuszmód jelzése.

## A 2.1 verzió változásai ##

* Új és frissített fordítások

## A 2.0 verzió változásai ##

* A kiegészítő súgója elérhető a bővítménykezelő párbeszédablakából is.

## Az 1.1 verzió változásai ##

* A navigátor kurzor téglalapja egy szaggatott vonalra lett változtatva.
* A "Bővítmények ujratöltése" hiba javítva.

## Az 1.0 verzió változásai ##

* Javítva egy navigátor kurzor probléma az Internet explorer 10-ben és a
  Skype programokban.
* Első verzió

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
