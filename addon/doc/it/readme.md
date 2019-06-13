# Focus Highlight #

* Autore: Takuya Nishimoto
* Scarica la [versione stabile][2]
* Scarica la [versione in sviluppo][1]

Disegnando un rettangolo colorato, questo addon consente agli utenti
ipovedenti, educatori vedenti o agli sviluppatori di tenere traccia della
posizione dell'oggetto su cui si trova il navigatore ad oggetti, oppure
dell'oggetto che ha il focus.

Sono utilizzati i colori seguenti:

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

* Nuove Traduzioni e aggiornamenti di quelle esistenti.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

## Changes for 6.0 ##

* Nuove Traduzioni e aggiornamenti di quelle esistenti.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Changes for 5.6 ##

* Nuove Traduzioni e aggiornamenti di quelle esistenti.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* Nuove Traduzioni e aggiornamenti di quelle esistenti.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* Nuove Traduzioni e aggiornamenti di quelle esistenti.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* Nuove Traduzioni e aggiornamenti di quelle esistenti.

## Changes for 5.1 ##

* Removed debug log output.

## Cambiamenti per la 5.0. ##

* Sono stati modificati gli indicatori della modalità focus e del navigatore
  ad oggetti.
* Sono supportati monitor multipli
* Per la visualizzazione ora viene usata la tecnologia GDI Plus.

## Cambiamenti per la 4.0. ##

* Nasconde il rettangolo se l'applicazione corrente è in modalità riposo.

## Cambiamenti per la 3.0. ##

* Risolto un problema con le caselle combinate espanse.
* Risolto un problema con il gestore attività di Windows.
* Capacità di indicare la modalità focus.

## Cambiamenti per la 2.1 ##

* Nuove Traduzioni e aggiornamenti di quelle esistenti.

## Cambiamenti per la 2.0 ##

* L'aiuto è disponibile dalla gestione componenti aggiuntivi di NVDA.

## Cambiamenti per la 1.1 ##

* Modificato il navigatore ad oggetti, da rettangolo a linea frastagliata.
* Risolto un problema con il caricamento dei plugin.

## Cambiamenti per la 1.0 ##

* In Internet Explorer 10 e in Skype su Windows 8, risolto un problema con
  il navigatore ad oggetti.
* Versione iniziale.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
