# Focus Highlight (fremhæv fokus) #

* Forfattere: Takuya Nishimoto
* Download [stabil version][2]
* Download [udviklingsversion][1]

Dette tilføjelsesprogram tegner et rektangel, så svagsynede brugere, seende
instruktører eller udviklere kan finde placeringen af NVDAs navigatorobjekt
og objektet/kontrollen, som har fokus.

Følgende farver bliver brugt af dette tilføjelsesprogram:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

Hvis du vil slå sporing af objekter fra, så afinstaller
tilføjelsesprogrammet.

## Changes for 6.0 ##

* Nye og opdaterede oversættelser.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Ændringer for 5.6 ##

* Nye og opdaterede oversættelser.
* Løser kompatibilitetsproblemet med NVDA snapshot alpha-16682.

## Ændringer for 5.5 ##

* Løser problemet med NVDA 2018.4 og Firefox / Chrome webbrowsere.

## Ændringer for 5.4 ##

* Nye og opdaterede oversættelser.
* Løser [problemet](https://github.com/nvdajp/focusHighlight/issues/11)
  angående versionskompatibilitet.

## Ændringer for 5.3 ##

* Nye og opdaterede oversættelser.
* retter [problemet](https://github.com/nvdajp/focusHighlight/issues/10)
  angående Chrome-rowseren og dvaletilstand for applikationer.

## Ændringer for 5.2 ##

* Nye og opdaterede oversættelser.

## Ændringer for 5.1 ##

* Fjernet debug log output.

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
