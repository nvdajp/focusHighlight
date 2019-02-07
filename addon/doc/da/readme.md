# Focus Highlight (fremhæv fokus) #

* Forfattere: Takuya Nishimoto
* Download [stabil version][2]
* Download [udviklingsversion][1]

Dette tilføjelsesprogram tegner et rektangel, så svagsynede brugere, seende
instruktører eller udviklere kan finde placeringen af NVDAs navigatorobjekt
og objektet/kontrollen, som har fokus.

Følgende farver bliver brugt af dette tilføjelsesprogram:

* Grøn og tynd rektangel med tynde skråstreger, der indikere
  navigatorobjektet.
* Rødt tyndt rektangel for at indikere objektet/kontrolen, som har fokus.
* Rødt tykt rektangel for at indikere, at navigatorobjekt og objekt i fokus
  overlapper.
* Blåt rektangel med tyk prikket linje for at indikere, at NVDA er i
  fokustilstand, d.v.s. at tastetryk bliver videregivet til kontrollen.

Hvis du vil slå sporing af objekter fra, så afinstaller
tilføjelsesprogrammet.

## Changes for 5.6 ##

* Nye og opdaterede oversættelser.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* Nye og opdaterede oversættelser.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* Nye og opdaterede oversættelser.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* Nye og opdaterede oversættelser.

## Changes for 5.1 ##

* Removed debug log output.

## Ændringer i 5.0 ##

* Indikatorer på navigator objektet og fokus tilstand blev ændret.
* Flere skærme er nu understøttet.
* Der bruges nu GDI Plus-teknologi til at tegne.

## Ændringer i 4.0 ##

* Skjule rektangel, hvis det aktuelle program er i dvaletilstand.

## Ændringer i 3.0 ##

* Fixed problem med hensyn til udvidet combo box.
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
