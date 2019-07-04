# Focus hervorheben #

* Authoren: Takuya Nishimoto
* [Stabile Version herunterladen][2]
* [Entwicklerversion herunterladen][1]

Durch Zeichnen eines farbigen Rechtecks ermöglicht diese Erweiterung
sehbehinderten Nutzern, sehenden Lehrern oder Entwicklern die Position des
fokusierten Objektes sowie des Navigator-Objektes auf dem Bildschirm zu
verfolgen.

Die folgenden Farben werden von dieser Erweiterung verwendet:

* Das dünne, gestrichelte, grüne Rechteck zeigt an, dass sich NVDA im
  Lesemodus befindet und dies ist das Navigator-Objekt.
* Das dünne, rote Rechteck zeigt an, dass sich NVDA im Lesemodus befindet
  und dies ist das fokussierte Objekt bzw. Steuerelement.
* Das dicke, rote Rechteck zeigt, dass sich NVDA im Lesemodus befindet und
  dies ist sowohl das Navigator-Objekt als auch das fokussierte Objekt, die
  sich überlappen.
* Das blaue Rechteck mit dicker, gestrichelter Linie zeigt an, dass sich
  NVDA im Fokusmodus befindet, d. h., Schlüsseltypen werden an die Steuerung
  übergeben.

Um das hervorheben von Objekten zu deaktivieren, deinstallieren Sie diese
Erweiterung.

Wenn die Kategorie Fokus-Hervorhebung im Dialogfeld NVDA-Einstellungen
verfügbar ist, können folgende Elemente verwendet werden.

* Setzen Sie den Fokusmodus auf die Standard-Einstellung: Dieses
  Kontrollkästchen ist standardmäßig aktiviert. Wenn das Kontrollkästchen
  deaktiviert ist, verhält sich diese Erweiterung wie die Version 5.6 oder
  älter, d. h., wenn der Suchmodus für eine App nicht verfügbar ist, wird
  der Fokus durch das dicke rote Rechteck angezeigt.
* Fokus im Fokusmodus, Fokus im Lesemodus, Navigator-Objekt: Jede dieser
  Gruppen enthält Farbe, Dicke und Stil.

    * Farbe: In diesem Eingabefeld können Sie den HTML-Farbcode eingeben,
      d. h. einen sechsstelligen Hexadezimalwert. Zum Beispiel ist "ffffff"
      weiß, "ff0000" ist rot, und so weiter. Beachten Sie, dass "00000000"
      nicht verwendet werden kann.
    * Dicke: In diesem Eingabefeld können Sie die Dicke der Box
      eingeben. Sie können einen Wert zwischen 1 und 30 eingeben.
    * Stil: Die Auswahlmöglichkeiten sind Solide, Strich, Punkt,
      Strich-Punkt und Strich-Punkt-Punkt.

* Stellt die Standard-Einstellungen wieder her: Mit dieser Schaltfläche
  können Sie Ihre Einstellungen auf die ursprünglichen Standardwerte
  zurücksetzen.

## Änderungen in 6.1 ##

* Neue und aktualisierte Übersetzungen.
* Behebt den [Fehler](https://github.com/nvdajp/focusHighlight/issues/14)
  mit den letzten Entwicklerversionen von NVDA.
* Die Kategorie Fokus-Hervorhebungen im Dialogfeld der NVDA-Einstellungen
  ist nun verfügbar. Beachten Sie, dass es nur mit NVDA 2018.3 oder neuer
  funktioniert.
* [Diskussionen bzgl. einstellen von
  Farben](https://github.com/nvdajp/focusHighlight/issues/3)
* [Englische Diskussionen bezüglich "Fokusmodus als Standard
  festlegen"](https://github.com/nvdajp/focusHighlight/issues/13)

## Änderungen in 6.0 ##

* Neue und aktualisierte Übersetzungen.
* Behebt den [Fehler](https://github.com/nvdajp/focusHighlight/issues/13)
  bzgl. des Lesemodus.
* Seit dieser Version, wenn der Lesemodus von NVDA für eine Anwendung nicht
  verfügbar ist, wird immer angezeigt, dass sich NVDA im Fokusmodus für die
  Anwendung befindet, anstatt das rote dicke Rechteck zu verwenden.
* Die Dicke der Linie, die den Fokusmodus darstellt, wurde auf die Hälfte
  reduziert.

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

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
