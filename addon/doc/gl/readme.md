# Focus Highlight #

* Autores: Takuya Nishimoto
* Descargar [versión estable][2]
* Descarga [versión de desenvolvemento][1]

Ó dibuxar un rectángulo coloreado, este complemento permite ós usuarios con
deficencia visual, educadores videntes, ou desenvolvedores seguir a posición
do navegador de obxectos do NVDA e o obxecto ou control enfocado.

As seguintes cores utilízanse por este complemento:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

Para deshabilitar o seguemento de obxectos, desinstala o complemento.

## Changes for 6.0 ##

* Traduccións novas e actualizadas.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

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

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
