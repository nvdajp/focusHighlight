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

* Nye og opdaterede oversættelser.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

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

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
