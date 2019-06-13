# Realse de foco #

* Autores: Takuya Nishimoto
* Baixe a [versão estável][2]
* Baixe a [versão de desenvolvimento][1]

Ao desenhar um retângulo colorido, este complemento possibilita usuários de
baixa visão, educadores de visão normal ou desenvolvedores, acompanhar a
localização do objeto de navegação do NVDA e o objeto/controle em foco.

O complemento usa as seguintes cores:

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

* Traduções novas e atualizadas.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

## Changes for 6.0 ##

* Traduções novas e atualizadas.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Changes for 5.6 ##

* Traduções novas e atualizadas.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Mudanças na 5.5 ##

* Soluciona o problema com o NVDA 2018.4 e os navegadores web
  Firefox/Chrome.

## Mudanças na 5.4 ##

* Traduções novas e atualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/11)
  relacionado à compatibilidade de versão.

## Mudanças na 5.3 ##

* Traduções novas e atualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/10)
  relacionado ao navegador Google Chrome e ao modo de suspensão do
  aplicativo.

## Mudanças na 5.2 ##

* Traduções novas e atualizadas.

## Mudanças na 5.1 ##

* Removida a saída de log de depuração.

## Mudanças na 5.0 ##

* Os indicadores do objeto de navegação e do modo de foco foram alterados.
* Múltiplos monitores são suportados.
* Agora ele usa a tecnologia GDI Plus para desenho.

## Mudanças na 4.0 ##

* Oculta retângulo se o aplicativo atual estiver em modo dormir.

## Mudanças na 3.0 ##

* Corrigido problema em relação à caixa de combinação expandida.
* Consertados problemas com a barra de tarefas do Windows.
* Capacidade de indicar o modo de foco.

## Mudanças na 2.1 ##

* Traduções novas e atualizadas.

## Mudanças na 2.0 ##

* A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.1 ##

* Alterado retângulo do objeto de navegação para uma linha entalhada.
* Concertado problema com "Recarregar plug-ins".

## Mudanças na 1.0 ##

* No Internet Explorer 10 e no Skype para Windows 8, consertado um problema
  com o navegador de objetos.
* Versão inicial.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
