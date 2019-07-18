# Focus Highlight (fremhæv fokus) #

* Forfattere: Takuya Nishimoto
* Download [stabil version][2]
* Download [udviklingsversion][1]

Dette tilføjelsesprogram tegner et rektangel, så svagsynede brugere, seende
instruktører eller udviklere kan finde placeringen af NVDAs navigatorobjekt
og objektet/kontrollen, som har fokus.

Følgende farver bliver brugt af dette tilføjelsesprogram:

* Grøn og tynd rektangel med tynde skråstreger, indikerer gennemsynstilstand
  og det indikere navigatorobjektet.
* Rødt tyndt rektangel for at indikere objektet/kontrolen, som har fokus i
  gennemsynstilstand.
* Rødt tykt rektangel for at indikere, at navigatorobjekt og objekt i fokus
  overlapper i gennemsynstilstand.
* Blåt rektangel med tyk prikket linje for at indikere, at NVDA er i
  fokustilstand, d.v.s. at tastetryk bliver videregivet til kontrollen.

Hvis du vil slå sporing af objekter fra, så afinstaller
tilføjelsesprogrammet.

Når kategorien Fremhævelse af Fokus i NVDA-s indstillingspanel er
tilgængelig, kan følgende indstillinger tilgås.

* Gør fokustilstand standard: Dette felt er som standard aktiveret. Når den
  ikke er markeret, fungerer denne tilføjelse lignende version 5.6 eller
  tidligere versioner, dvs. hvis gennemsynstilstand ikke er tilgængelig for
  en app, vises fokuset ved hjælp af det tykke røde rektangel.
* Fokus i fokustilstand, Fokus i gennemsynstilstand, Navigatorobjekt: Hver
  af disse grupper indeholder farve, tykkelse og stil.

    * Farve: Dette redigeringsfelt giver dig mulighed for at skrive
      HTML-farvekoden, dvs. hexadecimale tal med seks tegn. For eksempel er
      "ffffff" hvid, "ff0000" er rød og så videre. Bemærk at "000000" ikke
      kan bruges.
    * Tykkelse: Dette redigeringsfelt giver dig mulighed for at skrive
      tykkelsen af boksen. Du kan indtaste en værdi mellem 1 og 30.
    * Style: Valgene er Solid, streg, prik, streg prik og streg prik prik.

* Gendan standarder: Denne knap giver dig mulighed for at nulstille dine
  indstillinger til deres oprindelige standardindstillinger.

## Ændringer for 6.1 ##

* Nye og opdaterede oversættelser.
* Løser [problemet](https://github.com/nvdajp/focusHighlight/issues/14) med
  de seneste udviklingsversioner af NVDA.
* Indstillingskategorien Fremhævelse af fokus i NVDA-indstillingsdialog er
  nu tilgængelig. Bemærk, at dette kun er aktuelt med NVDA 2018.3 eller
  nyere.
* [Diskussioner vedrørende tilpasning af
  farver](https://github.com/nvdajp/focusHighlight/issues/3)
* [Diskussioner vedrørende 'Gør fokustilstand
  standard'](https://github.com/nvdajp/focusHighlight/issues/13)

## Ændringer i 6.0 ##

* Nye og opdaterede oversættelser.
* retter [problemet](https://github.com/nvdajp/focusHighlight/issues/13)
  angående gennemsynstilstand.
* Siden denne version, hvis gennemsynstilstanden for NVDA ikke er
  tilgængelig for en applikation, vises det altid, at NVDA er i
  fokustilstand for applikationen, i stedet for at bruge det røde tykke
  rektangel.
* Tykkelsen af linjen, der repræsenterer fokustilstanden, er reduceret til
  halvdelen.

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
