# Focus Highlight (fremhæv fokus) #

* Forfattere: Takuya Nishimoto
* Download [stabil version][2]
* download [udviklingsversionversion][1]

Dette tilføjelsesprogram tegner et rektangel, så svagsynede brugere, seende
instruktører eller udviklere kan finde placeringen af NVDAs navigatorobjekt
og objektet/kontrollen, som har fokus.

Følgende farver bliver brugt af dette tilføjelsesprogram:

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* Rødt tyndt rektangel for at indikere objektet/kontrolen, som har fokus.
* Rødt tykt rektangel for at indikere, at navigatorobjekt og objekt i fokus
  overlapper.
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

Hvis du vil slå sporing af objekter fra, så afinstaller
tilføjelsesprogrammet.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Changes for 4.0 ##

* Hide rectangle if current application is in sleep mode.

## Ændringer i 3.0 ##

* Fixed issue regarding expanded combo box.
* Løste problem med Windows Programstyring.
* Kan indikere fokustilstand.

## Ændringer i 2.1 ##

* Nye og opdaterede oversættelser.

## Ændringer i 2.0 ##

* Hjælp til tilføjelsesprogrammet er til rådighed fra styring af
  tilføjelsesprogrammer.

## Ændringer i 1.1 ##

* Ændret rektangel for navigatorobjekt til ujævne linjer.
* Løste problem med genindlæsning af tilføjelsesprogrammer.

## Ændringer i 1.0 ##

* Rettet et problem med navigatorobjektet i Internet Explorer 10 og i Skype
  på Windows 8.
* Første version.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
