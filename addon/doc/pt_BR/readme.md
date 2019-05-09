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

Para desabilitar o realse de objetos, desinstale o complemento.

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

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
