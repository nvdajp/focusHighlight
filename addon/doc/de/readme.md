# Focus hervorheben #

* Authoren: Takuya Nishimoto
* [Stabile Version herunterladen][2]
* [Entwicklerversion herunterladen][1]

Durch Zeichnen eines farbigen Rechtecks ermöglicht diese Erweiterung
sehbehinderten Nutzern, sehenden Lehrern oder Entwicklern die Position des
fokusierten Objektes sowie des Navigator-Objektes auf dem Bildschirm zu
verfolgen.

Die folgenden Farben werden von dieser Erweiterung verwendet:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

Um das hervorheben von Objekten zu deaktivieren, deinstallieren Sie diese
Erweiterung.

## Changes for 6.0 ##

* Neue und aktualisierte Übersetzungen.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Änderungen für 5.6 ##

* Neue und aktualisierte Übersetzungen.
* Behebt das Kompatibilitätsproblem mit dem NVDA-Snapshot alpha-16682.

## Änderungen für 5.5 ##

* Behebt das Problem mit NVDA 2018.4 und Firefox/Chrome-Internet-Browsern.

## Änderungen für 5.4 ##

* Neue und aktualisierte Übersetzungen.
* Behebt den [Fehler](https://github.com/nvdajp/focusHighlight/issues/11)
  bzgl. der Versionskompatibilität.

## Änderungen für 5.3 ##

* Neue und aktualisierte Übersetzungen.
* Behebt den [Fehler](https://github.com/nvdajp/focusHighlight/issues/10)
  bzgl. Chrome-Browser und Schlafmodus von Anwendungen.

## Änderungen für 5.2 ##

* Neue und aktualisierte Übersetzungen.

## Änderungen für 5.1 ##

* Die Protokollierungsstufe "debug"  wurde entfernt.

## Änderungen in 5.0 ##

* Die Anzeige für den Fokusmodus und für das Navigator-Objekt wurde
  geändert.
* Unterstützt multiple Bildschirme.
* Für Drawing wird nun GDI Plus verwendet.

## Änderungen in 4.0 ##

* Sobald die aktuelle Anwendung im Schlafmodus ist, wird das Rechteck
  ausgeblendet.

## Änderungen in 3.0 ##

* Es wurde ein Problem bei erweiterten Kombinationsfeldern behoben.
* Fehler mit dem Windows-Task-Manager behoben.
* Fähigkeit den Lesemodus anzuzeigen.

## Änderungen in 2.1 ##

* Neue und aktualisierte Übersetzungen.

## Änderungen in 2.0 ##

* Die Hilfe ist nun über den Erweiterungs-Manager verfügbar.

## Änderungen in 1.1 ##

* Das Navigator-Objekt wird nun mit einer gezackten Linie umrandet.
* Fehler behoben, der beim neuladen von Plugins auftrat.

## Änderungen in 1.0 ##

* Problem mit dem Navigator-Objekt in Internet Explorer 10 und Skype für
  Windows 8 behoben.
* Anfängliche Version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
