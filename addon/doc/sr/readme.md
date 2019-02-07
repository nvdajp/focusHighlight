# Focus Highlight #

* Autori: Takuya Nishimoto
* Preuzmi[stabilnu verziju][2]
* Preuzmi[razvojnu verziju][1]

Crtanjem obojenog pravougaonika, ovaj dodatak omogućava slabovidim osobama,
učiteljima, ili programerima da prate fokus navigacionog objekta programa
NVDA ili fokusiranu kontrolu.

Sledeće boje ovaj dodatak koristi:

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* Crveni pravougaonik, za prepoznavanje fokusirane kontrole
* Crveni pravougaonik, da označi kada se navigacioni objekat i fokus
  preklapaju.
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

Da onemogućite praćenje objekata, uklonite dodatak

## Changes for 5.6 ##

* Novi i ažurirani prevodi.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* Novi i ažurirani prevodi.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* Novi i ažurirani prevodi.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* Novi i ažurirani prevodi.

## Changes for 5.1 ##

* Removed debug log output.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Promene u 4.0 ##

* Sakri pravougaonik ako je trenutna aplikacija u režimu spavanja.

## Promene u 3.0 ##

* Fixed issue regarding expanded combo box.
* Popravljen problem sa Windows task menadžerom
* Sposobnost da prepozna režim fokusiranja.

## Promene u 2.1 ##

* Novi i ažurirani prevodi.

## Promene u 2.0 ##

* Pomoć za dodatak je dostupna iz upravljača dodataka

## Promene u 1.1 ##

* Promenjen navigacioni objekat u krivu liniju.
* Popravljen problem sa opcijom 'ponovo učitaj dodatke'.

## Promene u 1.0 ##

* U programu Internet Explorer 10 i Skype na Windowsu 8, popravljen problem
  sa navigacionim objektom.
* Prva verzija


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
