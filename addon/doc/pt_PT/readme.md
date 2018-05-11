# Focus Highlight #

* Autor: Takuya Nishimoto
* Baixar [versão estável][2]
* Baixar [versão de desenvolvimento][1]

Ao desenhar um rectângulo colorido, este extra permite que os utilizadores
com deficiência visual, educadores com visão ou desenvolvedores detectem a
localização do objecto do navegador nvda e o objeto / control focado.

As seguintes cores são usadas por este extra:

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* Rectângulo fino vermelho, para indicar o objecto / control sob o foco.
* Rectângulo grosso vermelho, para indicar quando o objecto do navegador e o
  objecto focado se sobrepõem.
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

Para desactivar o rastreamento de objecto, desinstale o extra.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Alterações para 4.0 ##

* Esconder o rectângulo se o aplicativo actual estiver no modo de suspensão.

## Alterações para 3.0 ##

* Fixed issue regarding expanded combo box.
* Corrigido problema com o gestor de tarefas do Windows.
* Capacidade de indicar o modo de foco.

## Mudanças para 2.1 ##

* Traduções novas e outras actualizadas.

## Mudanças para 2.0 ##

* A ajuda do extra ficou disponível no gestor de extras.

## Alterações para 1.1 ##

* Alterado o rectângulo do objeto do navegador para uma linha irregular.
* Corrigido problema com 'Recarregar plugins'.

## Alterações para 1.0 ##

* No Internet Explorer 10 e no Skype no Windows 8, reparado um problema com
  o objeto do navegador.
* Versão inicial.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
