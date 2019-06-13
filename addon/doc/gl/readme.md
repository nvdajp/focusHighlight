# Focus Highlight #

* Autores: Takuya Nishimoto
* Descargar [versión estable][2]
* Descarga [versión de desenvolvemento][1]

Ó dibuxar un rectángulo coloreado, este complemento permite ós usuarios con
deficencia visual, educadores videntes, ou desenvolvedores seguir a posición
do navegador de obxectos do NVDA e o obxecto ou control enfocado.

As seguintes cores utilízanse por este complemento:

* Rectángulo fino verde de liñas punteadas para indicar o navegador de
  obxectos.
* Rectángulo fino bermello amosa que NVDA está en modo exploración, e que
  éste é o obxecto/control enfocado.
* Rectángulo groso bermello amosa que NVDA está en modo exploración, e que
  éste é o obxecto/control enfocado.
* Rectángulo groso azul de liñas punteadas indica que NVDA está en modo
  foco, p.ex., as pulsacións de teclas pásanse ao control.

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

* Traduccións novas e actualizadas.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

## Cambios para 6.0 ##

* Traduccións novas e actualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/13)
  en relación co modo exploración.
* Dende esta versión, se o modo exploración do NVDA non está dispoñible para
  unha aplicación, amósase sempre que NVDA está en modo foco para a
  aplicación, en lugar de utilizar o rectángulo groso vermello.
* O grosor da liña que representa o modo foco reduciuse á metade.

## Cambios para 5.6 ##

* Traduccións novas e actualizadas.
* Arranxa o problema de compatibilidade coa compilación de desenvolvemento
  de NVDA alpha-16682.

## Cambios para 5.5 ##

* Soluciona o problema con NVDA 2018.4 e os navegadores web Firefox/Chrome.

## Cambios para 5.4 ##

* Traduccións novas e actualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/11)
  referente ás versións compatibles.

## Cambios para 5.3 ##

* Traduccións novas e actualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/10)
  en relación co navegador Chrome e o modo de aplicación durminte.

## Cambios para 5.2 ##

* Traduccións novas e actualizadas.

## Cambios para 5.1 ##

* Eliminada a saída ó rexistro de depuración.

## Cambios para 5.0 ##

* Cambiáronse os indicadores para o navegador de obxectos e para o Modo
  Foco.
* Admítense múltiples monitores.
* Agora usa a tecnoloxía GDI Plus para dibuxar.

## Cambios para 4.0 ##

* Agocha o rectángulo se a aplicación actual está en modo durminte.

## Cambios para 3.0 ##

* Arranxado un problema vencellado coa Caixa combinada expandida.
* Correxido un problema co xestor de tarefas de Windows.
* Capacidade para indicar modo foco.

## Cambios para 2.1 ##

* Traduccións novas e actualizadas.

## Cambios para 2.0 ##

* A axuda do complemento está dispoñible no Administrador de Complementos.

## Cambios para 1.1 ##

* Cambiado o rectángulo do navegador de obxectos por unha liña irregular.
* Correxido un problema con 'Recargar plugins'.

## Cambios para  1.0 ##

* No Internet Explorer 10 e no Skype en Windows 8, arránxase un problema co
  navegador de obxectos.
* Versión inicial.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
