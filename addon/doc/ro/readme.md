# Focus Highlight #

* Autori: Takuya Nishimoto
* Descarcă [Versiunea Stabilă][2]
* Descarcă [versiunea în dezvoltare][1]

La desenarea unui dreptunghi colorat, acest supliment le permite
utilizatorilor cu vedere parțială, educatorilor văzători, sau
dezvoltatorilor să urmărească locația navigatorului de obiecte NVDA și
obiectul/controlul focalizat.

Culorile utilizate de către acest add-on sunt:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

Pentru a dezactiva track obiect, dezinstalează add-on-ul.

## Changes for 6.0 ##

* Traduceri noi și actualizate.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Modificări aduse în versiunea 5.6 ##

* Traduceri noi și actualizate.
* Rezolvă problema de compatibilitate cu snapshot-ul NVDA alpha-16682.

## Modificări aduse în versiunea 5.5 ##

* Adresa problemei în legătură cu NVDA 2018.4 și navigatoarele web Firefox &
  Chrome.

## Modificări aduse în versiunea 5.4 ##

* Traduceri noi și actualizate.
* Adresa [problema](https://github.com/nvdajp/focusHighlight/issues/11) în
  legătură cu compatibilitatea versiunii.

## Modificări aduse în versiunea 5.3 ##

* Traduceri noi și actualizate.
* Adresa [problemei](https://github.com/nvdajp/focusHighlight/issues/10) în
  legătură cu navigatorul Chrome și modul de repaus al aplicației.

## Modificări aduse în versiunea 5.2 ##

* Traduceri noi și actualizate.

## Modificări aduse în versiunea 5.1 ##

* A fost eliminată ieșirea jurnalului diagnosticării.

## Modificări aduse în versiunea 5.0 ##

* Indicatorii obiectului navigator au fost modificați.
* Sunt suportate monitoare multiple.
* Acum, utilizează tehnologia GDI Plus pentru desen.

## Modificări aduse în versiunea 4.0 ##

* Ascunde modul dreptunghi dacă aplicația curentă este în modul de
  hibernare.

## Modificări aduse în versiunea 3.0 ##

* S-a rezolvat problema cu privire la casetele combinate extinse.
* A fost rezolvată problema cu managerul de activități Windows.
* Capabilitatea de a indica modul de focalizare.

## Modificări aduse în versiunea 2.1 ##

* Traduceri noi și actualizate.

## Modificări aduse în 2.0 ##

* Ajutorul suplimentului este valabil din managerul de add-on-uri.

## Modificări aduse în versiunea 1.1 ##

* A fost modificat obiectul navigatorului la linie zâmțată.
* A fost rezolvată problema cu "Reîncarcă plugin-urile".

## Modificări aduse în 1.0 ##

* În Internet Explorer 10 și în Skype pe Windows 8, a fost rezolvată
  problema cu obiectul navigatorului.
* Versiunea inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
